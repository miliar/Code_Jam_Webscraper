#include<iostream>
using namespace std;
int nos[19];
char text[501];
int main()
{
    int c,i,j,k,n,len,f;char ch;
    bool letters[128]={0};
    char wrds[]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
    for(i=0;i<19;i++)
    {
                     j=wrds[i];
                     letters[j]=1;
    }
    cin>>n;
    while((c=getchar())!='\n');
    for(i=0;i<n;i++)
    {
                    len=0;
                    for(j=0;j<501;j++)
                    text[j]='\0';
                    for(j=0;j<19;j++)
                    nos[j]=0;
                    if(i!=(n-1))
                    while((c=getchar())!='\n')
                    {
                                              if((c>='a' && c<='z') || c==' ')
                                              {
                                                         text[len]=c;
                                                         len++;
                                              }
                    }
                    else
                    while(cin>>ch)
                    {
                                              if((ch>='a' && ch<='z') || ch==' ')
                                              {
                                                         text[len]=ch;
                                                         len++;
                                              }
                    }
                    for(j=len-1;j>=0;j--)
                    {
                                         //c=text[j];cout<<letters[c]<<" ";
                                         //if(letters[c]==1)
                                         //{
                                                                f=1;
                                                                for(k=18;k>=0 && f==1;k--)
                                                                {
                                                                              if(text[j]==wrds[k])
                                                                              {
                                                                                       if(k==18)
                                                                                       nos[k]=(nos[k]+1)%10000;
                                                                                       else
                                                                                       nos[k]=(nos[k]+nos[k+1])%10000;
                                                                              }
                                                                              else
                                                                              {
                                                                                  if(nos[k]==0)
                                                                                  f=0;
                                                                              }
                                                                }
                                        // }
                    }
                    cout<<"Case #"<<i+1<<": ";
                    if(nos[0]<1000)
                    {
                                   cout<<"0";
                                   if(nos[0]<100)
                                   {
                                                 cout<<"0";
                                                 if(nos[0]<10)
                                                 cout<<"0";
                                   }
                    }
                    cout<<nos[0];
                    if(i!=(n-1))
                    cout<<endl;
    }
    return 0;
}
                    
                    
                                                         
                    
                    
                    
    
