#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;
#define REP(i, n) for(int i = 0; i <(n); i++)

typedef long long LL;

LL c[10000], p[10000];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);

    for(int tcase = 1; tcase <= t; tcase++) {

               int n;
               scanf("%d", &n);

               REP(i, n) {
                      string s;
                      LL pos;
                      cin>>s>>pos;
                      if(s=="O") c[i]=0;
                      else c[i]=1;
                      p[i] = pos;
                }

                LL bpos, opos;
                bpos=opos=1;

                LL bt, ot;
                bt=ot=0;
                LL lturn = 0;

                LL time;
                REP(i, n) {
                    switch(c[i]) {
                        case 0:
                        time = abs(opos-p[i])+1;
                        if(lturn==c[i]) {
                            ot += time;
                        } else {
                            if((ot+time)<=bt) {
                                ot = bt+1;
                            } else {
                                ot += time;
                            }
                        }
                        opos = p[i];
                        break;


                        case 1:
                        time = abs(bpos-p[i])+1;
                        if(lturn==c[i]) {
                            bt += time;
                        } else {
                            if((bt+time)<=ot) {
                                bt = ot+1;
                            } else {
                                bt += time;
                            }
                        }
                        bpos = p[i];
                        break;

                    }
                    lturn = c[i];
                }
                //////
                cout<<"Case #"<<tcase<<": "<<max(ot, bt)<<"\n";
    }
}

