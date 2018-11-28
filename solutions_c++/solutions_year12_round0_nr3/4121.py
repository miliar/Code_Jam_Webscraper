#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <sstream>
#include <queue>

using namespace std;

#define ALL(v) (v.begin(),v.end())
#define sz(x) ((int)(x).size())
#define pb push_back
typedef vector<int> vi;

const int INF (0x3f3f3f3f);

int dx[] = {1,0,-1,0}, dy[] = {0,1,0,-1};


typedef long long LL;

ifstream fin ("C-small-attempt1(1).in");
ofstream fout ("C-small-attempt1(1).out");


int main (){
	int T , A , B;
	fin >> T;

	for (int i=0;i<T;i++){
		fin >> A >> B;
		set <int> st1;
		set < pair<int,int> > st2;
		int c=0;
		
		for (int k=A;k<=B;k++){
			stringstream ss;
			ss << k;
			string s = ss.str();
			for (int j=1;j<s.length();j++){
				string x = s.substr(j,s.size()-j+1);
				x += s.substr(0,j);

				int in = atoi(x.c_str());

				if (s[0]!='0' && in!=k && in >=A && in <=B){
					st2.insert(pair<int,int>(min(in,k),max(in,k)));
				}
			}
		}

		fout << "Case #" << i+1 << ": " << st2.size() << endl;
	}

	return 0;
}