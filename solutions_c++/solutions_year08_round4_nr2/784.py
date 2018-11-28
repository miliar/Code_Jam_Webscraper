#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
#include<cstdio>
#include<cmath>
#include<fstream>
using namespace std;
#define pi 3.141592653589793

#define ABS(x) ((x)>0?(x):-(x))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define DIST(x,y) ABS((x)-(y))
int gcd(int x,int y){if(y==0)return x;else return(gcd(y,x%y));}

int main()
{
	ifstream fin ("input.in");
	ofstream fout ("output.out");
	int n,N,M,A,x1,x2,x3,y1,y2,y3;
	fin >> n;
	for (int i = 0; i < n; i ++)
	{
		fin >> N >> M >> A;
		x1=0;
		y1=0;
		//for (x1 = 0; x1 <= N; x1++)
		//{
		//	for (y1 = 0; y1 <= M; y1++)
		//	{
				for (x2 = 0; x2 <= N; x2++)
				{
					for (y2 = 0; y2 <= M; y2++)
					{
						for (x3 = 0; x3 <= N; x3++)
						{
							for (y3 = 0; y3 <= M; y3++)
							{
								if (A == ABS((x3 - x1)*(y2 - y1) - (x2 - x1)*(y3 - y1)))
									goto brk;
							}
						}
					}
				}
		//	}
		//}
brk:
		if (x2 > N)
			fout << "Case #" << i + 1 << ": IMPOSSIBLE"<<endl;
		else
			fout << "Case #" << i + 1 << ": " <<x1 <<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<< endl;
	}
	return 0;	
}
