
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

#define DEBUG 1

int map[513][513];
int M,N;
void Writemap(int i,char *str);
void Cut(int i,int j, int size);
bool Check(int i,int j,int size);

void printmap()
{
	int i;
		for(i=0;i<M;i++)
		{
			for(int j=0;j<N;j++)
				cout<<map[i][j];
			cout<<endl;
		}
}


int main()
{
#if DEBUG
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif

///////////////////////////////
	int T,Case = 1;

	cin>>T;
	while(T--)
	{
		cin>>M>>N;
		int i;
		for(i=0;i<513;i++)
		for(int j=0;j<513;j++)
			map[i][j] = 5;

		for(i=0;i<M;i++)
		{
			char str[500];
			scanf("%s",str);
			Writemap(i,str);
		}

		int K=0;
		int boardsize[513];
		for(i=0;i<=512;i++)
			boardsize[i] = 0;

		int size;
		if(M>N)
			size = N;
		else
			size = M;
		int S = size;
		while(size>=1)
		{
			bool flag = false;
			for(int i=0;i<M;i++)
			for(int j=0;j<N;j++)
			{
				if( Check(i,j,size) )
				{
				//	cout<<"ahfdlhfg="<<size<<endl;
					flag = true;
					boardsize[size]++;
					Cut(i,j,size);
				}
			}
			if(flag)
				K++;
			size--;
		}

		printf("Case #%d: %d\n",Case++,K);
		for(i=S;i>=0;i--)
		{
			if(boardsize[i]>0)
				printf("%d %d\n",i,boardsize[i]);
		}

	}

	return 0;
}

void Writemap(int i,char *str)
{
	int k = 0;
	for(int j=0;j<N/4;j++)
	{
		switch(str[j])
		{
		case '0': map[i][k] = 0; map[i][k+1] = 0; map[i][k+2] = 0; map[i][k+3] = 0; k=k+4; break;
		case '1': map[i][k] = 0; map[i][k+1] = 0; map[i][k+2] = 0; map[i][k+3] = 1; k=k+4; break;
		case '2': map[i][k] = 0; map[i][k+1] = 0; map[i][k+2] = 1; map[i][k+3] = 0; k=k+4; break;
		case '3': map[i][k] = 0; map[i][k+1] = 0; map[i][k+2] = 1; map[i][k+3] = 1; k=k+4; break;
		case '4': map[i][k] = 0; map[i][k+1] = 1; map[i][k+2] = 0; map[i][k+3] = 0; k=k+4; break;
		case '5': map[i][k] = 0; map[i][k+1] = 1; map[i][k+2] = 0; map[i][k+3] = 1; k=k+4; break;
		case '6': map[i][k] = 0; map[i][k+1] = 1; map[i][k+2] = 1; map[i][k+3] = 0; k=k+4; break;
		case '7': map[i][k] = 0; map[i][k+1] = 1; map[i][k+2] = 1; map[i][k+3] = 1; k=k+4; break;
		case '8': map[i][k] = 1; map[i][k+1] = 0; map[i][k+2] = 0; map[i][k+3] = 0; k=k+4; break;
		case '9': map[i][k] = 1; map[i][k+1] = 0; map[i][k+2] = 0; map[i][k+3] = 1; k=k+4; break;
		case 'A': map[i][k] = 1; map[i][k+1] = 0; map[i][k+2] = 1; map[i][k+3] = 0; k=k+4; break;
		case 'B': map[i][k] = 1; map[i][k+1] = 0; map[i][k+2] = 1; map[i][k+3] = 1; k=k+4; break;
		case 'C': map[i][k] = 1; map[i][k+1] = 1; map[i][k+2] = 0; map[i][k+3] = 0; k=k+4; break;
		case 'D': map[i][k] = 1; map[i][k+1] = 1; map[i][k+2] = 0; map[i][k+3] = 1; k=k+4; break;
		case 'E': map[i][k] = 1; map[i][k+1] = 1; map[i][k+2] = 1; map[i][k+3] = 0; k=k+4; break;
		case 'F': map[i][k] = 1; map[i][k+1] = 1; map[i][k+2] = 1; map[i][k+3] = 1; k=k+4; break;
		}
	}
}

void Cut(int i,int j, int size)
{
	for(int ii=0;ii<size;ii++)
	for(int jj=0;jj<size;jj++)
		map[i+ii][j+jj] = 5;
}

bool Check(int i,int j,int size)
{
	for(int ii=0;ii<size;ii++)
	{
		if(map[ii+i][j]>1)
			return false;
		if(ii>0)
		{
			if((map[ii+i][j]+map[ii+i-1][j])!=1)
				return false;
		}

		for(int jj=1;jj<size;jj++)
		{
			if(map[ii+i][jj+j]>1)
				return false;
			if((map[ii+i][jj+j]+map[ii+i][jj+j-1])!=1)
				return false;
		}
	}
	return true;
}


