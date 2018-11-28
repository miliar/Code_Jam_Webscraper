#include<string>
#include<algorithm>
#include<map>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<vector>
#include<string>
#include<algorithm>
#include <utility>
#include<sstream>
#include<set>

 using namespace std;
 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
typedef vector<int> VI;

#include<iostream.h>
#include<conio.h>
#define dbg(x) cout<<"#"<<x<<endl;

main()
{
      int n;
      cin>>n;
      vector<string> result(n);
      REP(i,n)
      {
              int p,k,l,ans=0,j;
              cin>>p>>k>>l;
              vector<int> v(l);
              for(j=0;j<l;j++)
              {
                      cin>>v[j];
              }
              sort(all(v));
              reverse(all(v));
              int tc=0,tf=1;;
              for(j=0;j<l;j++)
              {
                                if(tc>=k){tc=0;tf++;ans+=v[j]*tf;
                                    tc++;}
                                else
                                {
                                    ans+=v[j]*tf;
                                    tc++;
                                }
                                
                                
              }
              
              
              //cout<<ans<<endl;
              
                 int y=i+1;
                 char f[10];
                 
                // cout<<(char)y<<"hi"<<endl;
                 result[i]="Case #" ;
                 result[i]+=itoa(y,f,10);
                 result[i] += ":";
                 result[i] += " ";
                 result[i] +=itoa(ans,f,10);
              
      }
      REP(j,sz(result))
      {
              cout<<result[j]<<endl;
      }
      getch();
}
