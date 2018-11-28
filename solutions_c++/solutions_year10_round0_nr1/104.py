/*
 * Author: rush
 * Created Time:  2010年05月08日 星期六 08时33分15秒
 * File Name: icpc/GCJ/A.cpp
 */
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, N, K;
	int f[35] = {0};
	for (int i = 1; i <= 30; ++i)
		f[i] = f[i - 1] * 2 + 1;
	//cout << f[29] << " " << f[30] << endl;
	cin >> T;
	for (int id = 1; id <= T; ++id)
	{
		cin >> N >> K;
		cout << "Case #" << id << ": ";
		if (K % (f[N] + 1) == f[N])
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
    return 0;
}
