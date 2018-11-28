#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int > > VVI;
typedef pair <int,int> PII;
typedef vector <LL> VL;
typedef vector <string> VS;

#define INF 1000000000

VS split(string s, string t=" ") {
    VS ret;
    int a,b=0;
    while ((a=s.find_first_not_of(t,b))!=-1) {
        b=s.find_first_of(t,a);
        ret.push_back(s.substr(a,b-a));
    }
    return ret;
}

string print(int time)
{
    char buf[100];
    sprintf(buf,"%02d:%02d",time/60,time%60);
    return buf;
}

int main()
{
    int n;
    scanf("%d", &n);

    for (int tr=0; tr<n; tr++) {
        int turn;
        scanf("%d", &turn);

        int na, nb;
        scanf("%d %d", &na, &nb);

        vector<pair<int,int> > ab;
        set<int> times;
        for (int i=0; i<na; i++) {
            int t[4];
            scanf("%d:%d %d:%d", &t[0], &t[1], &t[2], &t[3]);
            ab.push_back(make_pair(t[0]*60+t[1], t[2]*60+t[3]));
            
            times.insert(t[0]*60+t[1]);
            times.insert(t[2]*60+t[3]);
        }

        vector<pair<int,int> > ba;
        for (int i=0; i<nb; i++) {
            int t[4];
            scanf("%d:%d %d:%d", &t[0], &t[1], &t[2], &t[3]);
            ba.push_back(make_pair(t[0]*60+t[1], t[2]*60+t[3]));
            times.insert(t[0]*60+t[1]);
            times.insert(t[2]*60+t[3]);
        }

        int acnt,bcnt;
        acnt=bcnt=0;

        priority_queue<int,vector<int>, greater<int> > seta; 
        priority_queue<int,vector<int>, greater<int> > setb; 

//        for (typeof(times.begin()) it=times.begin(); it != times.end(); it++) {
//            int cur = *it;
        for (int cur=0; cur<24*60; cur++) {
            for (int i=0; i<na; i++) {
                if (ab[i].first == cur) {
                    if (seta.empty()) {
                        acnt++;
                    } else {
                        int tmp = seta.top();
                        if (tmp > ab[i].first) {
                            acnt++;
                        } else {
                            seta.pop();
                        }
                    }
                    setb.push(ab[i].second+turn);
                }
            }
            for (int i=0; i<nb; i++) {
                if (ba[i].first == cur) {
                    if (setb.empty()) {
                        bcnt++;
                    } else {
                        int tmp = setb.top();
                        if (tmp > ba[i].first) {
                            bcnt++;
                        } else {
                            setb.pop();
                        }
                    }
                    seta.push(ba[i].second+turn);
                }
            }
        }


        /*
        int acnt=na;
        int bcnt=nb;
        for (int i=0; i<na; i++) {
            for (int j=0; j<nb; j++) {
                if (ab[i].first >= ba[j].second + t) {
                    acnt--;
                    break;
                }
            }
        }
        for (int j=0; j<nb; j++) {
            for (int i=0; i<na; i++) {
                if (ba[j].first >= ab[i].second + t) {
                    bcnt--;
                    break;
                }
            }
        }
        */

        printf("Case #%d: %d %d\n", tr+1, acnt, bcnt);
    }

}

