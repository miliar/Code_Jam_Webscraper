#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int N;

int ans = 1<<30;
string a[50];

int main()
{
	int C;

	cin >> C ;
	for (int cc = 1; cc <= C ;cc ++)
	{
		cin >> N;
		for (int i = 0;i<N;i++) cin >> a[i];
		int ans = 0;
		for (int i = 0;i<N-1;i++)
		{
			int j;
			for (j = i;;j++)
				if( a[j].substr(i+1).find("1") == string::npos) break;
			ans += j -i;
			for (int k = j-1;k >= i;k--) swap(a[k],a[k+1]);
		}
		printf("Case #%d: %d\n", cc, ans);

	}
	return 0;
}