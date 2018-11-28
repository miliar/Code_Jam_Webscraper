#include"stdafx.h"


#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>
//#include <windows.h>
using namespace std;
using std::vector;

typedef unsigned long long int64;
//typedef vector<int,int,int> v3i;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

int mat[200][200];
int sol[200][200];
int k,N,m,n;

void findmin(int i,int j)
{
	int pos=0;
	int curr=sol[i][j];
	int min=mat[i-1][j];
	if(mat[i][j-1]<min)
	{
		min=mat[i][j-1];
		pos=1;
	}
	if(mat[i][j+1]<min)
	{
		min=mat[i][j+1];
		pos=2;
	}
	if(mat[i+1][j]<min)
	{
		min=mat[i+1][j];
		pos=3;
	}


	if(min>=mat[i][j])
	{
		if(sol[i][j]==-1)
			sol[i][j]=k++;
	
		return;
	}

	else
		switch(pos)
		{
			case 0:
				if(sol[i-1][j]==-1 && sol[i][j]==-1)
				{
					sol[i-1][j]=sol[i][j]=k++;
				}
				else if(sol[i-1][j]!=-1 && sol[i][j]!=-1 && sol[i][j]!=sol[i-1][j])
				{
					int x=(sol[i-1][j]< sol[i][j])?(sol[i-1][j]):(sol[i][j]);
					int y=(sol[i-1][j]> sol[i][j])?(sol[i-1][j]):(sol[i][j]);
					for(int i=1;i<m+1;i++)
						for(int j=1;j<n+1;j++)
							if(sol[i][j]==y)
								sol[i][j]=x;
				}
				
				else if(sol[i-1][j]!=-1)
					sol[i][j]=sol[i-1][j];
				else if(sol[i][j]!=-1)
					sol[i-1][j]=sol[i][j];
				break;

			case 1:
				if(sol[i][j-1]==-1 && sol[i][j]==-1)
				{
					sol[i][j-1]=sol[i][j]=k++;
				}

				else if(sol[i][j-1]!=-1 && sol[i][j]!=-1 && sol[i][j]!=sol[i][j-1])
				{
					int x=(sol[i][j-1]< sol[i][j])?(sol[i][j-1]):(sol[i][j]);
					int y=(sol[i][j-1]> sol[i][j])?(sol[i][j-1]):(sol[i][j]);
					for(int i=1;i<m+1;i++)
						for(int j=1;j<n+1;j++)
							if(sol[i][j]==y)
								sol[i][j]=x;
				}

				else if(sol[i][j-1]!=-1)
					sol[i][j]=sol[i][j-1];
				else if(sol[i][j]!=-1)
					sol[i][j-1]=sol[i][j];
				break;
			case 2:
				if(sol[i][j+1]==-1 && sol[i][j]==-1)
				{
					sol[i][j+1]=sol[i][j]=k++;
				}
				
				else if(sol[i][j+1]!=-1 && sol[i][j]!=-1 && sol[i][j]!=sol[i][j+1])
				{
					int x=(sol[i][j+1]< sol[i][j])?(sol[i][j+1]):(sol[i][j]);
					int y=(sol[i][j+1]> sol[i][j])?(sol[i][j+1]):(sol[i][j]);
					for(int i=1;i<m+1;i++)
						for(int j=1;j<n+1;j++)
							if(sol[i][j]==y)
								sol[i][j]=x;
				}

				else if(sol[i][j+1]!=-1)
					sol[i][j]=sol[i][j+1];
				else if(sol[i][j]!=-1)
					sol[i][j+1]=sol[i][j];
				break;
			
			case 3:

				if(sol[i+1][j]==-1 && sol[i][j]==-1)
				{
					sol[i+1][j]=k;
					sol[i][j]=k++;
				}
				else if(sol[i+1][j]!=-1 && sol[i][j]!=-1 && sol[i][j]!=sol[i+1][j])
				{
					int x=(sol[i+1][j]< sol[i][j])?(sol[i+1][j]):(sol[i][j]);
					int y=(sol[i+1][j]> sol[i][j])?(sol[i+1][j]):(sol[i][j]);
					for(int i=1;i<m+1;i++)
						for(int j=1;j<n+1;j++)
							if(sol[i][j]==y)
								sol[i][j]=x;
				}

				
				else if(sol[i+1][j]!=-1)
					sol[i][j]=sol[i+1][j];
				else if(sol[i][j]!=-1)
					sol[i+1][j]=sol[i][j];
				break;	
		}

}

//void findmin(int i,int j)
//{
//	if(sol[i][j]!=-1)
//		return;
//	else
//		sol[i][j]=k++;
//	while(1)
//	{
//		int pos=0;
//		int curr=sol[i][j];
//		int min=mat[i-1][j];
//		if(mat[i][j-1]<min)
//		{
//			min=mat[i][j-1];
//			pos=1;
//		}
//
//		if(mat[i][j+1]<min)
//		{
//			min=mat[i][j+1];
//			pos=2;
//		}
//		if(mat[i+1][j]<min)
//		{
//			min=mat[i+1][j];
//			pos=3;
//		}
//
//
//		if(min>=mat[i][j])
//		{
//			break;
//		}
//
//		switch(pos)
//		{
//			case 0:
//				i--;
//				break;
//			case 1:
//				j--;
//				break;
//			case 2:
//				j++;
//				break;
//			case 3:
//				i++;
//				break;
//		}
//		if(sol[i][j]!=-1)
//			return;
//		else
//			sol[i][j]=
//		
//
//	}
//	return;
//}
int main()
{
	ifstream fin("ReadMe.txt");
	fin>>N;
	ofstream fout("out.txt");
	Rep(ti,N)
	{
		fin>>m>>n;
		k=0;
		Fill(sol,-1);
		Rep(i,m+2)
			Rep(j,n+2)
			{
				if(i==0 || i==m+1 || j==0 || j==n+1)
					mat[i][j]=200000;
				else
					fin>>mat[i][j];
			}	
		for(int i=1;i<m+1;i++)
			for(int j=1;j<n+1;j++)
				findmin(i,j);

		int curr=0;
		for(int i=1;i<m+1;i++)
			for(int j=1;j<n+1;j++)
			{
				if(sol[i][j]>curr+1)
				{
					int chk=sol[i][j];
					for(int i=1;i<m+1;i++)
						for(int j=1;j<n+1;j++)
							if(sol[i][j]==chk)
								sol[i][j]=curr+1;
					curr++;
				}
				else if(sol[i][j]==curr+1)
					curr++;
				
			}
		



				
		int count=0;
		fout<<"Case #"<<ti+1<<": "<<endl;
		cout<<"Case #"<<ti+1<<": "<<endl;
		for(int i=1;i<m+1;i++)
		{
			for(int j=1;j<n+1;j++)
			{
				cout<<(char)(sol[i][j]+'a')<<" ";
				fout<<(char)(sol[i][j]+'a')<<" ";
			}
			cout<<endl;
			fout<<endl;
		}

	}
	fin.close();
  	fout.close();
	getchar();
	return 0;
}