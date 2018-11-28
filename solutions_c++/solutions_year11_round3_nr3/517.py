// codejam9.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for(int t = 0; t < T; t++){
		long long L, H, ans;
		long long f[10000];
		int N;
		in >> N >> L >> H;
		for(int n = 0; n < N; n++)
			in >> f[n];
		for(ans = L; ans <= H; ans++){
			bool fail = false;
			for(int n = 0 ; n < N; n++)
				if(!(ans % f[n] == 0 || f[n] % ans == 0)){
					fail = true;
					break;
				}
			if(!fail)break;
		}
		if(ans == H + 1)out << "Case #" << t + 1 << ": NO" << endl;
		else out << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}