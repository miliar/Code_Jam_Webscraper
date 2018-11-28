#include<iostream>
using namespace std;

int main()
{
    char dic[30][30];
    int l,d,n,i,j,count=0,r=1,caseno=0;
    cin>>l>>d>>n;
    for(i=0;i<d;i++)
    cin>>dic[i];

n++;
    while(n--)
    {
              caseno++;
              char arr[11][30];    
              for(int a=0;a<11;a++)
              for(int b=0;b<30;b++)
              arr[a][b]='*';
              char ch;
              int i=-1,j=0,z,flag1=0,count=0,x,y;
              int flag=0,once;
              while((ch=getchar())!='\n')
              {
                    if(ch=='(')
                          {flag=1;i++;j=-1;continue;}
                    else if(ch==')')
                          {flag=0;continue;}
                    
                    if(flag==1) j++;
                    
                    else {i++;j=0;}                
                    arr[i][j]=ch;
                    }
             count=0;
              for(x=0;x<=d;x++)
              {
              for(i=0;i<l;i++)
              {
                 for(j=0;;j++)
                 {
                      if(arr[i][j]=='*')
                     {  flag1=1;  break;}
                            if(dic[x][i]==arr[i][j])
                            {flag1=2;
                                       break;
                                     }
                              }
              if(flag1==1) break;
              else if(flag1==2 && i+1==l) count++;
              }
              }
              if (caseno==1) continue;
              cout<<"Case #"<<caseno-1<<": "<<count<<endl;

    }
    return 0;
}
