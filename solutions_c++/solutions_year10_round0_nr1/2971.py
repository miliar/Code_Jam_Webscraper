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

int n,k;

void work(){
	cin >> n >> k;
	for (int i=0;i<n;i++){
		if (k%2==0) {puts("OFF");return ;}
		k/=2;
	}
	puts("ON");
	return;
}

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;cin >> t;
	int num=0;
	while (t--) {
		cout <<"Case #" << ++num<<": ";
		work();
	}
//	system("pause");
	return 0;
}
/*
4
1 0
1 1
4 0
4 47
*/
