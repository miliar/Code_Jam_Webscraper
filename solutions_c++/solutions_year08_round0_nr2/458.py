#include <stdio.h>
#include <map>

using namespace std;

struct times {
    int d, a;
    times(): d(0), a(0){}
    times(int d, int a): d(d), a(a){}
    times(int hd,int md, int ha,int ma): d(hd*60+md), a(ha*60+ma){}
};
struct timesless{
    bool operator()(const times& l, const times& r){
        return l.d < r.d ? true : l.d > r.d ? false : (l.a < r.a ? true : false);
    }
};

typedef map<times, int, timesless> mti;


#define FOR(i,f,t) for(int i=f; i<t; ++i)
#define REP(i,n) for(int i=0; i<n; ++i)

int main(){
    int k;
    FILE* f=fopen("test.txt", "r");
    FILE* fo=fopen("test_out.txt", "w+");
    fscanf(f, "%d", &k);
    REP(i,k){
        mti m[2];
        int t,na,nb, hd,md,ha,ma;
        fscanf(f, "%d %d %d", &t,&na,&nb);
        REP(j,na){
            fscanf(f, "%d:%d %d:%d", &hd,&md, &ha,&ma);
            m[0][times(hd,md,ha,ma)]++;
        }
        REP(j,nb){
            fscanf(f, "%d:%d %d:%d", &hd,&md, &ha,&ma);
            m[1][times(hd,md,ha,ma)]++;
        }
        int trainnum[2]={0,0};
        // while there is timeslots in the shedule
        for (; m[0].size() || m[1].size();){
            int ind=0;
            times ti;
            if (m[0].begin() == m[0].end()) ind=1;
            else if (m[1].begin() != m[1].end()) {
                ind = timesless()(m[0].begin()->first, m[1].begin()->first) ? 0 : 1;   //it[0]->first.d < it[1]->first.d ? 0 : 1;
            }

            // ind is the earliest train
            trainnum[ind]++;

            mti::iterator iter=m[ind].begin();
            ti=iter->first;
            if(!--(iter->second)){
                // remove timeslot
                m[ind].erase(iter);
            }

            // find timeslots for this train on each station, and remove them
            for(ind^=1;; ind^=1){
                iter=m[ind].lower_bound(times(ti.a+t, ti.a+t));
                if(iter==m[ind].end()) break;
                ti=iter->first;
                if(!--(iter->second))
                    //remove timeslot
                    m[ind].erase(iter);
            }
        }
        fprintf(fo, "Case #%d: %d %d\n", i+1, trainnum[0], trainnum[1]);
    }
    return 0;
}
