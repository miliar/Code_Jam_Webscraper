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
		int n,x[111];
		vector<int> v[2];
		char c[111];
		cin >> n;
		for (int i=0;i<n;i++){
			cin >> c[i] >> x[i];
			if (c[i]=='O')v[0].push_back(x[i]);else v[1].push_back(x[i]);
		}
		int u0=0;
		int u1=0;
		int u=0;
		int a=1;
		int b=1;
		int ans=0;
		while (u<n){
			int t=0;
			ans++;
			if (u0<v[0].size()&&v[0][u0]>a)a++;else if (u0<v[0].size()&&v[0][u0]<a)a--;else if (c[u]=='O'){
				u0++;
				u++;
				t=1;
			}
			if (u1<v[1].size()&&v[1][u1]>b)b++;else if (u1<v[1].size()&&v[1][u1]<b)b--;else if (c[u]=='B'&&!t){
				u1++;
				u++;
			}
			
		}
		cout << "Case #" << e << ": ";
		cout << ans << endl;
	}
	return 0;
}


