#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

struct ttime
{
   string time;
   int startStation; //0 : this , 1: Not this
};
ttime ta[400+2], tb[400+2];
int n;

string timeadd(string a, int b)
{
   int ha = (a[0] - '0')*10 + (a[1] - '0');
   int ma = (a[3] - '0')*10 + (a[4] - '0');
 
   int hc = 0, mc = 0;
   
   mc = (ma+b)%60;
   hc = ha + (ma+b)/60;
   stringstream ss;
   if(hc < 10) ss << "0";
   ss << hc << ":" ;
   if(mc < 10) ss << "0";
   ss << mc;
   string c = ss.str();
   return c;
}

bool cmp(const ttime& a, const ttime& b)
{
   if(a.time == b.time) return a.startStation > b.startStation;
   return a.time < b.time;
}
void calc(int na, int nb, int cases)
{
   int ansa, ansb, temp, i;
   sort(ta, ta + na + nb, cmp);
   
   temp = 0;
   ansa = 0;
   for( i = 0 ; i < na + nb; i++)
   {
      if(ta[i].startStation == 0) temp++;
      else if(ta[i].startStation == 1)
      {
         if(temp > 0){ ansa += temp; temp = -1; }
         else temp --;
      }
   }
   if(temp > 0) ansa += temp;
   sort(tb, tb + na + nb, cmp);
   
   temp = 0;
   ansb = 0;
   for( i = 0 ; i < na + nb; i++)
   {
      if(tb[i].startStation == 0) temp++;
      else if(tb[i].startStation == 1)
      {
         if(temp > 0){ ansb += temp; temp = -1; }
         else temp --;
      }
   }
   if(temp > 0) ansb += temp;

   cout << "Case #" << cases << ": " << ansa << " " << ansb <<endl;
}
void readIn()
{
   int t, na, nb;
   cin >> n;
   for(int i = 1; i <= n; i++)
   {
      int ka = 0, kb = 0;
      cin >> t >> na >> nb;
      int j;
      for(j = 0; j < na; j++)
      {
         string start, end;
         cin >> start >> end;
         ta[ka].time = start;
         ta[ka].startStation = 0;
         tb[kb].time = timeadd(end, t);
         tb[kb].startStation = 1;
         ka++, kb++;
      }
      
      for(j = 0; j < nb; j++)
      {
         string start, end;
         cin >> start>> end;
         tb[kb].time = start;
         tb[kb].startStation = 0;
         ta[ka].time = timeadd(end, t);
         ta[ka].startStation = 1;
         ka++, kb++;
      }
      calc(na, nb, i);
   }
}
int main()
{
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   readIn();
   return 0;
}
