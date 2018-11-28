#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int n,ni,i,j,f[500][4];
string s;

int main()
{
    freopen("gcj3.in","r",stdin);
    freopen("gcj3.out","w",stdout);
    cin>>n;
    getline(cin,s);
    for (ni=1;ni<=n;ni++)
    {
        int ans=0;
        memset(f,0,sizeof(f));
        getline(cin,s);
        for (i=0;i<s.size();i++)
        {
            if (s[i]=='w') f[i][1]=1;
            if (s[i]=='e')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]=='w') f[i][1]=(f[i][1]+f[j][1])%10000;
                              if (s[j]=='m') f[i][2]=(f[i][2]+f[j][1])%10000;
                              if (s[j]=='d') f[i][3]=(f[i][3]+f[j][1])%10000;
                          }
            }
            if (s[i]=='l')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]=='e') f[i][1]=(f[i][1]+f[j][1])%10000;
                          }
            }
            if (s[i]=='c')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]=='l') f[i][1]=(f[i][1]+f[j][1])%10000;
                              if (s[j]==' ') f[i][2]=(f[i][2]+f[j][2])%10000;
                          }
            }
            if (s[i]=='o')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]=='c') f[i][1]=(f[i][1]+f[j][1])%10000;
                              if (s[j]=='t') f[i][2]=(f[i][2]+f[j][1])%10000;
                              if (s[j]=='c') f[i][3]=(f[i][3]+f[j][2])%10000;
                          }
            }
            if (s[i]=='m')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]=='o') f[i][1]=(f[i][1]+f[j][1])%10000;
                              if (s[j]=='a') f[i][2]=(f[i][2]+f[j][1])%10000;
                          }
                          ans=(ans+f[i][2])%10000;
            }
            if (s[i]==' ')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]=='e') f[i][1]=(f[i][1]+f[j][2])%10000;
                              if (s[j]=='o') f[i][2]=(f[i][2]+f[j][2])%10000;
                              if (s[j]=='e') f[i][3]=(f[i][3]+f[j][3])%10000;
                          }
            }
            if (s[i]=='t')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]==' ') f[i][1]=(f[i][1]+f[j][1])%10000;
                          }
            }
            if (s[i]=='d')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]=='o') f[i][1]=(f[i][1]+f[j][3])%10000;
                          }
            }
            if (s[i]=='j')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]==' ') f[i][1]=(f[i][1]+f[j][3])%10000;
                          }
            }
            if (s[i]=='a')
            {
                          for (j=0;j<i;j++)
                          {
                              if (s[j]=='j') f[i][1]=(f[i][1]+f[j][1])%10000;
                          }
            }
        }
        cout<<"Case #"<<ni<<": ";
        if (ans<1000) cout<<0;
        if (ans<100) cout<<0;
        if (ans<10) cout<<0;
        cout<<ans<<endl;
    }
    return 0;
}
