#include<iostream>
using namespace std;
#define M1 16
#define M2 5001
#define M3 501
char dict[M2][M1];
bool token[M1][26];            
int main()
{
    int c,n,i,l,d,cnt,j,k,f;
    cin>>l>>d>>n;
    while((c=getchar())!='\n');
    for(i=0;i<d;i++)
    {
                    for(j=0;j<l;)
                    {
                                 c=getchar();
                                 if(c>='a' && c<='z')
                                 {
                                           dict[i][j]=c;
                                           j++;
                                 }
                    }
                    dict[i][j]='\0';
    }
    for(i=0;i<n;i++)
    {
                    for(k=0;k<M1;k++)
                    for(j=0;j<26;j++)
                    token[k][j]=0;
                    j=0;
                    while(j<l)
                    {
                              c=getchar();
                              if(c=='(')
                              {
                                        while((c=getchar())!=')')
                                        {
                                                                 if(c>='a' && c<='z')
                                                                 {
                                                                           c=c-'a';
                                                                           token[j][c]=1;
                                                                 }
                                        }
                                        j++;
                              }
                              else
                              {
                                  if(c>='a' && c<='z')
                                  {
                                            c=c-'a';
                                            token[j][c]=1;
                                            j++;
                                  }
                              }
                    }
                    cnt=0;
                    for(j=0;j<d;j++)
                    {
                                    f=1;
                                    for(k=0;k<l && f==1;k++)
                                    {
                                                c=dict[j][k]-'a';
                                                if(token[k][c]==0)
                                                f=0;
                                    }
                                    if(f==1)
                                    cnt++;
                    }                                             
                    cout<<"Case #"<<i+1<<": "<<cnt;
                    if(i!=(n-1))
                    cout<<endl;
    }
    return 0;
}
    
