#include<iostream>
#include<limits.h>

using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{	
		int h,w;
		cin>>h>>w;
		int in[h+2][w+2],o[h+2][w+2];
		for(int j=0;j<=h+1;j++)
		{
			for(int k=0;k<=w+1;k++)
			{
				if(j==0 || k==0 || j>h || k>w)
				{
					in[j][k]=INT_MAX;
				}
				else
					cin>>in[j][k];
				o[j][k]=0;
			}
		}
		//cout<<"chirag"<<endl;
		int current=1;
		for(int j=1;j<=h;j++)
		{
			for(int k=1;k<=w;k++)
			{
//				if(o[j][k]!=0)
	//				continue;
					
				int min=in[j][k];
				int x=0;
				int y=0;
				if(in[j-1][k] < min)
				{
					x=-1;
					y=0;
					min=in[j-1][k];
				}
				if(in[j][k-1] < min)
				{
					x=0;
					y=-1;
					min=in[j][k-1];
				}
				if(in[j][k+1] < min)
				{
					x=0;
					y=1;
					min=in[j][k+1];
				}
				if(in[j+1][k] < min)
				{
					x=1;
					y=0;
					min=in[j+1][k];
				}
				
				if(x==0 && y==0 && o[j][k]==0)
				{
					o[j][k]=current;
					current++;
				}
				else
				{
					if(o[j][k]*o[j+x][k+y]==0)
					{
						int a=o[j][k]+o[j+x][k+y];
						if(a==0)
						{
							a=current;
							current++;
						}
						
						o[j][k]=a;
						o[j+x][k+y]=a;
					}
					else
					{
						int max=o[j][k];
						int min=o[j+x][k+y];
						if(o[j+x][k+y] < o[j][k])
						{
							o[j][k]=o[j+x][k+y];
						}
						else
						{
							max=o[j+x][y+k];
							min=o[j][k];
							o[j+x][k+y]=o[j][k];
						}
						for(int jj=1;jj<=h;jj++)
						{
							for(int kk=1;kk<=w;kk++)
							{
								if(o[jj][kk]==max)
									o[jj][kk]=min;
							}
						}
					}			
				}
			}
		}
		int counter=1;
		for(int j=1;j<=h;j++)
		{
			for(int k=1;k<=w;k++)
			{
				if(o[j][k]==counter)
					counter++;
				if(o[j][k]>counter)
				{
					int a=o[j][k];
					int b=counter;
					for(int j=1;j<=h;j++)
					{
						for(int k=1;k<=w;k++)
						{
							if(o[j][k]==a)
								o[j][k]=b;
							else if(o[j][k]==b)
								o[j][k]=a;
						}
					
					}
					counter++;
				}
			}
		}
		cout<<"Case #"<<i+1<<":"<<endl;
		for(int j=1;j<=h;j++)
		{
			for(int k=1;k<=w;k++)
			{
				cout<<(char)(o[j][k]+96)<<" ";
			}
			cout<<endl;
		}		
	}
	return 0;
}
