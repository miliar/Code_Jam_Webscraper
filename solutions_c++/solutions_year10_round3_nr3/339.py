#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<sstream>
#include<stack>
#include<queue>


using namespace std;
int m,n;
string grid[600];
int check(int size,int x,int y)
{
	int i,j;
	if(x+size>m||y+size>n)
		return 0;
	for(i=x;i<x+size;i++)
	{
		for(j=y;j<y+size;j++)
		{	if(grid[i][j]=='2')return 0;
			if(i>x)
			{
				if(grid[i][j]=='0' && (grid[i-1][j]=='0'||grid[i-1][j]=='2'))
					return 0;
				if(grid[i][j]=='1' && (grid[i-1][j]=='1'||grid[i-1][j]=='2'))
					return 0;
			}
			if(j>y)
			{
				if(grid[i][j]=='0' && (grid[i][j-1]=='0'||grid[i][j-1]=='2'))
					return 0;
				if(grid[i][j]=='1' && (grid[i][j-1]=='1'||grid[i][j-1]=='2'))
					return 0;
			}
			if(i<x+size-1)
			{
				if(grid[i][j]=='0' && (grid[i+1][j]=='0'||grid[i+1][j]=='2'))
					return 0;
				if(grid[i][j]=='1' && (grid[i+1][j]=='1'||grid[i+1][j]=='2'))
					return 0;
			}
			if(j<y+size-1)
			{
				if(grid[i][j]=='0' && (grid[i][j+1]=='0'||grid[i][j+1]=='2'))
					return 0;
				if(grid[i][j]=='1' && (grid[i][j+1]=='1'||grid[i][j+1]=='2'))
					return 0;
			}
		}
	}
	return 1;
}
void remove(int size,int x,int y)
{
	int i,j;
	for(i=x;i<x+size;i++)
	{
		for(j=y;j<y+size;j++)
		{
			grid[i][j]='2';
		}
	}	

}
int main(void)
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);

	int t;
	cin>>t;
	int u=1;
	while(t-->0)
	{
		
		cin>>m>>n;

		int i,j;
		for(i=0;i<m;i++)
		{
			string temp;
			cin>>temp;
			grid[i]="";
			for(j=0;j<n/4;j++)
			{
				switch(temp[j]-48)
				{
					case 0:grid[i].append("0000");
						break;
							
					case 1:grid[i].append("0001");
						break;
													
					case 2:grid[i].append("0010");
						break;
													
					case 3:grid[i].append("0011");
						break;
													
					case 4:grid[i].append("0100");
						break;
													
					case 5:grid[i].append("0101");
						break;
													
					case 6:grid[i].append("0110");
						break;
													
					case 7:grid[i].append("0111");
						break;
													
					case 8:grid[i].append("1000");
						break;
													
					case 9:grid[i].append("1001");
						break;
													
					case 17:grid[i].append("1010");
						break;
					case 18:grid[i].append("1011");
						break;
					case 19:grid[i].append("1100");
						break;
					case 20:grid[i].append("1101");
						break;
					case 21:grid[i].append("1110");
						break;
					case 22:grid[i].append("1111");
						break;
				}
			}
		}
		int gridsize=m>n?n:m;
		vector<int> size,no;
		int fincount=0;
		while(gridsize>1)
		{
			int count=0;
			for(i=0;i<m;i++)
			{	
				for(j=0;j<n;j++)
				{
					if(check(gridsize,i,j))
					{
						count++;
						remove(gridsize,i,j);
																
					}							
				}
			}								
			if(count!=0)
			{
				fincount+=(gridsize*gridsize)*count;
				size.push_back(gridsize);
				no.push_back(count);
			}
			gridsize--;
		}
		if((m*n)-fincount>0)
		{
			size.push_back(1);
			no.push_back((m*n)-fincount);
		}
		cout<<"Case #"<<u<<": "<<size.size()<<endl;
		u++;
		for(i=0;i<size.size();i++)
		{
			cout<<size[i]<<" "<<no[i]<<endl;
		}
	}
}

