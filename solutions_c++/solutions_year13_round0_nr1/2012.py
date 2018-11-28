#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
int i,j,k,xs=0,zs=0,ds=0,x1,x2,t,f=0,n,inde=0;
string x[4];
ifstream fi;
fi.open("in.txt");
ofstream fo;
fo.open("out.txt");
fi>>n;
while(n--){
fi>>x[0]>>x[1]>>x[2]>>x[3];
inde++;
x1=x2=f=0;
xs=zs=t=0;
for(i=0;i<4;i++)
{
         x1=x2=t=zs=xs=0;
         for(j=0;j<4;j++)
         if(x[i][j]=='X')
         xs++;
         else if(x[i][j]=='O')
         zs++;
         else if(x[i][j]=='T')
         t++;
         if(xs+t==4)
         {
                    f=1;
                    break;
         }
         else if(zs+t==4)
         {
              f=2;
              break;
         }
}//cout<<f<<" "<<xs<<" "<<zs<<"\n";
if(f==0)
for(i=0;i<4;i++)
{
          x1=x2=t=zs=xs=0;
         for(j=0;j<4;j++)
         if(x[j][i]=='X')
         xs++;
         else if(x[j][i]=='O')
         zs++;
         else if(x[j][i]=='T')
         t++;
         if(xs+t==4)
         {
                    f=1;
                    break;
         }
         else if(zs+t==4)
         {
              f=2;
              break;
         }
}
//cout<<f<<" "<<xs<<" "<<zs<<"hlk\n";
if(f==0)
{//cout<<"dsf";
         x1=x2=t=zs=xs=0;
        for(i=0;i<4;i++)
        {
                if(x[i][i]=='X')
                xs++;
                else if(x[i][i]=='O')
                zs++;
                else if(x[i][i]=='T')
                t++;
        }
        if(xs+t==4)
         {
                    f=1;
                    //break;
         }
         else if(zs+t==4)
         {
              f=2;
              //break;
         }
          x1=x2=t=zs=xs=0;//cout<<"hovoc";
        for(i=0;i<4;i++)
        {//cout<<"sx";
                if(x[i][3-i]=='X')
                xs++;
                else if(x[i][3-i]=='O')
                zs++;
                else if(x[i][3-i]=='T')
                t++;
        }//cout<<xs<<" "<<zs<<" "<<t;
        if(xs+t==4)
         {
                    f=1;
                    
         }
         else if(zs+t==4)
         {
              f=2;
         
         }
}//cout<<f<<" "<<xs<<" "<<zs<<"\n";
if(f==1)
fo<<"Case #"<<inde<<": X won\n";
else if(f==2)
fo<<"Case #"<<inde<<": O won\n";    
else
{
    t=0;
    for(i=0;i<4;i++)
    for(j=0;j<4;j++)  
    if(x[i][j]=='.')
     t++;
     if(t==0)
     fo<<"Case #"<<inde<<": Draw\n";
     else
     fo<<"Case #"<<inde<<": Game has not completed\n";
}
}
fi.close();
fo.close();
}
       
