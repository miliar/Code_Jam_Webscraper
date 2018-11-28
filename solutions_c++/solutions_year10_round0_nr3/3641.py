#include<iostream.h>
#include<fstream.h>
#include<conio.h>
int main()
{
    ofstream outf("output.txt");
    long int t,i,j,r[50],k[50],n[50],g[50][10],money[50],x,y,move[10],z=0,index,space;
     cout<<"Enter the the number of patterns";
cin>>t;
for(i=0;i<t;i++)
{cin>>r[i]>>k[i]>>n[i];
 for(j=0;j<n[i];j++)
  {cin>>g[i][j];
  }
}

//input taken
for(i=0;i<t;i++)
{
   money[i]=0;
    for(j=0;j<r[i];j++)
 { x=0;index=0;
  
   space=k[i];
   while((space>0)&&(space>=g[i][x])&&(x<n[i]))
   {                               
       money[i]=money[i]+g[i][x];
       space=space-g[i][x];
       index++;
       x++;            
    }
    z=0;
    for(y=index;y<n[i];y++)
    {move[z]=g[i][y];
    z++;
      }
      
    for(y=0;y<=index-1;y++)
    {move[z]=g[i][y];
    z++;
      }
    for(y=0;y<n[i];y++)
    {g[i][y]=move[y];
      }
     }
              outf<<"Case #"<<(i+1)<<": "<<money[i]<<endl;     
                }

getch();
return 0;
}
