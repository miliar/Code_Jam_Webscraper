#include <iostream>
#include <cmath>
#define maxn 2222

using namespace std;
int a[maxn],b[maxn];
int ntest,test,k,r,n;
long long ketqua;

void solve()
{
  ketqua=0;
  for(int i=1;i<=n;i++) b[i]=a[i];
  int loop;
  for(loop=1;loop<=r;loop++)
   {
     long long sum=0;               
     int j,i;
     for(j=1;j<=n;j++)  
      {
         sum+=b[j];
         if (sum>k) 
          {
            sum-=b[j];          
            break;                
          }
      }
     ketqua+=sum;     
     j-=1;
     for(i=n+1;i<=n+j;i++) b[i]=b[i-n];
     for(i=j+1;i<=n+j;i++) b[i-j]=b[i];
     bool stop=true;
     for(i=1;i<=n;i++) if (a[i]!=b[i]) { stop=false;break;}
     if (stop) break;
   }
  if (loop>r) loop--;
  ketqua=(r/loop)*ketqua;  
  int forl=r%loop;
  for(loop=1;loop<=forl;loop++)
   {
     long long sum=0;               
     int j,i;
     for(j=1;j<=n;j++)  
       {
          sum+=b[j];
          if (sum>k) 
           {
             sum-=b[j];
             break;                
           }
       }
     ketqua+=sum;     
     j-=1;
     for(i=n+1;i<=n+j;i++) b[i]=b[i-n];
     for(i=j+1;i<=n+j;i++) b[i-j]=b[i];     
   }
}

void enter()
{
 cin>>ntest;
 for(test=1;test<=ntest;test++)
  {
    cin>>r>>k>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    solve();
    cout<<"Case #"<<test<<": ";
    if (test<ntest) cout<<ketqua<<endl;else cout<<ketqua;
  }
}

int main()
{
/* freopen("csmall.in","r",stdin);
 freopen("csmall.out","w",stdout);*/
 enter(); 
 return 0;
}
