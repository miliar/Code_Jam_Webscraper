#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>

using namespace std;
int p,q;
bool d[100001];
int d2[1000];
bool v[1000];
int a[1000];
int ans,c;

void Dfs2(int k)
{
     if(k<=0||k>p) return;
     if(d[k]==false) return;    
     c++;
     //d[k]=false;
     Dfs2(k-1);
     Dfs2(k+1);
}

void Check()
{
     int i,j,k;
     memset(d,true,sizeof(d));
     //d[0]=d[p+1]=false;
     c=0;
     for(i=1;i<=q;i++) {
        k=a[i];
        d[k]=false;
        for(j=k-1;j>=1;j--)
          if(d[j]==false) break;
          else c++;
        for(j=k+1;j<=p;j++)
           if(d[j]==false) break;
           else c++;
        //Dfs2(k);
        //c--;
        //cout<<c<<endl;
     }
     //cout<<endl;
     if(c<ans) {
       ans=c;
       //for(i=1;i<=q;i++) cout<<a[i]<<" ";
       //cout<<endl;
     }
}

void Dfs(int dep)
{
     if(dep>q) {
        Check();
        return;
     }
     int i;
     for(i=1;i<=q;i++)
        if(v[i]) {
           a[dep]=d2[i];
           v[i]=false;
           Dfs(dep+1);
           v[i]=true;
        }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);  freopen("p3.out","w",stdout);
    int kase;
    int i,j,k;
    cin>>kase;
    for(i=1;i<=kase;i++) {
      cout<<"Case #"<<i<<": ";                   
      cin>>p>>q;
      for(j=1;j<=q;j++) cin>>d2[j];
      ans=100000000;
      memset(v,true,sizeof(v));
      Dfs(1);
      cout<<ans<<endl;
    }
    return 0;
}
