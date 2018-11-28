#include<fstream>
#include<iostream>
using namespace std;
int main()
{
    int n,t,i,x,j,m,l=0;
    long r,k,g[1000],g1[1000],y;
    ifstream fin("jammu31.in");
	ofstream fout("output.out");
	fin>>t;
	while(t--)
	{
         fin>>r>>k>>n;
         for(i=0;i<n;i++)
             fin>>g[i];
         y=0;
         for(i=0;i<r;i++)
         {
             x=0;
             for(j=0;j<n;j++)
             {
                 x+=g[j];
                 if(x>k)
                 {
                     x-=g[j];
                     break;
                 }
			 }
			 for(m=0;j<n;j++,m++)
				 g1[m]=g[j];
			 for(j=0;m<n;m++,j++)
				 g1[m]=g[j];
			 for(j=0;j<n;j++)
				g[j]=g1[j];
             y+=x;
         }
         fout<<"Case #"<<(++l)<<": "<<y<<"\n";
     }
     fin.close();
     fout.close();
     return 0;
}
