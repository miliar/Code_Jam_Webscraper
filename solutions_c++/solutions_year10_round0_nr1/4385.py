#include<iostream.h>
#include<fstream.h>
#include<conio.h>
int main()
{int t,i,n[10000],k[10000],result[10000],status,critical;
ofstream outf("output.txt");
    cout<<"Enter the the number of patterns";
    cin>>t;
    for(i=0;i<t;i++)
    {cin>>n[i];
    cin>>k[i];  }
   for(i=0;i<t;i++)
   {int snapper[n[i]];
   for(int temp=0;temp<n[i];temp++)
{    snapper[temp]=0;
}
    for ( int j=0;j<k[i];j++)
    {status=0;
        while (snapper[status]==1)
        {snapper[status]=0;
              status++;}
     //   if (snapper[status]==0)
        snapper[status]=1;
        
    }
   
   critical =0;
   for(int y=0;y<n[i];y++)
   {if (snapper[y]==0)
   critical =1;
   }
   if (critical==0)
   {result[i]=1;}
   else result[i]=0;
   
   
   
   
   
       }
for(int x=0;x<t;x++)
{if (result[x]==1)
   { outf<<"Case #"<<(x+1)<<": ON"<<endl;}
   
   
else if(result[x]==0)
                outf<<"Case #"<<(x+1)<<": OFF"<<endl;}
getch();
return 0;     
     }
