#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <string>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)))
#define Out(x) (cout << #x << " = " << x << endl)

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T> inline void out(T x, int n){  for(int i = 0; i < n; ++i)  cout << x[i] <<" " ;    cout << endl;    }
template<class T> inline void out(T x, int n, int m){  for(int i = 0; i < n; ++i)    out(x[i], m);    cout << endl;    }
template<class T> inline void out(char * x) { for(int i =0;i< (int) strlen(x); i++)  cout << x[i] <<" " ;    cout << endl;  }

const double pi = acos(-1.0);
const double eps = 1e-8;
const int INF = 0x7fffffff;

char line[100];
int app[500];
int num[100];
int len;
long long ans;

void todec(int b)
{
        int i;
        for(i=0;i<len-1;i++)
        {
                ans=(ans+num[i])*b;
        }
        ans+=num[len-1];
}

int main()
{
//        freopen("A-small-attempt2.in","r",stdin);
//        freopen("A-small-attempt2.out","w",stdout);

        freopen("A-large.in","r",stdin);
        freopen("A-large.out","w",stdout);

        int i,cases,N;
        cin>>N;
        getchar();
        for(cases=1; cases<=N;cases++)
        {
                ans=0;
                mem(app,-1);
                mem(num,0);

                gets(line);

                len=strlen(line);
                app[line[0]]=1;
                num[0]=1;

                int t=0;
                for(i=1;i<len;i++)
                {
                        if(app[line[i]]==-1)
                        {
                                app[line[i]]=t;
                                num[i]=t;
                                t++;
                                if(t==1)
                                        t=2;
                        }
                        else
                        {
                                num[i]=app[line[i]];
                        }
                }
                if(t==0)
                        t=2;
//                Out(t);
//                out(num,len);
                todec(t);
                printf("Case #%d: ",cases);
                cout<<ans<<endl;
        }
        return 0;
}
