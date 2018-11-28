/*
 * A.cpp
 *
 *  Created on: May 22, 2010
 *      Author: Yasser
 */

#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

vector<string> v;

string getRow(int ind) {
	string str = ".";
	for (int i = 0; i < v[ind].size(); i++) {
		if (v[ind][i] == '.')
			continue;
		str += v[ind][i];
	}
	while (str.size() <= v.size())
		str = '.' + str;
	return str;
}

vector<string> v2;
int dx[] = { 0, 1, 1, 1 };
int dy[] = { 1, 0, 1, -1 };

bool getDir(int x, int y, int i, int &nx, int &ny) {
	nx = x + dx[i];
	ny = y + dy[i];
	return nx >= 0 && nx < v2.size() && ny >= 0 && ny < v2[0].size();
}

bool fun(char c, int k) {

	int n = v2.size();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < v2[i].size(); j++) {
			if (v2[i][j] == c) {
				for (int z = 0; z < 4; z++) {
					int x = i, y = j;
					for (int w = 0; w + 1 < k; w++) {
						if (getDir(x, y, z, x, y) && v2[x][y] == c)continue;
						goto NEXT;
					}
//					cout<<i << " " << j << " " << c<<endl;
					return true;
					NEXT: ;
				}
			}
		}
	}
	return false;
}

int main() {

	freopen("test.in", "rt", stdin);
	freopen("out.txt","wt",stdout);

	int TC, N, k;
	scanf("%d" ,&TC);
	for (int i = 0; i < TC; i++) {
		scanf("%d %d",&N,&k);

		v.clear();
		v.resize(N);

		char s[N];
		for (int i = 0; i < N; i++){
			scanf("%s",&s);
			v[i] = s;
		}

		v2.clear();
		for (int i = 0; i < N; i++) {
			string str = getRow(i);
			v2.push_back(str);
//			cout<<v2[i]<<endl;
		}

		printf("Case #%d: ",i+1);
		bool b1= fun('R',k) , b2 = fun('B',k);
		if(b1 && b2)
			printf("Both\n");
		else if(!b1 && !b2)
			printf("Neither\n");
		else if(b1)
			printf("Red\n");
		else if(b2)
			printf("Blue\n");
	}

	return 0;
}
