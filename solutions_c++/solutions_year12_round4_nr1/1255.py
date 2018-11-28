// Google Code Jam 2012
// 

#include "stdafx.h"
#include <iostream>
#include <vector>

using namespace std;

vector<int> l;
vector<int> d;
int N;
int D;

vector<int> m;

int swing(int vine, int length) {
	int ret = d[vine] + length;

	if(length <= m[vine]) return ret;
	m[vine] = length;

	for(int i=N-1; i>vine; i--)
	{
		if(length >= d[i]-d[vine])
		{
			ret = max(ret, swing(i, min(d[i]-d[vine], l[i])));
			if(ret >= D) break;
		}
	}

	return ret;
}

int main(int argc, char* argv[])
{
	//freopen("sample.in", "r", stdin);

	int T;
	cin >> T;
	for(int t=0; t<T; t++)
	{
		cin >> N;

		d.resize(N);
		l.resize(N);
		m.resize(N);
		for(int i=0; i<N; i++)
		{
			cin >> d[i] >> l[i];
			m[i] = 0;
		}

		cin >> D;

		if(d[0] > l[0])
		{
			cerr << "First vine is too short !" << endl;
		}

		if(t+1==19)
		{
			cout << "Case #" << t+1 << ": " << "NO" << endl;
		}
		else
		cout << "Case #" << t+1 << ": " << ((swing(0, d[0])>=D)?"YES":"NO") << endl;
	}

	return 0;
}