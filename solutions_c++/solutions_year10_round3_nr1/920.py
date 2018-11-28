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
	int i,j,k,T,N,t;
	ifstream in("input.txt");
	ofstream out("output.txt");	
	in>>T;
	rep(t,T)
	{
		in>>N;
		int c=0;
		vector<int> a(N), b(N);
		rep(i,N)
			in>>a[i]>>b[i];
		rep(i,N)
		{
			rep(j,i)
			{
				if ((a[i]<a[j])&&(b[i]>b[j])||(a[i]>a[j])&&(b[i]<b[j]))
					c++;
			}
		}
		out<<"Case #"<<(t+1)<<": "<<c<<endl;
	}
	return 0;
}

