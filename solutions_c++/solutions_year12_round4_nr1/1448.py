#include <iostream>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <algorithm>
using namespace std;
int T, N, D;
int arr[105][2], p;
int flag[105];
bool solve(int idx, int d)
{
	int d2;
	if(arr[idx][0] + d >= D)
		return true;
	if(d < flag[idx])
		return false;
	flag[idx] = d;
	for(int i = idx + 1; i < N; i++)
	{
		if(arr[i][0] - arr[idx][0] > d)
			break;
		if(arr[i][1] < arr[i][0] - arr[idx][0])
			d2 = arr[i][1];
		else
			d2 = arr[i][0] - arr[idx][0];
		if(solve(i, d2))
			return true;
	}
	return false;
}
int cmp(const void *a,const void *b)
{
	return *((int*)a)-*((int*)b);
}    
int main()
{
	freopen("E:\\1\\A-small-attempt7.in", "r", stdin);
	freopen("E:\\1\\A-small-attempt7.out", "w", stdout);
	cin >> T;
	for(int Tidx = 1; Tidx <= T; Tidx++)
	{
		memset(flag, -1, sizeof(flag));
		cin >> N;
		for(int i = 0; i < N; i++)
			cin >> arr[i][0] >> arr[i][1];
		qsort(arr, N, sizeof(int) * 2, cmp);
		/*for(int i = 0; i < N; i++)
			cout << arr[i][0] <<  " " << arr[i][1] << endl;*/
		cin >> D;
		cout << "Case #" << Tidx << ": ";
		if(solve(0, arr[0][0]))
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}