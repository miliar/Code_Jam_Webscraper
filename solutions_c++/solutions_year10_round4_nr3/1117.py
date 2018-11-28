#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;

int g[105][105];
int g1[105][105];

int cnt(int x,int y)
{
    cout<<x<<" "<<y<<endl;
 int count=0;
            for(int ii=0;ii<=x;++ii)
                    for(int jj=0;jj<=y;++jj)
                    count+=g[ii][jj]==1;
   return count;
}

main()
{
	ifstream fin;ofstream fout;
	fin.open("C:\\c.in");
	fout.open("C:\\c.out");
	
	int tests;
	
	fin>>tests;
	int x=0,y=0;
	
	for(int cas=1;cas<=tests;++cas)
	{
            int r;
            fin>>r;
            memset(g,0,sizeof(g));
            int count=0,ret=0;
            for(int j=0;j<r;++j)
            {
                    int x1,y1,x2,y2;
                    fin>>x1>>y1>>x2>>y2;
                    if(x2>x)x=x2;
                    if(y2>y)y=y2;
                    for(int k=x1;k<=x2;++k)
                            for(int l=y1;l<=y2;++l)
                            g[k][l]=1;
            }
            count=cnt(x,y);
            while(count>0)
            {
             ret++;
             count=0;
            memset(g1,0,sizeof(g1));             
             for(int i=1;i<=x;++i)
                     for(int  j   =1;j<=y;++j)
                     if(g[i][j])
                     {
                      if(g[i-1][j] ==0 and g[i][j-1]==0)
                       g1[i][j]=0;
                       else
                       {
                        g1[i][j]=1;count++;
                        }
                     }
                     else
                     {
                      if(g[i-1][j] ==1 and g[i][j-1]==1)
                      {
                       g1[i][j]=1;count++;
                       }
                       else
                       {
                        g1[i][j]=0;
                        }                         
                     }
                     
             for(int i=0;i<=x;++i)
             for(int j=0;j<=y;++j)
             g[i][j]=g1[i][j];
            }
            fout<<"Case #"<<cas<<": "<<ret<<endl;
 }
	
	fin.close();
	fout.close();
	cin>>tests;
}
