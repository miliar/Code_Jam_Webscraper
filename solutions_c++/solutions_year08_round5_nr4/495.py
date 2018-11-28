#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int a[100][100];

int get(int i, int j) {
	if (i < 0 || j < 0)
		return 0;
	if (a[i][j]>=0)
		return a[i][j];
	if (a[i][j] == -2)
		return 0;
	return a[i][j] = (get(i-2,j-1)+get(i-1,j-2))%10007;	
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int h,w,r;
		cin>>h>>w>>r;
		for (int i = 0;i<h;++i)
			for(int j=0;j<w;++j)
				a[i][j]=-1;
		a[0][0]=1;
		for (int i=0;i<r;++i){
			int r,c;
			cin>>r>>c;
			a[r-1][c-1]=-2;
		}
		cout << "Case #" << test+1 << ": " << get(h-1,w-1) << endl;
	}

	return 0;
}

