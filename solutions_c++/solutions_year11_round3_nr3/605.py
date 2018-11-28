#include<iostream>
using namespace std;
int main()
{
    freopen("C:\\Users\\Administrator\\Desktop\\C-small-attempt2.in","r",stdin);
    freopen("C:\\Users\\Administrator\\Desktop\\out1","w",stdout);
    long long T;
    cin>>T;
    long long i;
    long long a[10001];
    long long allgcd[10001];//后k个数的最大公约数 
    for(i=0;i<T;i++)
    {
         int j,k;
         int n,l,h;
         cin>>n>>l>>h;
         for(j=0;j<n;j++)
         cin>>a[j];
         
         cout<<"Case #"<<i+1<<": ";
         for(j=l;j<=h;j++)
         {
            for(k=0;k<n;k++)
              if(j%a[k]==0||a[k]%j==0)
                 continue;
              else break;
            if(k==n)
               break;
         }
         if(j<=h)
         cout<<j<<endl;
         else cout<<"NO"<<endl;
    }
  //  system("pause");
    return 0;
}
