#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;


int area(int x1,int y1,int x2,int y2)
{
	return abs(x1*y2 - x2*y1);
}
int main()
{
	ifstream fin ("B-small-attempt0.in");
	ofstream fout ("test.out");

	int i,j,i1,j1;
	
	int n,cases;
	
	fin>>n;
	int t;
	int N,M,A;
	for(cases = 1; cases <= n; cases++)
	{
		int fi =0;
		fin>>N>>M>>A;
		for(i=0;!fi && i<=N;i++)
			for(j=0;!fi && j<=M;j++)
			for(i1=0;!fi && i1<=N;i1++)
			for(j1=0;!fi && j1<=M;j1++)
		{
			int ar = area(i,j,i1,j1);
			//cout<<i<<" "<<j<<" "<<i1<<" "<<j1<<" "<<ar<<endl;
			if( ar == A)
			{
				fout<<"Case #"<<cases<<": "<<"0 0 "<<i<<" "<<j<<" "<<i1<<" "<<j1 <<endl;
				fi =1;
			}

		}
		if(fi ==0)
			fout<<"Case #"<<cases<<": "<<"IMPOSSIBLE"<<endl;
		
		
	}

}