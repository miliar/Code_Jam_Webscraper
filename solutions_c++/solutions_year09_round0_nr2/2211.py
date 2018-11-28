#include <iostream>
#include <vector>

#define SIZE 100


using namespace std;

int area[SIZE][SIZE];
char ans[SIZE][SIZE];
int max_rows,max_cols;
char current;



char flow(int x,int y)
{
	int min,minx=x,miny=y;
	if( ans[x][y] == '-' )
	{
	
		min=area[x][y];
		if( x-1 > -1)
			if(area[x-1][y] < min )
				{
					min=area[x-1][y];
					minx=x-1;
					miny=y;
				}

		if( y-1 > -1)
			if(area[x][y-1] < min )
				{
					min=area[x][y-1];
					miny=y-1;
					minx=x;
				}
		
				
		if( y+1 < max_cols)
			if(area[x][y+1] < min )
				{
					min=area[x][y+1];
					miny=y+1;
					minx=x;
				}

		if( x+1 < max_rows)
			if(area[x+1][y] < min )
				{
					min=area[x+1][y];
					minx=x+1;
					miny=y;
				}

		
		if(min == area[x][y])
		{
			/*pt temp;
			temp.x=x;
			temp.y=y;
			temp.character=current;
			current++;
			basins.push_back(temp);*/
			ans[x][y]=current;
			current++;
			return ans[x][y];
		}
		else
			ans[x][y]=flow(minx,miny);
		
	}
	return ans[x][y];
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int n,case_no=1;
	cin>>n;
	
	while(n!=0)
	{
		cin>>max_rows>>max_cols;
		cout<<"Case #"<<case_no<<":\n";
		case_no++;
		for(int i=0;i<max_rows;i++)
			for(int j=0;j<max_cols;j++)
				cin>>area[i][j];
		current='a';
		for(int i=0;i<max_rows;i++)
			for(int j=0;j<max_cols;j++)
				ans[i][j]='-';
		for(int i=0;i<max_rows;i++)
			for(int j=0;j<max_cols;j++)
				flow(i,j);
			
		
		for(int i=0;i<max_rows;i++)
		{
			for(int j=0;j<max_cols;j++)
				cout<<ans[i][j]<<" ";
			cout<<endl;
		}		
		
		n--;
	}
return 0;
}
