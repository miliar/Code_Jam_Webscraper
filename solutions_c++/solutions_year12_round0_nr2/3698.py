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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;

struct Triplet{
	int s1, s2, s3;
	bool isSurprising;
	int best;
	Triplet(){
		s1 = s2 = s3 = best = 0;
		isSurprising = false;
	}
	Triplet(int a, int b, int c){
		//cout << a << " " << b << " " << c << endl;
		s1 = a;
		s2 = b;
		s3 = c;
		best = max(s1, max(s2, s3));
		if(abs(s1 - s2) == 2 || abs(s1 - s3) == 2 || abs(s2 - s3) == 2)
			isSurprising = true;
		else
			isSurprising = false;
	}
};

int N, S, P;
int sol;
int scores[100];
bool visited[11][11][11];
vector<Triplet> allTriplets[31];

bool isVisited(int a, int b, int c){
	int arr[3] = {a, b, c};
	sort(arr, arr + 3);
	bool ret = visited[arr[0]][arr[1]][arr[2]];
	visited[arr[0]][arr[1]][arr[2]] = true;
	return ret;
}

vector<Triplet> getGooglerTriplets(int n){
	memset(visited, false, sizeof(visited));
	vector<Triplet> triplets;
	for(int i = 0; i <= 10; i++){
		for(int j = 0; j <= 10; j++){
			if(abs(i - j) > 2) continue;
			for(int k = 0; k <= 10; k++){
				if(abs(k - j) > 2 || abs(k - i) > 2) continue;
				if(i + j + k == n && !isVisited(i, j, k))
					triplets.push_back(Triplet(i, j, k));
			}
		}
	}
	return triplets;
}

void solve(int idx, int s, int w){
	if(idx == N && s == S){
		sol = max(sol, w);
		return;
	}
	if(idx >= N)
		return;
	if(s > S)
		return;
	for(int i = 0; i < (int)allTriplets[scores[idx]].size(); i++){
		int sCnt = 0, wCnt = 0;
		if(allTriplets[scores[idx]][i].best >= P)
			wCnt = 1;
		if(allTriplets[scores[idx]][i].isSurprising)
			sCnt = 1;
		solve(idx + 1, s + sCnt, w + wCnt);
	}
}
int main(){
	freopen("in.in", "r", stdin);
	for(int i = 0; i <= 30; i++){
		allTriplets[i] = getGooglerTriplets(i);
	}
	int T;
	cin >> T;
	for(int c = 1; c <= T; c++){
		cin >> N >> S >> P;
		for(int i = 0; i < N; i++){
			cin >> scores[i];
		}
		sol = 0;
		solve(0, 0, 0);
		cout << "Case #" << c << ": " << sol << endl;
	}
	return 0;
}

