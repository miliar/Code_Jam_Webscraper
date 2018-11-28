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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

char H[45];
int M[45];
int ret;
void g_swap(int s, int f)
{
	for (int i=f;i>s; i--)
	{
		swap(M[i],M[i-1]);
		ret++;
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int N;
	cin >> N;
	for (int I=0; I<N; I++)
	{
		cout << "Case #" << I+1 <<": ";
		int n;
		cin >> n;
		memset(M,0,sizeof M);
		for (int i=0; i<n; i++)
		{
			cin >> H;
			int tmp = 0;
			for (int j=0; j<n; j++)
				if (H[j] == '1')
					tmp = j;
			M[i] = tmp;
		}
		ret = 0;
		for (int i=0; i<n; i++)
		{
			int kol = 0;
			for (int j=0; j<=i; j++)
				if (M[j] > i)
				{
					kol++;
				}
			if (kol)
			for (int j=i; j<n; j++)
				if (M[j] <= i)
				{
					g_swap(i,j);
					break;
				}
		}
		cout << ret << endl;
	}
	return 0;
}