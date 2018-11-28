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

int t;

vector<int> tmp;

int gcd(int a,int b){
	if (a<b) swap(a,b);
	if (b==0) return a;
	tmp.push_back(a/b);
	return gcd(b,a%b);
}

map<vector<int>,int>X;

bool dfs(vector<int> cur){
	if (cur.size()==0) return true;
	if (X.find(cur)!=X.end()) return X[cur];
	int val=cur[cur.size()-1];
	bool ret=false;
	for (int j=1;j<=val;j++){
		cur.pop_back();
		if (j<val) cur.push_back(val-j);
		if (!dfs(cur)) ret=true;
		if (j<val) cur.pop_back();
		cur.push_back(val);
	}
	X.insert(make_pair(cur,ret));
	return ret;
}

bool check(int i,int j){
	tmp.clear();
	gcd(i,j);
	reverse(tmp.begin(),tmp.end());
	for (int k=0;k<tmp.size();k++)
		if (tmp[k]>1) tmp[k]=2;
	X.clear();
	if (dfs(tmp)) return true;
	return false;
}

int pos[1111111];

void init(){
	memset(pos,0xf,sizeof(pos));
	for (int i=1;i<=618920;i++){
		int t;
		scanf("%d%d",&t,&pos[i]);
	}
}

long long calc(int a,int b){
	if (a==0||b==0) return 0;
	long long ans=0;
	for(int i=1;i<=a;i++){
	//	cout << i <<endl;
		/*long long l=i,r=b;
		if (l>r) continue;
		while (l+1<r){
			long long mid=(l+r)/2;
			if (check(i,mid)) r=mid;
				else l=mid;
		}
		while (l<=b&&!check(i,l)) l++;*/
		int l=pos[i];
		if (l>b) continue;
		ans+=b-l+1;
	}
	for(int i=1;i<=b;i++){
		/*long long l=i,r=a;
		if (l>r) continue;
		while (l+1<r){
			long long mid=(l+r)/2;
			if (check(i,mid)) r=mid;
				else l=mid;
		}
		while (l<=a&&!check(i,l)) l++;*/
		int l=pos[i];
		if (l>a) continue;
		//cout << i <<" " << l <<" "<< a << endl;
		ans+=a-l+1;
	}
	//cout <<"#" << a <<" "<< b <<endl;
	//cout << ans <<endl;
	return ans;
}

void work(){
	int a1,a2,b1,b2;
	cin >> a1 >> a2 >> b1 >> b2;
	//cout << a1 <<" " << a2 <<" " << b1 <<" " << b2 <<endl;
	cout << calc(a2,b2)-calc(a2,b1-1)-calc(a1-1,b2)+calc(a1-1,b1-1) <<endl;
}

int main(){
	freopen("val.txt","r",stdin);
	init();
	fclose(stdin);
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin >> t;
	
	for (int i=1;i<=t;i++) {
		cout <<"Case #" << i << ": ";
		work();
	}
	//system("pause");
	return 0;
}
/*
3
5 5 8 8
11 11 2 2
1 6 1 6
*/
