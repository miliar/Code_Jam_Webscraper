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

int n,a[1111];

void work(){
	cin >> n;
	for (int i=0;i<n;i++)
		cin >> a[i];
	sort(a,a+n);
	int sum=0;
	for (int i=0;i<n;i++) sum^=a[i];
	if (sum!=0) {puts("NO");return;}
	int ans=0;
	for (int i=1;i<n;i++) ans+=a[i];
	cout << ans <<endl;
}

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ": ";
		work();
	}
	//system("pause");
	return 0;
}
/*
2
5
1 2 3 4 5
3
3 5 6
*/
