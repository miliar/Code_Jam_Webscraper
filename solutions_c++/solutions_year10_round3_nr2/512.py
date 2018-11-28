// CodeJam2010-2.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <algorithm>

using namespace std;



int main(long argc, char* argv[])
{
	ifstream in(argv[1]);

	string line;
	
	getline(in, line);
	
	int counter = atoi(line.c_str());

	for(int iTest = 0; iTest < counter; ++iTest)
	{
		int min, max,c;
		getline(in, line);
		sscanf(line.c_str(), "%d %d %d", &min, &max, &c);

		int t = 0;
		while(true)
		{
			min *= c;
			if(min >= max) break;
			++t;
		}

		int ans = 0;
		while(true)
		{
			if(t == 0)break;
			t = t/2;
			++ans;
			if(t == 0)break;

		}





		printf("Case #%d: %d\n", iTest+1, ans);
	


	}
	return 0;
}


