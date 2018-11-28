#include <iostream>
using namespace std;
string s[6001];
string T;
bool f[30][200];
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("x.out","w",stdout);
  int L,D,N;
  cin>>L>>D>>N;
  for (int i=1;i<=D;i++)
  {
    cin>>s[i];

  }
  for (int i=1;i<=N;i++)
  {

    cin>>T;
  
    int l=T.length();
    int p=-1;
    memset(f,false,sizeof(f));
    bool out=true;
    for (int j=0;j<l;j++)
    {
      if (out)
      {
        if (T[j]=='(')
        {
          out=false;
          p++;
        }
        else
        {
          f[++p][T[j]-'a']=true;
        }
        continue;
      }
   //   printf("p:%d\n",p);
      if (T[j]==')')
      {
        out=true;
        continue;
      }
      
      f[p][T[j]-'a']=true;
    
    }
    int sum=0;
     for (int j=1;j<=D;j++)
     {
       bool flag=true;
       for (int k=0;k<L;k++)
       {
         if (!f[k][s[j][k]-'a'])
         {
           flag=false;
           break;
         }
       }
       sum+=flag;
     }
     cout<<"Case #"<<i<<": "<<sum<<endl;
  }
  return 0;
}
