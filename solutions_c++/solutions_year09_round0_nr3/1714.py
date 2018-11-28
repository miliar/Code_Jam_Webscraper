#include <iostream>
using namespace std;
string t="welcome to code jam";
int f[5001][30];
int main()
{
  freopen("C-small-attempt1.in","r",stdin);
  freopen("x.out","w",stdout);
  string s;
  int tn;
  cin>>tn;
  cin.ignore();
  int lt=t.length();
  for (int ts=1;ts<=tn;ts++)
  {
    memset(f,0,sizeof(f));
    getline(cin,s);
    int ls=s.length();
    f[0][0]=(s[0]==t[0]);
    for (int j=1;j<ls;j++)
      f[0][j]=(f[0][j-1]+(s[j]==t[0]))%10000;
    for (int i=1;i<lt;i++)
      for (int j=1;j<ls;j++)
      {
        if (t[i]==s[j])
              f[i][j]=f[i-1][j-1];
          f[i][j]=(f[i][j]+f[i][j-1])%10000;
      }
    /*
    for (int i=0;i<lt;i++)
    {
      for (int j=0;j<ls;j++)
      {
        printf("%d ",f[i][j]);
      }
      printf("\n");
    }
    */
    cout<<"Case #"<<ts<<": ";
    cout<<f[lt-1][ls-1]/1000<<f[lt-1][ls-1]/100%10<<f[lt-1][ls-1]/10%10<<f[lt-1][ls-1]%10<<endl;
  }
  
  return 0;
}
