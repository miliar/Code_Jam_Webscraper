/*
 * speakingInTongues.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: ahmed
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
/*#include <hash_map>
using namespace __gnu_cxx;*/
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;
string s1 = "ejpmyslckdxvnribtahwfougzq";
string s2 = "ourlangeismpbtdhwyxfckjvqz";
int main()
{
	freopen("b.txt", "wt", stdout);
	int t;string line;
	getline(cin, line);
	sscanf(line.c_str(), "%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		getline(cin, line);
		string ans = "";
		for (int i = 0; i < (int)line.size(); ++i) {
			if(line[i] == ' ') {
				ans+=' ';
			}
			else {
				int idx = find(s1.begin(), s1.end(), line[i]) - s1.begin();
				ans+=s2[idx];
			}
		}
		cout<<"Case #"<<ii+1<<": "<<ans<<endl;
	}
	return 0;
}

/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
 */
