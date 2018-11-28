// googlecode1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.in");
	ofstream out("out.txt");
	long T, N, K, t = 0;
	in >> T;
	while(t < T){
		++t;
		int ans = 0, num = 0;
		in >> N >> K;
		while(K){
			++num;
			if(num > N)
				break;
			ans = K % 2;
			if(num <= N && ans == 0)
				break;
			K = K / 2;
		}
		if(num < N)
			ans = 0;
		if(ans == 1)
			out << "Case #" << t << ": ON" << endl;
		else
			out << "Case #" << t << ": OFF" << endl;
	}
	return 0;
}

