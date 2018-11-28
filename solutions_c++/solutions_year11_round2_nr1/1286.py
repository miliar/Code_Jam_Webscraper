#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <map>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef vector<double> vd;
typedef queue<int> qi;

#define fori(i, n) for(i=0;i<n;i++)
#define fordi(i, n) for(int i=0;i<n;i++)
#define INF 0x7fffffff

char sc() {char r; if (scanf("%c", &r) != 1) {printf("-1"); exit(0);} return r;}
int si() {int r; if (scanf("%d", &r) != 1) {printf("-1"); exit(0);} return r;}
long long sli() {long long r; if (scanf("%lld", &r) != 1) {printf("-1"); exit(0);} return r;}
double sf() {double r; if (scanf("%lf", &r) != 1) {printf("-1"); exit(0);} return r;}



main() {
    int t = si();
    fordi(ii,t) {
        vii table;
        int n=si();
        table.resize(n);
        fordi(j,n) {
            table[j].resize(n);
            string s;
            cin >> s;
            fordi(k,n){
                char c=s[k];
                if (c=='1') table[j][k] = 1;
                if (c=='0') table[j][k] = 0;
                if (c=='.') table[j][k] = 2;
            }
        }
        
        vd wp;
        wp.resize(n);
        fordi(j,n) {
            int played=0,won=0;
            fordi(k,n) {
                if (table[j][k] == 1) won++;
                if (table[j][k] <=1) played++;
                //printf("%d",table[j][k]);
            }
            //printf("\n");
            if (played !=0)
                wp[j] = (double) won / (double) played;
        }

        vd owp;
        owp.resize(n);
        fordi(j,n) {
            vd wpj;
            wpj.resize(n);
            fordi(s,n) {
                if (table[j][s]==2) continue;
                int played=0,won=0;
                fordi(k,n) {
                    if(k==j)continue;
                    if (table[s][k] == 1) won++;
                    if (table[s][k] <=1) played++;
                }
                if (played !=0)
                    wpj[s] = (double) won / (double) played;
                //printf("wpj %f\n", wpj[s]);
            }
            double sum=0;
            int played=0;
            fordi(s,n) {
                if(table[j][s]!=2) {
                    played++;
                    sum += wpj[s];
                }
            }
            owp[j] = sum / played;
        }

        vd oowp;
        oowp.resize(n);
        fordi(j,n) {
            double sum=0;
            int played=0;
            fordi(k,n) {
                if (table[j][k] !=2) {
                    sum += owp[k];
                    played++;
                }
            }
            oowp[j] = sum / played;
        }
        printf("Case #%d:\n",ii+1);
        fordi(j,n) {
            printf("%.9lf\n", 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j]);
        }   

    }
}
