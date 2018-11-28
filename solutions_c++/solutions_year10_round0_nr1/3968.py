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

long long po[32];
void calcPow(){
	po[0] = 1;
	rep(i,30)
		po[i+1] = po[i] * 2;
}

int main()
{
	ifstream cin("A-large(3).in");
	ofstream cout("1.txt");
//	ios_base::sync_with_stdio(0);
//	long long begin = GetTickCount();
//	long long end = GetTickCount();
//	include <window.h>
	calcPow();
	long long n, k, t, casenum = 1;
	cin >> t;
	while(t--){
		cin >> n >> k;
		n = po[n];
		k++;
		cout << "Case #" << casenum++ << ": ";
		if(k % n == 0) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}

}