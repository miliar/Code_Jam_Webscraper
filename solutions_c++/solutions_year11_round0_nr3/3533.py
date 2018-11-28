/*
ID: tecnoyo1
PROG: brownie
LANG: C++
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <utility>
#include <map>
#include "math.h"
#include "string.h"
#include "stdio.h"

using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define mem(arr,val) memset(arr,val,sizeof(arr))
#define mp(x,y) make_pair(x,y)
#define fr(fl) freopen(fl,"r",stdin)
#define fw(fl) freopen(fl,"w",stdout)
#define getBit(code,i) (code &  (1 << i))
#define setBit(code,i) (code |  (1 << i))
#define resetBit(code,i) (code & ~(1 << i))

int tmp;
int sz;



int main()
{
	fr("in.txt");
	fw("gcjb2.txt");
	int N;
	cin >> N;
	rep(kase,N)
	{
		cin >> sz;
		int sm=0;
		int xor=0;
		int mn=INT_MAX;
		printf("Case #%d: ",kase+1);
		rep(i,sz)
		{
			cin >> tmp;
			sm += tmp;
			xor ^= tmp;
			mn = min(mn,tmp);
		}
		if(xor == 0)
			printf("%d\n",sm-mn);
		else
			printf("NO\n");
	}
	return 0;
}