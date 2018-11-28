#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string>
#include<iomanip>
#define beginT int _T; cin>>_T; for(int _t=1;_t<=_T;_t++)
#define printT(_ans) cout<<"Case #"<<_t<<": "<<_ans<<endl
using namespace std;

int main()
{
   beginT
   {
         int N;
         cin>>N;
         char arr[N][N];
         long double wp[N],owp[N],oowp[N];
         int a[N],s[N];
         for(int i=0;i<N;i++)
         {
                 a[i]=0,s[i]=0;
                 for(int j=0;j<N;j++)
                 {
                         cin>>arr[i][j];
                         if(arr[i][j]!='.')
                         {
                                         if(arr[i][j]=='1')
                                                      a[i]++;
                                         s[i]++;
                         }
                 }
                 wp[i] = (long double)a[i]/(long double)s[i];
                 cin.ignore();
         }
         for(int i=0;i<N;i++)
         {
                 long double owpi=0;
                 int s1=0;
                 for(int j=0;j<N;j++)
                 {
                         if(i==j || arr[j][i]=='.') continue;
                         owpi+=((long double)(a[j]-(arr[j][i]=='1'))/(long double)(s[j]-(arr[j][i]!='.')));
                         s1++;
                 }
                 owp[i] = owpi/(long double)(s1);
         }
         for(int i=0;i<N;i++)
         {
                 long double oowpi=0;
                 int s1=0;
                 for(int j=0;j<N;j++)
                 {
                         if(i==j || arr[j][i]=='.') continue;
                         oowpi+=owp[j];
                         s1++;
                 }
                 oowp[i] = oowpi/(long double)(s1);
         }
         printT("");
         for(int i=0;i<N;i++)
         {
                 long double rti = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
                 cout<<setprecision(12)<<rti<<endl;
         }
   }
   return 0;
}
