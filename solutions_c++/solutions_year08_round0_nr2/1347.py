#include <iostream>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, B) for(int A = 0; A < (int)B; A++)
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define ERRO 1e-9
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

struct sched {
    int deph, depm, arrh, arrm;
};

struct train {
    int h, m;
};

sched scheda[120];
sched schedb[120];

bool operator<(train a, train b)
{
    if(a.h == b.h)
        return a.m < b.m;
    return a.h < b.h;
}

bool cmp(sched a, sched b)
{
    if(a.deph == b.deph)
        return a.depm < b.depm;
    return a.deph < b.deph;
}

// True if train a is ready before departure of schedule b
bool avail(train a, sched b)
{
    if(a.h == b.deph)
        return a.m <= b.depm;
    return a.h < b.deph;
}

int main()
{
    int n, t, na, nb;
    scanf("%d", &n);
    FOR(casos, n){
        
        scanf("%d %d %d", &t, &na, &nb);
       
        FOR(i, na){
            char buff[20];
            int h, m;
            scanf("%s", buff);
            sscanf(buff, "%d:%d", &h, &m);
            scheda[i].deph = h;
            scheda[i].depm = m;
            
            scanf("%s", buff);
            sscanf(buff, "%d:%d", &h, &m);
            scheda[i].arrh = h;
            scheda[i].arrm = m;
        }

        FOR(i, nb){
            char buff[20];
            int h, m;
            scanf("%s", buff);
            sscanf(buff, "%d:%d", &h, &m);
            schedb[i].deph = h;
            schedb[i].depm = m;
            
            scanf("%s", buff);
            sscanf(buff, "%d:%d", &h, &m);
            schedb[i].arrh = h;
            schedb[i].arrm = m;
        }

        sort(scheda, scheda + na, cmp);
        sort(schedb, schedb + nb, cmp);

        /*printf("A:\n");
        FOR(i, na)
            printf("%d:%d %d:%d\n", scheda[i].deph, scheda[i].depm, scheda[i].arrh, scheda[i].arrm);
        
        printf("B:\n");
        FOR(i, nb)
            printf("%d:%d %d:%d\n", schedb[i].deph, schedb[i].depm, schedb[i].arrh, schedb[i].arrm);*/

        int posa = 0, posb = 0;
        int respa = 0, respb = 0;
        multiset<train> trainsa;
        multiset<train> trainsb;
        while(posa < na && posb < nb){
            if(cmp(scheda[posa], schedb[posb])){ // A departs first
                //printf("Departure de A\n");
                if(!trainsa.empty() && avail(*(trainsa.begin()), scheda[posa]))
                    trainsa.erase(trainsa.begin());
                else respa++;
                train tmp;
                tmp.h = scheda[posa].arrh;
                tmp.m = scheda[posa].arrm;
                tmp.m += t;
                if(tmp.m >= 60){
                    tmp.m = tmp.m%60;
                    tmp.h++;
                }
                if(tmp.h < 24)
                    trainsb.insert(tmp);
                posa++;
            } else {
                //printf("Departure de B\n");
                if(!trainsb.empty() && avail(*(trainsb.begin()), schedb[posb]))
                    trainsb.erase(trainsb.begin());
                else respb++;
                train tmp;
                tmp.h = schedb[posb].arrh;
                tmp.m = schedb[posb].arrm;
                tmp.m += t;
                if(tmp.m >= 60){
                    tmp.m = tmp.m%60;
                    tmp.h++;
                }
                if(tmp.h < 24)
                    trainsa.insert(tmp);
                posb++;
            }
            /*printf("Trens em A\n");
            for(set<train>::iterator it = trainsa.begin(); it != trainsa.end(); it++)
                printf("%d:%d\n", (*it).h, (*it).m);
            printf("Trens em B\n");
            for(set<train>::iterator it = trainsb.begin(); it != trainsb.end(); it++)
                printf("%d:%d\n", (*it).h, (*it).m);*/
        }
        if(posa == na){
            while(posb < nb){
                if(!trainsb.empty() && avail(*(trainsb.begin()), schedb[posb]))
                    trainsb.erase(trainsb.begin());
                else respb++;
                posb++;
            }
        }
        if(posb == nb){
            while(posa < na){
                if(!trainsa.empty() && avail(*(trainsa.begin()), scheda[posa]))
                    trainsa.erase(trainsa.begin());
                else respa++;
                posa++;
            }
        }
        printf("Case #%d: %d %d\n", casos + 1, respa, respb);
    }
    return 0;

}

