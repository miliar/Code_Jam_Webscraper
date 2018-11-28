// 1CA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

bool dfs(int start, vector<vector<int> > v)
{
	set<int> visited;
	
	queue<int> q;
	q.push(start);
	while(!q.empty()) {
		int index = q.front() - 1;
		q.pop();
		vector<int> l = v[index];
		for(int i = 0; i < l.size(); ++i) {
			if(visited.find(l[i]) != visited.end()) 
				return true;

			visited.insert(l[i]);
			q.push (l[i]);
		}

	}
	return false;

}

int _tmain(int argc, _TCHAR* argv[])
{
	fstream f("in.txt", ios::in);
	fstream fout("out.txt", ios::out);
	int T;
	f >> T;
	for(int tc = 1; tc <= T; ++tc) {
		int N;
		f >> N;
		vector<vector<int> > aList;
		for(int i = 0; i < N; ++i) {
			int M;
			f >> M;
			vector<int> v;
			for(int j = 0; j < M; ++j) {
				int x;
				f >> x;
				v.push_back(x);
			}
			aList.push_back(v);
		}
		


		bool found = false;
		for(int i = 1; i <= N; ++i) {
			if(dfs(i, aList)) {
				found = true;
				break;
			}
		}
		string s;
		if(found)
			s = "Yes";
		else
			s = "No";
		cout << "Case #" << tc << ": " << s << endl;
		fout << "Case #" << tc << ": " << s << endl;
	}

	return 0;
}

