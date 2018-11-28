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

int a[111111],n;
int lo[111111],hi[111111];

bool check(int pos){
	for (int i=0;i<=10000;i++)
		lo[i]=hi[i]=a[i];
	for (int i=0;i<=10000;i++){
		if (lo[i]>0){
			int cur=lo[i];
			for (int j=i;j<i+pos;j++){
				if (hi[j]<cur) return false;
				hi[j]-=cur;
				lo[j]-=cur;
			}
			for (int j=i+pos;j<=10000;j++){
				cur=min(cur,hi[j]);
				lo[j]-=cur;
				if (cur==0) break;
			}
		}	
	}
	return true;
}

void work(){
	memset(a,0,sizeof(a));
	cin >> n;
	for (int i=0;i<n;i++){
		int x;
		cin >> x;
		a[x]++;
	}
	int Lo=1,Hi=n;
	while (Lo+1<Hi){
		int mid=(Lo+Hi)/2;
		if (check(mid)) Lo=mid;
		else Hi=mid;
	}
	if (check(Hi)) printf("%d\n",Hi);
	else printf("%d\n",Lo);
}

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ":" <<" ";
		work();
	}
//	system("pause");
	return 0;
}
/*
4
10 1 2 3 4 5 10 9 8 7 6
8 101 102 103 104 105 106 103 104
0
5 1 2 3 4 9
*/
