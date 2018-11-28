#include<stdio.h>
#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
#include<memory.h>
#include<map>
#include<queue>

using namespace std;


int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int t=0;
	cin >> t;
	for (int e=1;e<=t;e++){
		int n,a,s=0,o=0,m=111111111;
		cin >> n;
		for (int i=0;i<n;i++){
			cin >> a;
			s^=a;
			o+=a;
			if (a<m)m=a;
		}
		cout << "Case #" << e << ": ";
		if (s)puts("NO");else cout << o-m << endl;
	}
	return 0;
}


