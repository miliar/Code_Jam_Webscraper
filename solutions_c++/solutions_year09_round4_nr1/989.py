#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define REP(i, a, b) for(int i = a; i < b; i++)
#define GET(a) int a; cin >> a

int matrix[100][100];
int mat[100];
char buf[100];

int main()
{
	GET(N);
	REP(NN, 0, N)
	{
		GET(K);
		REP(i, 0, K)
		{
			cin >> buf;
			mat[i] = 0;
			REP(j, 0, K)
			{
				if(buf[j] == '1')
				{
					mat[i] = j;
				}
			}
		}
		bool sorted = true;
		int ret = 0;
		do
		{
			sorted = true;
			REP(i, 0, K)
			{
				if(mat[i] > i)
				{
					sorted = false;
					int j = 0;
					for(int jj = K-1; jj > i; jj--)
					{
						if(mat[jj] <= i)
						{
							j = jj;
						}
					}
					for(int k = j; k > i; k--)
					{
						ret++;
						int tmp = mat[k];
						mat[k] = mat[k-1];
						mat[k-1] = tmp;
					}
					break;
				}
			}
		}while (!sorted);
		cout << "Case #" << NN + 1<< ": " << ret << endl;
	}
	return 0;
}
