#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

vector<int> toVector(int v)
{
	vector<int> vv;
	while (v) { vv.push_back(v%10); v /= 10;}
	vv.push_back(0);
	reverse(vv.begin(), vv.end());
	return vv;
}
int toInt(vector<int> &vv)
{
	int v = 0;
	for (int i=0; i < vv.size(); ++i)
	{
		v = v * 10 + vv[i];
	}
	return v;
}
int getNext(vector<int> vv)
{
	next_permutation(vv.begin(), vv.end());
	return toInt(vv);
}

int getIntLine()
{
	int v;
	cin >> v;
	string dummy;
	getline(cin, dummy);
	return v;
}
int main()
{
	int T = getIntLine();
	for (int i=0; i < T; ++i)
	{
		int res = getNext(toVector(getIntLine()));
		printf("Case #%d: %d\n", i+1, res);
	}
}
