#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <string>
#define rep(i,n) for(int i=0;i<n;i++)
#define For(i,a,b) for(int i=a;i<=b;i++)
#define tr(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define all(x) x.begin(),x.end()
#define pb push_back
using namespace std;
const int inf=~0U>>1;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef long long LL;
template<class T> bool get_max(T&a,T&b) {
    return b>a?a=b,1:0;
}
template<class T> bool get_min(T&a,T&b) {
    return b<a?a=b,1:0;
}

string cstr[500];
string dstr[500];
string str;
int C,D,N;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    int times=1;
    while (T--) {
        cin>>C;
        rep(i,C) cin>>cstr[i];
        cin>>D;
        rep(i,D) cin>>dstr[i];
        cin>>N;
        cin>>str;
        string ss="";
        for (int i=0;i<str.size();i++) {
            if (i==0) {
                ss+=str[i];
                continue;
            }
            ss+=str[i];
            for (int j=0;j<C;j++) {
                string t="";
                t+=cstr[j][0];
                t+=cstr[j][1];
                string tt="";
                tt+=cstr[j][1];
                tt+=cstr[j][0];
                if (ss.size()<=1) break;
                string t1="";
                int n=ss.size();
                t1+=ss[n-2];
                t1+=ss[n-1];
                if (t1==t||t1==tt) {
                    string t2="";
                    for (int k=0;k<n-2;k++) t2+=ss[k];
                    ss=t2;
                    ss+=cstr[j][2];
                }
            }

            if(ss.size()<=1) continue;
            for (int j=0;j<D;j++) {
                int st=-1,et=-1;
                if (ss.size()<=1) break;
                for (int k=0;k<ss.size();k++) {
                    if (ss[k]==dstr[j][0]) {
                        st=k;
                        break;
                    }
                }
                for (int k=0;k<ss.size();k++) {
                    if (ss[k]==dstr[j][1]) {
                        if(k!=st) {
                            et=k;
                            break;
                        }
                    }
                }

                //bool flag=false;
                if (st!=-1&&et!=-1&&st<et) {
                    //flag = true;
                    string t1="";
                    //if(st>et) swap(st,et);
                    //for (int k=0;k<st;k++) t1+=ss[k];
                    for (int k=et+1;k<ss.size();k++) {
                        t1+=ss[k];
                    }
                    ss=t1;
                }
                //if(flag) continue;
                //cout<<ss<<endl;
                st=-1,et=-1;
                for (int k=0;k<ss.size();k++) {
                    if (ss[k]==dstr[j][1]) {
                        st=k;
                        break;
                    }
                }
                for (int k=0;k<ss.size();k++) {
                    if (ss[k]==dstr[j][0]) {
                        if(k!=st) {
                            et=k;
                            break;
                        }
                    }
                }
                if (st!=-1&&et!=-1&&st<et) {
                    string t1="";
                    //if(st>et) swap(st,et);
                    //for (int k=0;k<st;k++) t1+=ss[k];
                    for (int k=et+1;k<ss.size();k++) {
                        t1+=ss[k];
                    }
                    ss=t1;
                }
            }
        }
        printf("Case #%d: [",times++);
        for (int i=0;i<ss.size();i++) {
            if(i==0) printf("%c",ss[i]);
            else printf(", %c",ss[i]);
        }
        printf("]\n");
    }
    return 0;
}
