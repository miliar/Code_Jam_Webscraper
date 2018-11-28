#include<iostream>
#include<fstream>
#include<conio.h>

using namespace std;
int len(int x)
{
    int l=0;
    while(x>0)
    {
    x=x/10;
    l++;
    }
    return l;
    }
int change(int x,int u,int d)
{    
    int r,k,j,p,l,c,e;
    for(r=0;r<=u;r++)
    {
    e=1;
    if(len(x)!=d)
    {
                    for(c=0;c<d-len(x);c++)
                     e=10*e;
                    }
    p=1;
    l=x/10;
    k=x%10;
    for(j=0;j<len(l);j++)
      p=p*10;
    l=k*p*e+l;
    x=l;
    }
    return l;
    }
int pass(int x,int y)
{    
    int i,u,j,k=0,f;
    for(i=x;i<y;i++)
    {
          for(u=0;u<len(i)-1;u++)
          {   
               f=change(i,u,len(i));
               for(j=i+1;j<=y;j++)
               {
                                  if(f==j)
                                    {k++;
                                    }
                                  }      
          }
    }
    return k;
    }
int main()
{
    char l[1000];
    int ans[1000];
    int a[100][100];
    fstream fin,fout;
    int i=0,k,j=0,t,f=0,count=0,tot=0;
    int x,y;
    fin.open("C-small-attempt0.in",ios::in);
    fout.open("C-small.txt",ios::out);
    while(!fin.eof())
    {
                     fin.getline(l,1000);
                     if(count==0)
                     {
                                 count=1;
                                 for(i=0;l[i]!='\0';i++)
                                 {
                                     tot=tot*10+(l[i]-48);                   
                                 }
                     }
                     else
                     {
                        for(i=0;l[i]!='\0';i++)
                        {
                                            t=l[i]-48;
                                            if(t!=-16)
                                              k=k*10+t;
                                            else
                                            {
                                              x=k;
                                              k=0;
                                            }
                        }
                        if(l[i]=='\0')
                        {
                           y=k;
                           k=0;
                           ans[f++]=pass(x,y);
                        }
                     }
    }
    for(i=0;i<tot;i++)
    {
                    cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
                    fout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
                    }
    fin.close();
    fout.close();
    getch();
    return 0;
    }
