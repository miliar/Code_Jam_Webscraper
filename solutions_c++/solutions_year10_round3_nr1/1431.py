// gl1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T, t = 0;
	in >> T;
	int a[1000];
	int b[1000];
	while(t < T){
		++t;
		int N;
		long ans = 0;
		in >> N;
		for(int i = 0; i < N; ++i)
			in >> a[i] >> b[i];
		for(int i = 0; i < N; ++i)
			for(int j = 0; j < i; ++j)
				{
					if(a[j] > a[i] && b[j] < b[i])
						++ans;
					if(a[j] < a[i] && b[j] > b[i])
						++ans;
				}
		out << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

