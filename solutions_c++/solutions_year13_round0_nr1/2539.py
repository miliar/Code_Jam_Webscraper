#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

//BEGINTEMPLATE_BY_SCORPIOLIU
const double PI  = acos(-1.0);
const double EPS = 1e-11;
const double INF  = 1E200;

typedef long long int64;
typedef unsigned long long uint64;

typedef pair<int,int> ipair;
#define MP(X,Y) make_pair(X,Y)
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))

#define REP(i,a) for(int i=0;i<int(a);++i)
#define REP2(i,n,m) for(int i=n;i<(int)(m);++i)
#define FORE(it,a) for (typeof((a).begin()) it=(a).begin();it!=(a).end();++it)
#define ALL(a) (a).begin(),(a).end()
//ENDEMPLATE_BY_SCORPIOLIU

#define SMALL
//#define LARGE

int main()
{
#ifdef SMALL
    //ifstream fin("A-small-practice.in");ofstream fout("A-small-practice.out");
    //ifstream fin("A-small-attempt0.in");ofstream fout("A-small-attempt0.out");
    freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("A-large-practice.in");ofstream fout("A-large-practice.out");
    //ifstream fin("A-large.in");ofstream fout("A-large.out");
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
#endif
    char tb[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
    'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    int N;
    string s;
    cin>>N;
    getline(cin, s);
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        bool flag = false;
        bool flag2 = true;
        char win = NULL;
        vector<string>a;
        for (int i = 0; i < 4; i++) {
            getline(cin, s);
            a.push_back(s);
        }
        getline(cin, s);

        for (int i = 0; i < 4 ; i++) {
            flag2 = true;
            for (int j = 0; j < 4; j++) {
                if (a[j][i] == '.') {
                    flag = true;
                    flag2 = false;
                    win = NULL;
                    break;
                }
                if (win == NULL) {
                    if (a[j][i] != 'T') {
                        win = a[j][i];
                    }
                } else {
                    if (a[j][i] != 'T' && win != a[j][i]) {
                        flag2 = false;
                        win = NULL;
                        break;
                    }
                }
            }

            if (flag2 && win != NULL) {
                break;
            }
        }
        if (flag2 && win != NULL) {
            ;
        } else {
            for (int j = 0; j < 4 ; j++) {
                flag2 = true;
                for (int i = 0; i < 4; i++) {
                    if (a[j][i] == '.') {
                        flag2 = false;
                        win = NULL;
                        break;
                    }
                    if (win == NULL) {
                        if (a[j][i] != 'T') {
                            win = a[j][i];
                        }
                    } else {
                        if (a[j][i] != 'T' && win != a[j][i]) {
                            flag2 = false;
                            win = NULL;
                            break;
                        }
                    }
                }
                if (flag2 && win != NULL) {
                    break;
                }
            }
        }
        if (flag2 && win != NULL) {
            ;
        } else {
            flag2 = true;
            for (int i = 0; i < 4 ; i++) {
                if (a[i][i] == '.') {
                    flag2 = false;
                    win = NULL;
                    break;
                }
                if (win == NULL) {
                    if (a[i][i] != 'T') {
                        win = a[i][i];
                    }
                } else {
                    if (a[i][i] != 'T' && win != a[i][i]) {
                        flag2 = false;
                        win = NULL;
                        break;
                    }
                }
            }
        }

        if (flag2 && win != NULL) {
            ;
        } else {
            flag2 = true;
            for (int i = 0; i < 4 ; i++) {
                if (a[i][3-i] == '.') {
                    flag2 = false;
                    win = NULL;
                    break;
                }
                if (win == NULL) {
                    if (a[i][3-i] != 'T') {
                        win = a[i][3-i];
                    }
                } else {
                    if (a[i][3-i] != 'T' && win != a[i][3-i]) {
                        flag2 = false;
                        win = NULL;
                        break;
                    }
                }
            }

        }
        //cout<<win<<flag<<" " <<flag2<< " " <<win;
        if (win == NULL && flag) {
            cout<<"Game has not completed";
        } else if (flag2) {
            cout<<win<<" won";
        } else if (!flag2 && !flag) {
            cout<<"Draw";
        }
        //////////////////////////////////////
        cout<<endl;
    }


    return 0;
}
