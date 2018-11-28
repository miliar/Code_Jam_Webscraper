#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <list>
#include <vector>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

ifstream is("i.txt");
ofstream os("o.txt");

int less1(int i1,int i2)
{
	return i1<i2?i1:i2;

}

int more1(int i1,int i2)
{
	return -less1(-i1,-i2);
}
const int SIZE=102;
int main()
{
	int ie2;
	is>>ie2;
	for(int ie=1;ie<=ie2;ie++)
	{
		cout<<"Starts processing case "<<ie<<endl;
		os<<"Case #"<<ie<<": ";

		//begin of processing
		int r;
		is>>r;
		int mat[SIZE][SIZE]={{0}};
		while(r--)
		{
			int x1,x2,y1,y2;
			is>>x1>>y1>>x2>>y2;
			for(int i=x1;i<=x2;i++)
				for(int j=y1;j<=y2;j++)
				{
					mat[j][i]=1;
				}
		}
		int cnt=0;
		while(1)
		{
			/*
			for(int i=0;i<=5;i++)
			{
				for(int j=0;j<=5;j++)
					cout<<mat[i][j]<<" ";
				cout<<endl;
			}
			*/
			cout<<endl;
			bool found=false;
			for(int i=0;i<SIZE&&!found;i++)
			{
				for(int j=0;j<SIZE&&!found;j++)
					if(mat[i][j])
					{
						found=true;
					}
			}
			if(found==false)break;
			int toaddx[20000];
			int toaddy[20000];
			int toaddn=0;
			int todelx[20000];
			int todely[20000];
			int todeln=0;
			//int mat2[SIZE][SIZE]={{0}};
			for(int i=1;i<SIZE;i++)
				for(int j=1;j<SIZE;j++)
				{
					if(i>0&&j>0)
					{
						if(mat[i-1][j]==1&&mat[i][j-1]==1)
						{	//mat2[i][j]=1;
							toaddx[toaddn]=i;
							toaddy[toaddn++]=j;
						}
						if(mat[i-1][j]==0&&mat[i][j-1]==0)
						{
							//mat[i][j]=0;
							todelx[todeln]=i;
							todely[todeln++]=j;
						}
					}
					else
						mat[i][j]=0;
				}
				/*
			for(int i=0;i<SIZE;i++)
				for(int j=0;j<SIZE;j++)
					mat[i][j]=mat2[i][j];
					*/
			for(int i=0;i<toaddn;i++)
				mat[toaddx[i]][toaddy[i]]=1;
			for(int i=0;i<todeln;i++)
				mat[todelx[i]][todely[i]]=0;
			cnt++;
		}
		os<<cnt<<endl;
		//end of processing

		cout<<"Case "<<ie<<" finished. \n";
	}
	cout<<"done\n";
	return 0;
}