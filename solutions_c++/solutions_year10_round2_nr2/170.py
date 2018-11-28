#include <cstdio>
#include <iostream>
#include <fstream>
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
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

long long C, N, K, B, T;
long long re;
long long X[1000];
long long V[1000];
int possib[1000];

int main()
{
    fstream fin("B-large.in",fstream::in);
    fstream fout("B-large.out",fstream::out);
    fin >> C;
	long long per = 0;
	string tmp;
    for(int j=1;j<=C;j++)
    {
		re = 0;
		rep(i,1000) possib[i] = 0;
		fin >> N >> K >> B >> T ;
		rep(i, N)
		{
			fin >> X[i];
		}
		rep(i, N)
		{
			fin >> V[i];
		}
		long long tre = 0;
		rep(i, N)
		{
			if ( (B-X[i]) <= V[i]*T ) possib[i] = 1;
			else possib[i] = 0;
			tre += possib[i];
		}
		if (tre<K) 
		{
			fout << "Case #" << j << ": " << "IMPOSSIBLE\n";
			continue;
		}
		tre = 0;
		for(int i=N-1;i>=0;i--)
		{
			if (tre>=K) break;
			if (possib[i])
			{
				for(int k=i+1;k<N;k++)
				{
					if (possib[k]==0) re++;
				}
				tre++;
			}
		}
		fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
	fin.clear();
    fout.close();
	fout.clear();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
