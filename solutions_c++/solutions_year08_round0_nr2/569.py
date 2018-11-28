#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

struct Event
{
   Event(int hr, int min, int pos, int type)
      : m_hr(hr), m_min(min), m_pos(pos), m_type(type) {}

   bool operator<(const Event& rhs) const
   {
      if(m_hr != rhs.m_hr)
         return m_hr < rhs.m_hr;
      if(m_min != rhs.m_min)
         return m_min < rhs.m_min;
      if(m_type != rhs.m_type) // first arrive, then leave
         return m_type > rhs.m_type;
      return m_pos < rhs.m_pos;
   }
   int m_hr;
   int m_min;
   int m_pos; // 0 for station A, 1 for station B
   int m_type; // 0 for leaving, 1 for arriving
};

int main(void)
{
   int n;
   scanf("%d", &n);
   for(int i = 1; i <= n; ++i)
   {
      printf("Case #%d: ", i);

      int turnaround;
      scanf("%d", &turnaround);

      int na, nb;
      scanf("%d%d", &na, &nb);

      vector<Event> eventlist;
      for(int j = 0; j < na; ++j) // A -> B
      {
         int begin_h, begin_m, end_h, end_m;
         scanf("%d:%d%d:%d", &begin_h, &begin_m, &end_h, &end_m);
         end_m += turnaround;
         if(end_m > 60)
         {
            end_h += (end_m / 60);
            end_m %= 60;
         }
         eventlist.push_back(Event(begin_h, begin_m, 0, 0));
         eventlist.push_back(Event(end_h, end_m, 1, 1));
      }
      for(int j = 0; j < nb; ++j) // B -> A
      {
         int begin_h, begin_m, end_h, end_m;
         scanf("%d:%d%d:%d", &begin_h, &begin_m, &end_h, &end_m);
         end_m += turnaround;
         if(end_m > 60)
         {
            end_h += (end_m / 60);
            end_m %= 60;
         }
         eventlist.push_back(Event(begin_h, begin_m, 1, 0));
         eventlist.push_back(Event(end_h, end_m, 0, 1));
      }

      int avail_a = 0;
      int avail_b = 0;
      int req_a = 0;
      int req_b = 0;
      sort(eventlist.begin(), eventlist.end());
      for(vector<Event>::const_iterator j = eventlist.begin();
            j != eventlist.end(); ++j)
      {
         int pos = j->m_pos;
         int type = j->m_type;
         if(type == 0) // leaving
         {
            if(pos == 0)
            {
               if(avail_a == 0)
                  ++req_a;
               else
                  --avail_a;
            }
            else if(pos == 1)
            {
               if(avail_b == 0)
                  ++req_b;
               else
                  --avail_b;
            }
         }
         else if(type == 1) // arriving
         {
            if(pos == 0)
               ++avail_a;
            else if(pos == 1)
               ++avail_b;
         }
      }

      printf("%d %d\n", req_a, req_b);
   }
}
