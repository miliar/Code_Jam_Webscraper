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

int main()
{
	int ie2;
	is>>ie2;
	for(int ie=1;ie<=ie2;ie++)
	{
		cout<<"Starts processing case "<<ie<<endl;
		os<<"Case #"<<ie<<": ";

		//begin of processing
		int N, K, B ,T;
		is>>N>>K>>B>>T;
		int pos[50];
		int v[50];
		for(int i=0;i<N;i++)
			is>>pos[i];
		for(int i=0;i<N;i++)
			is>>v[i];
		int blks=0;
		int swaps=0;
		int passed=0;
		for(int i=N-1;i>=0&&passed<K;i--)
		{
			if(v[i]*T<B-pos[i])
				blks++;
			else
			{
				swaps+=blks;
				passed++;
			}
		}
		if(passed!=K)
			os<<"IMPOSSIBLE\n";
		else
			os<<swaps<<endl;
		//end of processing

		cout<<"Case "<<ie<<" finished. \n";
	}
	cout<<"done\n";
	return 0;
}