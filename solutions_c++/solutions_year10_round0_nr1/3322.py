#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define rep(i,n) for(i=0; i<n; i++)

using namespace std;

int main()
{
	int i,j,k,T,N,K;
	ifstream in("input.txt");
	ofstream out("output.txt");	
	in>>T;
	rep(k,T)
	{
		in>>N>>K;
		if (K%(1<<N)==((1<<N)-1))
		{
			out<<"Case #"<<(k+1)<<": ON"<<endl;
		}
		else
		{
			out<<"Case #"<<(k+1)<<": OFF"<<endl;
		}
	}
	return 0;
}

