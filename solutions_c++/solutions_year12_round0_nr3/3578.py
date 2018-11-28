#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define fr(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
int main(){
	
	freopen("inp1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int tt,c,n,s,pp,p1,p2,p,x,i,t[1001],a,b;
    fr(i,1,1001)t[i]=0;
    cin>>tt;c=1;    
    while(tt--){ cin>>a>>b;cout<<"Case #"<<c<<": ";c++;s=0;
    fr(i,1,1001)t[i]=0;
  fr(i,a,b+1){ x=i;if(x==1000)break;
    if(t[i]==0 || t[i]==1)
     { t[i]=1; if(x>=100) {p=x%10;p1=(x/10)%10;p2=x/100;if(p1>0){pp=(x%100)*10+p2;if(pp<=b && pp>=a && pp!=x){t[pp]=1;s++;} } 
                           if(p>0) {pp=(x%10)*100+(x/10);if(pp<=b && pp>=a && pp!=x){t[pp]=1;s++;} }
                          }
       else if(x>10) { p=x%10;p1=x/10;if(p>0){pp=p*10+p1;if(pp<=b && pp>=a && pp!=x){t[pp]=1;s++;}  } } 
     } 
   }  
    cout<<s/2<<endl;
    }
    return 0;
}
