#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <fstream>
#include <string>
//#include <windows.h>

using namespace std;

#define rep(i,n) for(int i = 0; i < n; i++)
#define rep1(i,n) for(int i = 1; i <= n; i++)
#define repk(i,k,n) for(int i = k; i < n; i++)
#define clr(a,x) memset(a,x,sizeof(a))
#define clearqueue(x) while(!x.empty()) x.pop();
#define clearvector(arr,n) rep(i,n)arr[i].clear();

int x[50];
int v[50];

bool canMakeIt(int dist, int speed, int time, int goal){
	int realDist = goal - dist;

	if(realDist <= time * speed)
		return true;
	else 
		return false;
}

int main()
{
	ifstream cin("B-large.in");
	ofstream cout("1.txt");
//	ios_base::sync_with_stdio(0);
//	long long begin = GetTickCount();
//	long long end = GetTickCount();
//	include <window.h>

	/*
	go through all the points mark the one who can make it true and the one who can not false
	and i might keep track of the number of ones who can not make it in the array also
	*/
	int c, n, k, b, t, ans, cnt, casenum = 1;
	bool can[50];
	int before[51];

	cin >> c;
	while(c--){
		cin >> n >> k >> b >> t;
		rep(i,n)
			cin >> x[i];
		
		rep(i,n)
			cin >> v[i];

		clr(before,0);
		for(int i = n - 1; i >= 0; i--){
			if(canMakeIt(x[i], v[i], t, b)){
				can[i] = true;
				before[i] = before[i+1];
			}
			else{
				can[i] = false;
				before[i] = before[i+1] + 1;
			}
		}

		ans = 0;
		cnt = 0;
		for(int i = n - 1; i >= 0; i--){
			if(can[i]){
				ans+=before[i];
				cnt++;
			}
			if(cnt == k) break;
		}


		cout << "Case #" << casenum++ << ": ";
		if(cnt == k)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}