#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
char mat[100][100];
int num[100];
int main()
{
//	freopen("A-small-attempt1.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out1.txt", "w", stdout);
	int T;
	cin>>T;

	int Case;
	for(Case = 1; Case <= T; Case++)
	{
		int N;
		cin>>N;
		memset(num, 0, sizeof(num));
		int i, j;
		for(i = 0; i < N; i++)
			for(j = 0; j < N; j++)
			{
				cin>>mat[i][j];
				if(mat[i][j]=='1' && num[i] < j) num[i] = j;
			}
		//for(i = 0; i < N; i++)
		//	cout<<num[i]<<endl;
		int ans = 0;
		for(i = 0; i < N; i++)
		{
			if(num[i] > i)
			{
				for(j = i + 1; j < N; j++)
				{
					if(num[j] <= i) break;
				}
				for(; j > i; j --)
				{
					int t = num[j];
					num[j] = num[j-1];
					num[j-1] = t;
					ans++;
				}
			}
		}
		/*for(i = 0; i < N; i++)
		{
			int jj = 0;
			for(j = i; j < N; j++)
			{
				if(num[j] == i)
				{
					jj = j;
					break;
				}
			}
			for(j = jj - 1; j >= i; j--)
			{
				int t = num[j];
				num[j] = num[j+1];
				num[j+1] = t;
				ans++;
			}
		}*/
		printf("Case #%d: %d\n", Case, ans);
	}
	return 0;
}