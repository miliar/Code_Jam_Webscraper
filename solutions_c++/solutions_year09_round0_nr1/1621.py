#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
const double eps = 1e-11;
const double pi = acos(-1.0);
const double inf = 1e17;
#define swap(a,b) {a^=b;b^a=;a^=b;}
#define two(X) (1<<(X))
#define pair <int,int> pii
#define SZ(x) ((int)x.size())
template<class T> T gcd(const T &a,const T &b) {return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(const T &a,const T &b) {return a*(b/gcd(a,b));}
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
int L,D,N;
int cnt;
string lang[5001];
int main()
{
        int i,j,k,l;
        int flag,flag1;
        string test,tmp;
        vector <string> group;
        cin>>L>>D>>N;
        for (i=0;i<D;i++){
            cin>>lang[i];
        }
        for (i=0;i<N;i++){
            cin>>test;
            cnt = 0;
            flag = 0;
            group.erase(group.begin(),group.end());
            tmp = "";
            for (j=0;j<SZ(test);j++){
                if (test[j]=='('){
                   flag = 1;
                }else if (test[j]==')'){
                   flag = 0;
                   group.push_back(tmp);
                   tmp = "";
                }else{
                      if (flag == 0){
                         tmp += test[j];
                         group.push_back(tmp);
                         tmp = ""; 
                      }else{
                         tmp += test[j];
                      }
                }         
            }
            for (j=0;j<D;j++){
                flag = 1;
                for (k=0;k<L;k++){
                    flag1 = 0;
                    for (l=0;l<SZ(group[k]);l++){
                        if (lang[j][k] == group[k][l]) flag1 = 1;
                    }
                    if (flag1 != 1){
                       flag = 0;
                       break;
                    }
                }
                if (flag == 1) cnt++;
            }
//            for (j=0;j<SZ(group);j++)
//                cout<<group[j]<<endl;
        printf("Case #%d: %d\n",i+1,cnt);
        }
        return 0;
}

