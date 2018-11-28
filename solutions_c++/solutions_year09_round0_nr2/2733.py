#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream infile("B-small-attempt1.in.txt");
	ofstream outfile("out.txt");
	int t,h,w,i,j,k,num,zimu,min,tempx1,tempy1,tempx,tempy,x,y,p;
	int a[100][100];
	int b[100][100];
	bool mark[100][100];
	int c[100];
	int d[100];
	infile>>t;
	for(p=0;p<t;p++)
	{
		zimu='a';
		for(i=0;i<10;i++)
		{
			for(j=0;j<10;j++)
			{
				mark[i][j]=false;
			}
		}
		infile>>h>>w;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				infile>>a[i][j];
			}
		}
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(mark[i][j]==true)
					continue;
				
				else
				{
					
					tempx=i,tempy=j;
					num=0;
					while(1)
					{
						
						tempx1=tempx,tempy1=tempy;x=tempx;x=tempy;
					    min=1000;
						if((tempx-1)>=0 && a[tempx-1][tempy]<min)
						{
							min=a[tempx-1][tempy];
							x=tempx-1;
							y=tempy;
						}
						
						if((tempy-1)>=0 && a[tempx][tempy-1]<min)
						{
							min=a[tempx][tempy-1];
							x=tempx;
							y=tempy-1;
						}
						if((tempy+1)<w && a[tempx][tempy+1]<min)
						{
							min=a[tempx][tempy+1];
							x=tempx;
							y=tempy+1;
						}
						if((tempx+1)<h&& a[tempx+1][tempy]<min)
						{
							min=a[tempx+1][tempy];
							x=tempx+1;
							y=tempy;
						}
						
						
						
						
						tempx=x;
						tempy=y;
						if(mark[tempx][tempy]==true && a[tempx][tempy]<a[tempx1][tempy1])
						{
							c[num]=tempx1;
							d[num]=tempy1;
							for(k=0;k<=num;k++)
							{
								b[c[k]][d[k]]=b[tempx][tempy];
								mark[c[k]][d[k]]=true;
							}
							break;
						}
						if(min<a[tempx1][tempy1])
						{
							c[num]=tempx1;
							d[num]=tempy1;
							num++;													
						}
						
						if(min>=a[tempx1][tempy1])
						{	
							c[num]=tempx1;
							d[num]=tempy1;
							for(k=0;k<=num;k++)
							{
								b[c[k]][d[k]]=zimu;
								mark[c[k]][d[k]]=true;
							}
							zimu++;
							break;
							
						}
						
					}
				}
			}
		}
		outfile<<"Case #"<<(p+1)<<":"<<endl;;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
					outfile<<char(b[i][j])<<' ';
					
				
				
			}
			outfile<<endl;
			
		}
		
		
	}
	infile.close();
	outfile.close();
	return 0;
}