using namespace std;

//#include<iostream>
#include<conio.h>
#include<fstream>
#include<algorithm>

struct intranet
{
int a,b;
};
bool mysort(intranet aa,intranet bb)
{
                     if(aa.a<bb.a)
                     return true;
                     else return false;                     
                     }
int main()
{
          intranet wire[1000];
          int t,n,intersect;
          int i,j,k;
          ofstream out;
          ifstream in;
          out.open("newout.txt");
          in.open("newin.in");
          in>>t;
          for(i=1;i<=t;i++)
          {
                           j=0;
                           intersect=0;
                           in>>n;
                           while(j<n)
                           in>>wire[j].a>>wire[j++].b;
                           sort(wire,wire+n,mysort);
                           for(j=0;j<n-1;j++)
                           {
                                           for(k=j+1;k<n;k++)
                                           {
                                                             if(wire[k].b<wire[j].b)
                                                             intersect++;
                                           }
                                           }
                           out<<"Case #"<<i<<": "<<intersect<<endl;
                           }
                           out.close();
                           in.close();
          getch();
          return 0;
 }
