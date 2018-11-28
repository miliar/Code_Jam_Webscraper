#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("B-small-attempt0.in");
ofstream fout("p2.out");
//#define fout cout
int n, m;
int a;
void init()
{
	fin>>n>>m>>a;
}
void calc()
{
	for (int x1=0;x1<=n;x1++)
		for (int x2=0;x2<=n-x1;x2++)
			for (int y2=0;y2<=m;y2++)
			{
				int rest = a-x2*y2-x1*y2;
				int y1;
				if (x2 ==0) 
				{
					if (rest==0) y1=0;
					else continue;
				}
				else if (rest%x2==0) y1=rest/x2;
				else continue;
					if (y1+y2<=m)
					{
						fout<<"0 0 "<<x1<<" "<<y1+y2<<" "<<x1+x2<<" "<<y1<<endl;
						return;
					}
			}
	fout<<"IMPOSSIBLE\n";
}
int main()
{
	int t;
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		init();
		fout<<"Case #"<<i<<": ";
		calc();
	}
	
}