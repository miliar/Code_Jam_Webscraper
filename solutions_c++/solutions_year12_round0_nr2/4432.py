#include <iostream>
#include <stdio.h>
#include <fstream>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
using namespace std;



int main()
{
	ofstream fout("out.txt");
	ifstream fin("in.txt");

	int n, s, p, t, cnt;
	fin>>t;
	cnt = 0;
	while (cnt++<t){
		fin>>n>>s>>p;

		int ans = 0;
		for (int i = 0; i < n; i++){
			int sum;
			fin>>sum;
			
			int maxNum;
			if (sum == 0){
				maxNum = 0;
			} else {
				maxNum = (sum-1)/3 + 1;
			}

			if (maxNum >= p){
				ans++;
				continue;
			}

			if (s > 0 && sum >= 2 && sum % 3 != 1 && maxNum == p - 1){
				s--;
				ans++;
			}
		}

		fout<<"Case #"<<cnt<<": "<<ans<<endl;
	}


	fout.close();
	fin.close();

	return 0;
}