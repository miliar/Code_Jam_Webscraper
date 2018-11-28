#include <cctype>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <bitset>
#include <assert.h>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <ctime>

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define DBG(z) cout << #z << " : " << (z) << "\n";
#define DBY(x,y) cout << #x << " : " << (x) <<" , "<< #y << " : "<< (y) << "\n";
#define DBZ(x,y,z) cout << #x << " : " << (x) <<" , "<< #y << " : "<< (y) << " , " << #z << " : " << (z) << "\n";
#else
#define DBG(z)
#define DBY(x,y)
#define DBZ(x,y,z)
#endif

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ms(x,y) memset((x),(y),sizeof((x)))
#define all(c) c.begin(),c.end()
#define emp(a,i) (!((a) & (1<<(i))))
#define sh(a) (1<<(a))

#define PI 3.1415926535

using namespace std;
using namespace __gnu_cxx;

int niza[31];//2 - dvete, 1 - surprising, 0 - not surprising
int za_s[31],za_n[31];

void pre(){
    for(int i=0;i<=10;i++)
        for(int j=max(i-2,0);j<=min(i+2,10);j++)
            for(int q=max(i-2,0);q<=min(i+2,10);q++){
                if(abs(j-q)>2)  continue;
                else if(abs(i-j)==2 || abs(i-q)==2 || abs(j-q)==2){
                    if(niza[i+j+q]==0)  niza[i+j+q]=2;
                    else if(niza[i+j+q]==-1)    niza[i+j+q]=1;
                    za_s[i+j+q]=max(za_s[i+j+q],max(i,max(j,q)));
                }
                else{
                    if(niza[i+j+q]==1)  niza[i+j+q]=2;
                    else if(niza[i+j+q]==-1)    niza[i+j+q]=0;
                    za_n[i+j+q]=max(za_n[i+j+q],max(i,max(j,q)));
                }
            }
}

int main()
{
   // ofstream cout("test.txt");
    int t,n,s,p,v[110];
    ms(niza,-1),ms(za_s,-1),ms(za_n,-1);

   /* for(int i=0;i<=30;i++){
        cout<<i<<" ";
        DBZ(niza[i],za_s[i],za_n[i]);
    }*/

    cin>>t;

    for(int q=1;q<=t;q++){
        cin>>n>>s>>p;
        int ans=0;
        pre();
        for(int i=0;i<n;i++){
            cin>>v[i];
            if(niza[v[i]]==1){
                s--;
                if(za_s[v[i]]>=p)  ans++;
            }
            if(niza[v[i]]==0 && za_n[v[i]]>=p)  ans++;
        }
        for(int i=0;i<n;i++){
            if(niza[v[i]]==2 && s>0 && za_s[v[i]]>=p && za_n[v[i]]<p)   ans++,niza[v[i]]=-1,s--;
        }
        for(int i=0;i<n;i++){
            if(niza[v[i]]==2 && s>0){
                s--;
                if(za_s[v[i]]>=p)  ans++;
            }
            else if(niza[v[i]]==2 && s==0 && za_n[v[i]]>=p)  ans++;
        }
        cout<<"Case #"<<q<<": "<<ans<<"\n";
    }

    return 0;
}
