#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

#define DEBUG 1

int N,K;
char map1[55][55];
char map2[55][55];
char map3[55][55];
void gravity();
bool take_K( char color);
bool horizontally(int ii,int jj,char color);
bool vertically(int ii,int jj,char color);
bool diagonally1(int ii,int jj,char color);
bool diagonally2(int ii,int jj,char color);




int main()
{
#if DEBUG 
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	/////code region////////////

	int T,Case = 1;

	cin>>T;
	while(T--)
	{
		cin>>N>>K;
		for(int i=0;i<N;i++)
	        scanf("%s",map1[i]);
	
		printf("Case #%d: ",Case++);

		for(int i=0;i<N;i++)     //rotate
		{
			for(int j=0;j<N;j++)
			{
				map2[j][N-1-i] = map1[i][j];
			}
		}
		for(int i=0;i<N;i++)
			map2[i][N] = '\0';

		gravity();   //ÏÂÂä

		//cout<<K<<endl;
		//for(int i=0;i<N;i++)
		//{
		//	for(int j=0;j<N;j++)
		//		cout<<map3[i][j];
		//	cout<<endl;
		//}

		bool blue = take_K('B');
		bool red  = take_K('R');

	
		if(blue && red)
			cout<<"Both"<<endl;
		else if(blue && !red)
			cout<<"Blue"<<endl;
		else if(!blue && red)
			cout<<"Red"<<endl;
		else
			cout<<"Neither"<<endl;


		//cout<<endl<<endl;
	}

	return 0;
}


void gravity()
{
	for(int k=0;k<N;k++)
	{
		int j=0;
		for(int i=N-1;i>=0;i--)
		{
			if(map2[i][k]!='.')
			{
				map3[N-1-j][k] = map2[i][k];
				j++;
			}
		}
		while(N-1-j>=0)
		{
			map3[N-1-j][k] = '.';
			j++;
		}
	}

	for(int i=0;i<N;i++)
		map3[i][N] = '\0';
}


bool take_K( char color)
{
	for(int j=0;j<N;j++)
	for(int i=0;i<N;i++)
	{
		if(horizontally(i,j,color) || vertically(i,j,color) || diagonally1(i,j,color) || diagonally2(i,j,color))
			return true;
	}

	return false;
}

bool horizontally(int ii,int jj,char color)
{
	for(int k=0;k<K;k++)
	{
		if(jj+k>=N || map3[ii][jj+k]!=color )
			return false;
	}

	return true;
}

bool vertically(int ii,int jj,char color)
{
	for(int k=0;k<K;k++)
	{
		if(ii+k>=N || map3[ii+k][jj]!=color)
			return false;
	}
	return true;
}

bool diagonally1(int ii,int jj,char color)
{
	for(int k=0;k<K;k++)
	{
		if(ii+k>=N || jj+k>=N || map3[ii+k][jj+k]!=color)
			return false;
	}

	return true;

}
bool diagonally2(int ii,int jj,char color)
{
	for(int k=0;k<K;k++)
	{
		if(ii-k<0 || jj+k>=N || map3[ii-k][jj+k]!=color)
			return false;
	}

	return true;
}
	