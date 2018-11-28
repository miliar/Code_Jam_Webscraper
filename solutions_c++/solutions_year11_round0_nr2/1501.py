/* magicka */
/* produced by wegnahz */
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define skip(x) for(int i=1;i<=(x);++i) getchar();
#define xx first
#define yy second
#define MP make_pair
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define fill0(a) memset(a,0,sizeof(a));
typedef pair<int,int> ipair;
const int inf=0x3FFFFFFF;
const double pi=acos(-1.0);
const double eps=1e-8;
const int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
inline void show(int *a,int n){
  for (int i=0;i<=n;i++) cout<<a[i]<<' ';cout<<endl;}
int num,n,m,ans;
bool d[26][26];
char c[26][26],s[1000000];
int main(){
    int tt,ii,i,j,k,t;
    char ch1,ch2,ch;
    #ifndef ONLINE_JUDGE
    freopen("magicka.in","r",stdin);
    freopen("magicka.out","w",stdout);
    #endif
    cin>>tt;
    for (ii=1;ii<=tt;ii++)
    {
        fill0(c); fill0(d);
        cin>>k;
        while (k--)
        {
            cin>>ch1>>ch2;
            cin>>c[ch1-'A'][ch2-'A'];
            c[ch2-'A'][ch1-'A']=c[ch1-'A'][ch2-'A'];
        }
        cin>>k;
        while (k--)
        {
            cin>>ch1>>ch2;
            d[ch1-'A'][ch2-'A']=d[ch2-'A'][ch1-'A']=1;
        }
        cin>>n; m=0;
        for (i=0;i<n;i++)
        {
            cin>>ch; s[m++]=ch;
            while (m>=2 && c[s[m-1]-'A'][s[m-2]-'A']>0)
            {
                s[m-2]=c[s[m-1]-'A'][s[m-2]-'A'];
                m--;
            }
            for (j=m-2;j>=0;j--)
                if (d[s[j]-'A'][s[m-1]-'A'])
                {
                    m=0;
                    break;
                }
        }
        cout<<"Case #"<<ii<<": [";
        if (m==0)cout<<"]\n";else
        {
            cout<<s[0];
            for (i=1;i<m;i++) cout<<", "<<s[i];
            cout<<"]\n";
        }
    }        
    return 0;
}
