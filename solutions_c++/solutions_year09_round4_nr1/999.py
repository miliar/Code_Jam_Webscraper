#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

void solve(int caseNum)
{
	int N;
	fin >> N;
	int a[41] = {0};
	for (int i=0; i<N; i++)
	{
		int max = 0;
		string str;
		fin >> str;
		for (int j=0; j<N; j++) 
		{
			if (str[j] == '1')
				max = j;
		}
		a[i]=max;
	}
	int cnt=0;
	for (int i=0; i<N; i++)
	{
		for (int j=i; j<N; j++)
		{
			if (a[j]<=i)
			{
				if (j!=i)
				{
					cnt += j-i;
					for (int k=j-1; k>=i; k--)
						a[k+1] = a[k];
					break;
				} else {
					break;
				}
			} 
		}
	}
	fout << "Case #" << caseNum << ": ";
	fout << cnt << endl;
}

int main()
{
	int T;
	fin >> T;

	for (int i=1; i<=T; i++)
		solve(i);
	return 0;
}