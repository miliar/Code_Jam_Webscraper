/**
 * Codejam template
 * - daftmutt
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <new>
#include <memory>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define FOR2(i, m, n) for((i)=(int) (m);(i)<(int) (n); (i)++
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

using namespace std;

int TC;

vector<string> dirs;
vector<string> createDirs;
int i, j;
int N, M;

int checkDir(string dir){
	int c = 0;
	if (find(dirs.begin(), dirs.end(), dir) == dirs.end()){
		++c;
		dirs.push_back(dir);
		size_t found;
		found=dir.find_last_of("/");
		string tmp = dir.substr(0, found);
		if (tmp != "") c += checkDir(tmp);
	}
	return c;
}

int main()
{
	
	cin >> TC;
	 
	for (int C = 1; C <=TC; C++)
	{
		dirs.clear();
		createDirs.clear();
		dirs.push_back("/");
		int count = 0;
		cin >> N >> M;
		
		FOR(i, N) {
			string tmp;
			cin >> tmp;
			dirs.push_back(tmp);
		}
		FOR(i, M) {
			string tmp;
			cin >> tmp;
			createDirs.push_back(tmp);
		}
		
		foreach(createDirs, it) {
			string tmp = *it;
			count += checkDir(tmp);
		}
		
		cout << "Case #" << C << ": " << count << "\n";
	}
}
