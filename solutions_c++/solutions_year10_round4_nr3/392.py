#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

int n,a[111][111],b[111][111];

void work(){
	cin >> n;
	memset(a,0,sizeof(a));
	for (int i=0;i<n;i++){
		int x1,y1,x2,y2;
		cin >> x1 >> y1 >> x2 >> y2;--x1;--y1;--x2;--y2;
		if (x1>x2) swap(x1,x2);
		if (y1>y2) swap(y1,y2);
		for (int j=x1;j<=x2;j++)
			for (int k=y1;k<=y2;k++) a[j][k]=1;
	}
	int t=0;
	while (1){
		//for (int i=0;i<10;i++){
		//	for (int j=0;j<10;j++) cout << a[i][j] << " ";
		//	puts("");
		//}
		//puts("");
		bool f=false;
		for (int i=0;i<100;i++)
			for (int j=0;j<100;j++)
				if (a[i][j]==1) f=true;
		if (!f) break;
		memset(b,0,sizeof(b));
		for (int i=0;i<100;i++)
			for (int j=0;j<100;j++){
				int t=0;
				t+=a[i][j];
				if (i) t+=a[i-1][j];
				if (j) t+=a[i][j-1];
				if (t>=2) b[i][j]=1;
				}
		for (int i=0;i<100;i++)
			for (int j=0;j<100;j++)
				a[i][j]=b[i][j];
		t++;
	}
	cout << t <<endl;
}

int main(){
	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		work();
	}
	//system("pause");
	return 0;
}
