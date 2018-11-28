#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

#define sz(a) int((a).size())

struct Trip {
   char source;
   int dep_time, arr_time;

   Trip(char src, int dtime, int atime) :
      source(src), dep_time(dtime), arr_time(atime) {}
   Trip(char src, int dhh, int dmm, int ahh, int amm) :
      source(src), dep_time(dhh*60 + dmm), arr_time(ahh*60 + amm) {}
   bool operator< (const Trip& x) const {
      return dep_time < x.dep_time ||
             dep_time == x.dep_time && arr_time < x.arr_time;
   }
};

int main(int argc, char *argv[]) {
   int N;
   scanf("%d", &N);

   for (int tc = 1; tc <= N; ++tc) {
      int T;
      scanf("%d", &T);

      int NA, NB;
      scanf("%d %d", &NA, &NB);

      vector<Trip> sched;
      while (NA-- > 0) {
         int dephh, depmm, arrhh, arrmm;
         scanf("%d:%d %d:%d", &dephh, &depmm, &arrhh, &arrmm);
         sched.push_back(Trip('A', dephh, depmm, arrhh, arrmm));
      }
      while (NB-- > 0) {
         int dephh, depmm, arrhh, arrmm;
         scanf("%d:%d %d:%d", &dephh, &depmm, &arrhh, &arrmm);
         sched.push_back(Trip('B', dephh, depmm, arrhh, arrmm));
      }

      sort(sched.begin(), sched.end());
      priority_queue< int, vector<int>, greater<int> > trains[2];  // 0 -> A   1 -> B
      int ans[2] = {0, 0};
      for (int i = 0; i < sz(sched); ++i) {
         int station_idx = sched[i].source == 'A' ? 0 : 1;
      /*
         printf("Source: %c  Dep %4d   Arr %4d  Q: %4d\n",
                sched[i].source, sched[i].dep_time, sched[i].arr_time,
                trains[station_idx].empty() ? -1 : trains[station_idx].top());
      */
         if (trains[station_idx].empty() ||
             trains[station_idx].top() > sched[i].dep_time) {
            ++ans[station_idx];
            trains[station_idx].push(sched[i].dep_time);
         }
         trains[station_idx].pop();
         trains[1-station_idx].push(sched[i].arr_time+T);
      }

      printf("Case #%d: %d %d\n", tc, ans[0], ans[1]);
   }
   return 0;
}
