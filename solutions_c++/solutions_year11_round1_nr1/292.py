#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long



int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	forn(tt, t){
		long long n;
		int pd, pg;
		cin >>n >>pd >> pg;
		bool ok = 0;

		printf("Case #%d: ", tt + 1);

		if(n > 100)n = 100;

		if(n > 100){

		}else{
			fore(j, 1, n + 1){
				if(!ok)
					forn(k, j + 1){
						if(ok)continue;
						if (k * 100 == pd * j){
							if (k > 0 && pg == 0)
								continue;
							if (k < j && pg == 100)
								continue;
							ok = 1;
							puts("Possible");
						}
					}
			}
		}
		if (!ok)
			puts("Broken");
	}
	
	return 0;
}