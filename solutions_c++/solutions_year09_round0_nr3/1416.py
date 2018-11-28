#include <iostream>
#include <string>

using namespace std;

string ss="welcome to code jam";

int main()
{
 freopen("out","w",stdout);
 int zz;
 scanf("%d\n",&zz);
 for(int z=0; z<zz; z++)
 {
  string s;
  getline(cin,s);
  //scanf("\n");
  int a[1000][20];
  for(int j=0; j<s.length(); j++)for(int i=0;i<19; i++)
  {
   a[j][i]=0;
  }
  if(s[0]=='w')a[0][0]=1;
  int n=s.length();
  for(int i=0; i<=n; i++)for(int j=0; j<=19; j++)a[i][j]=0;
  for(int i=0; i<n; i++)
  {
   for(int j=0; j<19; j++)
   {
    if(s[i]==ss[j])
    {
     if(j>0)for(int ii=0; ii<i; ii++){a[i][j]+=a[ii][j-1];a[i][j]%=10000;}else a[i][j]=1;
    }//else a[i][j]=a[i-1][j];
   }
  }
  for(int i=1; i<n; i++)a[i][18]=(a[i-1][18]+a[i][18])%10000;
  int i=n-1;
  cout <<"Case #" << z+1 << ": ";
  if(a[i][18]<1000)cout << 0;
  if(a[i][18]<100)cout << 0;
  if(a[i][18]<10)cout << 0;
  cout << a[i][18] << endl;
 }

}
