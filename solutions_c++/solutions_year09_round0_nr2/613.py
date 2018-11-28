#include<iostream>
using namespace std;

int map[100][100];
int draw[100][100];
int x,y,basin;

int mini(int a,int b)
{
	int n[4]={-1,-1,-1,-1};
	if(a > 0)
	{
		n[0]=map[a-1][b];
	}		
	if(b > 0)
	{
		n[1]=map[a][b-1];
	}
	if(b < y-1)
	{
		n[2]=map[a][b+1];
	}
	if(a < x-1)
	{
		n[3]=map[a+1][b];
	}
	
	int mm=map[a][b],d=-1;
	for(int i=0;i<4;i++)
	{
		if(n[i] != -1 && mm > n[i])
		{
			//cout<<"======"<<endl;
			//cout<<mm<<" "<<n[i]<<" "<<i<<endl;
			mm=n[i];
			d=i;
		}
	}
	return d;
}

int go(int a,int b)
{
	int d=mini(a,b);
	//cout<<a<<" "<<b<<" "<<d<<endl;
	if(d == -1)
	{
		if(draw[a][b] == 0)
		{
			draw[a][b] = basin+1;
			basin++;
		}
		return draw[a][b];
	}
	else
	{
		if(d == 0)
		{
			draw[a][b] = go(a-1,b);
			return draw[a][b];
		}
		else if(d == 1)
		{
			draw[a][b] = go(a,b-1);
			return draw[a][b];
		}
		else if(d == 2)
		{
			draw[a][b] = go(a,b+1);
			return draw[a][b];
		}
		else if(d == 3)
		{
			draw[a][b] = go(a+1,b);
			return draw[a][b];
		}
	}
}

int main()
{
	int cas;
	while(cin>>cas)
	{
		for(int ccas=0;ccas<cas;ccas++)
		{
			basin=0;
			cin>>x>>y;
			for(int i=0;i<x;i++)
				for(int j=0;j<y;j++)
					cin>>map[i][j];
			for(int i=0;i<x;i++)
				for(int j=0;j<y;j++)
					if(draw[i][j] == 0)
					{
						draw[i][j] = go(i,j);
						
					}
			cout<<"Case #"<<ccas+1<<":"<<endl;
			for(int i=0;i<x;i++)
			{
				cout<<(char)((draw[i][0]-1)+'a');
				for(int j=1;j<y;j++)
					cout<<" "<<(char)((draw[i][j]-1)+'a');
				cout<<endl;
			}
			for(int i=0;i<x;i++)
				for(int j=0;j<y;j++)
					draw[i][j]=0;
		}
	}
	return 0;
}
