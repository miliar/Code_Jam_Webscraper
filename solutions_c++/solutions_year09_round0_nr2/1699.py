#include<iostream>
#include<string>
using namespace std;
int a[128][128];
int h,w;
int count;
void check(char b[][128], int i, int j)
{
	int x = i, y = j;
	if(i>0 && a[i-1][j] < a[x][y])
	{
		x = i-1;
		y = j;
	}
	if(j>0 && a[i][j-1] < a[x][y])
	{
		x = i;
		y = j-1;
	}
	if(j<w-1 && a[i][j+1] < a[x][y])
	{
		x = i;
		y = j+1;
	}
	if(i<h-1 && a[i+1][j] < a[x][y])
	{
		x = i+1;
		y = j;
	}
	if(b[x][y])
		b[i][j] = b[x][y];
	else
		if(x!=i || y != j)
		{
			check(b, x , y);
			b[i][j] = b[x][y];
		}
		else
		{
			b[i][j] = 'a' + count;
			count++;
		}
}



	

int main()
{
	freopen("next.txt", "r", stdin);
	freopen("test.txt", "w", stdout);
	int test;
	cin>>test;
	for(int t = 0;t<test;t++)
	{
		
		cin>>h>>w;
		
		for(int i = 0; i < h; i++)
			for(int j = 0; j< w; j ++)
				cin>>a[i][j];
		char b[128][128] = {0};
		count = 0;
		for(int i = 0; i<h; i++)
			for(int j = 0; j<w; j++)
				if(!b[i][j])
					check(b, i, j);
		cout<<"Case #"<<t+1<<":"<<endl;
		for(int i = 0;i<h;i++)
		{
			for(int j = 0;j<w;j++)
				if(j<w-1)
					cout<<b[i][j]<<" ";
				else
					cout<<b[i][j]<<endl;
		}
	}
	return 0;
}