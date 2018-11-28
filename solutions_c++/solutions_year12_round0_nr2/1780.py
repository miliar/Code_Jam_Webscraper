//
//  main.cpp
//  GCJ2012QB
//
//  Created by Seki Inoue on 12/04/14.
//  Copyright (c) 2012年 UNIPRO Inc. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
int main(int argc, const char * argv[])
{
	ifstream ifs( "input.txt" );
    int T = 0;
    ifs >> T;
	for (int i = 0; i < T; i++) {
		int N, S, p;
		ifs >> N >> S >> p;
		vector<int> t;
		
		int ans = 0;
		for (int j = 0; j < N; j++) {
			int tj;
			ifs >> tj;
			t.push_back(tj);
		}
		
		sort(t.begin(),t.end(),std::greater<int>());
		
		for (int j = 0; j < N; j++) {
			int total = t[j];
			if (total/3 >= p) {
				ans++;
			}else if (total && total/3 == p-1) {
				if (total%3 >= 1) {
					ans++;
				}else if (S) {
					S--;
					ans++;
				}
			}else if (total && total/3 == p-2) {
				if (total%3 == 2 && S) {
					S--;
					ans++;
				}
			}
		}
		
		cout << "Case #" << i+1 << ": " <<  ans << endl;
	}

    return 0;
}

