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

int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("1.txt");
//	ios_base::sync_with_stdio(0);
//	long long begin = GetTickCount();
//	long long end = GetTickCount();
//	include <window.h>
	bool arr1[101][101], arr2[101][101];
	int c, r, x1, y1, x2, y2, casenum = 1, mxRows, mxCols;
	cin >> c;
	while(c--){
		cin >> r;

		bool isArr1 = true, done = false;
		clr(arr1,0);
		clr(arr2,0);
		mxRows = mxCols = 0;
		rep(i,r){
			cin >> x1 >> y1 >> x2 >> y2;
			if(x2 > mxCols) mxCols = x2;
			if(y2 > mxRows) mxRows = y2;
			repk(j, y1, y2+1)
				repk(k, x1, x2+1)
					arr1[j][k] = 1;
		}
				//rep1(i,mxRows){
		//	rep1(j,mxCols){
		//		cout << arr1[i][j] << ' ';
		//	}
		//	cout << endl;
		//}
		//cout << mxRows << endl;
		//cout << mxCols << endl;

		
		int cnt = 0;
		while(!done){
			cnt++;
			done = true;
			if(isArr1){
				rep1(i,mxRows)
					rep1(j,mxCols){
						if(arr1[i-1][j] && arr1[i][j-1])
							arr2[i][j] = true;
						else if (!arr1[i-1][j] && !arr1[i][j-1])
							arr2[i][j] = false;
						else
							arr2[i][j] = arr1[i][j];
						if(arr2[i][j])
							done = false;
					}
			}
			else{
				rep1(i,mxRows)
					rep1(j,mxCols){
						if(arr2[i-1][j] && arr2[i][j-1])
							arr1[i][j] = true;
						else if (!arr2[i-1][j] && !arr2[i][j-1])
							arr1[i][j] = false;
						else
							arr1[i][j] = arr2[i][j];
						if(arr1[i][j])
							done = false;
					}
			}
			isArr1 = !isArr1;
		}
		cout << "Case #" << casenum++ << ": " << cnt << endl;
	}



	return 0;
}