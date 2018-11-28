#include<fstream>
#include<string>
using namespace std;
main()
{
      ifstream fcin("c.in");
      ofstream fcout("c.out");
      string s="welcome to code jam";
	  char t[501];
      int f[500][19];
      int i,j,k,nn,n,ans;
      const int mmod=10000;
      fcin>>n;
      char c;
      fcin.get(c);
      for(nn=0;nn<n;nn++)
      {
          fcin.getline(t,500);
          for(i=0;i<strlen(t);i++)
          {
               for(j=0;j<s.length();j++)f[i][j]=0;
               if(t[i]==s[0])f[i][0]=1;
          }
          for(i=1;i<s.length();i++)
          {
              for(j=0;j<strlen(t);j++)
              {
                   if(f[j][i-1]!=0)
                   for(k=j+1;k<strlen(t);k++)
                   if(t[k]==s[i])f[k][i]=(f[k][i]+f[j][i-1])%mmod; 
              }     
          }
          ans=0;
          for(i=0;i<strlen(t);i++)ans=(ans+f[i][18])%mmod;
          fcout<<"Case #"<<nn+1<<": ";
          fcout.width(4);fcout.fill('0');
          fcout<<ans<<endl;
      }
}
