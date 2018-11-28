#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

typedef long long ll;

const int maxn=550;
ll a[maxn][maxn];

void mass(int x,int y,int k,ll &mx,ll &my,ll &m){
	m=mx=my=0;
	if(k%2==0){
		int i0=x+k/2;
		int j0=y+k/2;
		for(int i=x;i<x+k;i++){
			for(int j=y;j<y+k;j++){
				int dx=i0-i-(i>=i0);
				int dy=j0-j-(j>=j0);
				mx+=a[i][j]*dx;
				my+=a[i][j]*dy;
				m+=a[i][j];
			}
		}
	}
	else{
		int i0=x+k/2;
		int j0=y+k/2;
		for(int i=x;i<x+k;i++){
			for(int j=y;j<y+k;j++){
				int dx=i0-i;
				int dy=j0-j;
				mx+=a[i][j]*dx;
				my+=a[i][j]*dy;
				m+=a[i][j];
			}
		}
	}
}


int check(ll mx,ll my, int x,int y,int k){
	if(k%2==0){
		mx-=(a[x][y]+a[x][y+k-1])*(k/2)+(-a[x+k-1][y]-a[x+k-1][y+k-1])*(k/2);
		my-=(a[x][y]-a[x][y+k-1])*(k/2)+(+a[x+k-1][y]-a[x+k-1][y+k-1])*(k/2);
	}
	else{
		mx-=(a[x][y]+a[x][y+k-1])*(k/2)+(-a[x+k-1][y]-a[x+k-1][y+k-1])*(k/2);
		my-=(a[x][y]-a[x][y+k-1])*(k/2)+(+a[x+k-1][y]-a[x+k-1][y+k-1])*(k/2);
	}
	return(mx==0 && my==0);
}

void move(int x,int y,int k,ll &mx,ll &my,ll &m){
	if(k%2==0){
		int i0=x+k/2;
		int j0=y+k/2;
		for(int i=x;i<x+k;i++){
			int j=y;
			int dx=i0-i-(i>=i0);
			int dy=j0-j-(j>=j0);
			mx-=a[i][j]*dx;
			my-=a[i][j]*dy;
			m-=a[i][j];
		}
	}
	else{
		int i0=x+k/2;
		int j0=y+k/2;
		for(int i=x;i<x+k;i++){
			int j=y;
			int dx=i0-i;
			int dy=j0-j;
			mx-=a[i][j]*dx;
			my-=a[i][j]*dy;
			m-=a[i][j];
		}
	}
	my+=m;
	if(k%2==0){
		int i0=x+k/2;
		int j0=y+1+k/2;
		for(int i=x;i<x+k;i++){
			int j=y+k;
			int dx=i0-i-(i>=i0);
			int dy=j0-j-(j>=j0);
			mx+=a[i][j]*dx;
			my+=a[i][j]*dy;
			m+=a[i][j];
		}
	}
	else{
		int i0=x+k/2;
		int j0=y+1+k/2;
		for(int i=x;i<x+k;i++){
			int j=y+k;
			int dx=i0-i;
			int dy=j0-j;
			mx+=a[i][j]*dx;
			my+=a[i][j]*dy;
			m+=a[i][j];
		}
	}
}

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	long long T;
	cin >> T;
	for(long long q=0;q<T;q++){
		cout << "Case #" << q+1 << ": ";
		int n,m;
		long long d;
		cin >> n >> m >> d;
		memset(a,0,sizeof a);
		string s;
		getline(cin,s);
		for(int i=0;i<n;i++){
			string s;
			getline(cin,s);
			for(int j=0;j<m;j++){
				a[i][j]=s[j]-'0'+d;
			}
		}

		int k=min(n,m);
		int f=0;
		for(;k>2 && !f;k--){
			for(int i=0;i<=n-k && !f;i++){
				ll mx,my,M;
				mass(i,0,k,mx,my,M);
				for(int j=0;j<=m-k && !f;j++){
					mass(i,j,k,mx,my,M);
					if(check(mx,my,i,j,k)){
						f=1;
						break;
					}
						//if(j!=m-k)move(i,j,k,mx,my,M);
				}
			}
			if(f){
				break;
			}
		}
		if(f){
			cout << k << endl;
		}
		else{
			cout << "IMPOSSIBLE\n";
		}
	}
	return 0;
}