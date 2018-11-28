#include <iostream>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath> 

#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x)) 


using namespace std;
int main()
{
	int N;
	ifstream inp("e:\\A-large.in");
	ofstream out("e:\\output.txt");
	inp>> N;
	cout<<N<<endl;
	int i,j;
	for (int nn = 1; nn <= N; nn++)
	{
		cout<< nn<<endl;
		long n, k;
		inp >> n >> k;
	//	cout<<k<<endl;
		int numOfOnes = 0;
		while ( k % 2 == 1)
		{
			k /= 2;
			numOfOnes ++;
		}
		if ( n <= numOfOnes )
			out<<"Case #"<<nn<<": ON"<<endl;
		else
			out<<"Case #"<<nn<<": OFF"<<endl;
	}// end of nn
	out.close();
}