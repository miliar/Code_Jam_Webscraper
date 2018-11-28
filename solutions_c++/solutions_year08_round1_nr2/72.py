#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

const int maxn=2010;

int a[maxn][maxn];
int T[maxn];
int C[maxn];
int n,m,Times;

void init(){
	memset(a,0,sizeof(a));
	int t,x,y;
	cin >> n >> m;
	for (int i=0;i<m;i++){
		cin >> t;
		for (int j=0;j<t;j++){
			cin >> x >> y;
			a[i][x-1]|=(1<<y);
		}
	}
	for (int i=0;i<n;i++) T[i]=1;
	Times=0;
}

bool satisfy(int k){
	for (int i=0;i<n;i++)
		if (a[k][i]&T[i]) return true;
	return false;
}

bool work(){
	Times++;
	for (int i=0;i<m;i++)
		if (!satisfy(i)){
	//		cout << i << endl;
			return false;
		}
	return true;
}

void change(){
	for (int i=0;i<m;i++)
		if (!satisfy(i))
			for (int j=0;j<n;j++)
				if (a[i][j]>=2) T[j]=2;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int Q,test=0,now,ans;
	cin >> Q;
	while (Q--){
		init();
		while (!work()){
			if (Times>=3000) break;
			change();
		}
		test++;
		cout << "Case #" << test << ":";
		if (work()){
			for (int i=0;i<n;i++) cout << " " << T[i]-1;
			cout << endl;
		}
		else cout << " IMPOSSIBLE" << endl;
	}
	return 0;
}