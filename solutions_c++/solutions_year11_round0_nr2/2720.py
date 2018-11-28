#include <cstdlib>
#include <iostream>
#include <stdio.h>

using namespace std;
char c[40][3],d[30][2];
char str[105];
bool ans[105];
int cn,dn,n,t;
int ansn=0;
char combine;

void init()
{
  ansn=0;
  cin>>cn; getchar();
  //cout<<cn<<endl;
  for(int i=1;i<=cn;i++)
  {cin>>c[i][0]>>c[i][1]>>c[i][2];getchar();
  if(c[i][0]>c[i][1]) {char t; t=c[i][0]; c[i][0]=c[i][1];c[i][1]=t;}
 // cout<<c[i][0]<<c[i][1]<<c[i][2]<<endl;
  }
  cin>>dn; getchar();
  //cout<<dn<<endl;
  for(int i=1;i<=dn;i++)
  {cin>>d[i][0]>>d[i][1];getchar();
  if(d[i][0]>d[i][1]) {char t; t=d[i][0]; d[i][0]=d[i][1];d[i][1]=t;}
  //cout<<d[i][0]<<d[i][1]<<endl;
  }
  cin>>n; getchar();
  for(int i=1;i<=n;i++)
  {
  cin>>str[i];
  //cout<<str[i];
  }
  getchar();   
  
  memset(ans,true,sizeof(ans));
     
}


void op(int i)
{
cout<<"Case #"<<i<<": [";
for(int j=1;j<=n;j++)
        if(ans[j]) 
            if(j!=n)
            cout<<str[j]<<", ";
            else cout<<str[j];
  
cout<<"]"<<endl;      
}

bool find_combine(char a,char b)
{
     if(a>b) 
     {
             char t;
             t=a;a=b;b=t;
     }
     for(int i=1;i<=cn;i++)
     if((a==c[i][0])&&(b==c[i][1]))
     {                             
          combine=c[i][2];
          return true;
     }
     return false;
     
}

bool find_oppose(char a,char b)
{    
     if(a>b) 
     {
             char t;
             t=a;a=b;b=t;
     }
     //cout<<"=="<<a<<" "<<b<<endl;
     for(int i=1;i<=dn;i++)
     if((a==d[i][0])&&(b==d[i][1]))
         return true;
     return false;
}

void _do()
{
for(int i=2;i<=n;i++)
{       char m;
        m=str[i];
        for(int j=i-1;j>=1;j--)
        { 
          
          if(ans[j])
                   { 
                               
                    if(!find_combine(m,str[j]))
                      break;
                    else
                     {//cout<<str[i]<<"+"<<str[j]<<endl;
                      str[i]=combine;
                      m=combine;
                      ans[j]=false;
                     }
                  
                   }
         
        }
        for(int j=i-1;j>=1;j--)
        {if(ans[j])
                  if(find_oppose(str[i],str[j]))
                  {   //cout<<str[i]<<" "<<str[j]<<endl;
                      for(int k=1;k<=i;k++)
                            ans[k]=false;       
                      break;
                  }
        }
}     
     
     
     
}

int main(int argc, char *argv[])
{
    
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
    init();
         _do();
    op(i);}
  //  system("PAUSE");
    return EXIT_SUCCESS;
}
