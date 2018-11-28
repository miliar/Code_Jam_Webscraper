#include <fstream>
#include <iostream>
#include <string>
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
int child[50000][100];
string a[1000000];
int main()
{
    int ans,t,T,N,M,total,i,j,k,p;
    string str,temp;
    fin>>T;
    for (t=1;t<=T;t++)
    {
        memset(child,0,sizeof(child));
        ans=0;
        fin>>N>>M;
        child[0][0]=0;
        total=0;
        for (i=1;i<=N;i++)
        {
            fin>>str; str+='\0';
            k=1;
            p=0;
            while (str[k]!='\0')
            {
               temp="";
               while (str[k]!='/'&&str[k]!='\0') temp=temp+str[k++];
               for (j=1;j<=child[p][0];j++)
                  if (a[child[p][j]]==temp) break;
               if (j>child[p][0])
               {
                  total++;
                  a[total]=temp;
                  child[p][0]++;
                  child[p][child[p][0]]=total;
                  p=total;
               } else p=child[p][j];
               if (str[k]=='/') k++;
            }
        }
        for (i=1;i<=M;i++) 
        {
            fin>>str; str+='\0';
            k=1;
            p=0;
            while (str[k]!='\0')
            {
               temp="";
               while (str[k]!='/'&&str[k]!='\0') temp+=str[k++];
               for (j=1;j<=child[p][0];j++)
                  if (a[child[p][j]]==temp) break;
               if (j>child[p][0])
               {
                  ans++;
                  total++;
                  a[total]=temp;
                  child[p][0]++;
                  child[p][child[p][0]]=total;
                  p=total;
               } else p=child[p][j];
               if (str[k]=='/') k++;
            }
        }
        fout<<"Case #"<<t<<": ";
        fout<<ans<<endl;
    }
    return 0;
}
