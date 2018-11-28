#include <iostream>
#include <map>

using namespace std;

int a[513][513];
int n,m;
map<int,int> mm;
map<int,int>::iterator mi;
int ans[513][2];

int find(int x,int y) {
	int i,j,k,c=a[x][y];
	bool t;
	if (c==2) return 0;
	k=1;
	while (x+k-1<=m && y+k-1<=n) {
		t=true;
		if (k%2==0) c=a[x][y]^1; else c=a[x][y];
		for (i=0;i<k;i++) {
			if (a[x+i][y+k-1]!=c) {t=false; break;};
			c=c^1;
		}
		if (k%2==0) c=a[x][y]^1; else c=a[x][y];
		for (i=0;i<k;i++) {
			if (a[x+k-1][y+i]!=c) {t=false;break;};
			c=c^1;
		}
		if (!t) break;
		k++;
	}
	return k-1;
}

void clear(int x,int y,int k) {
	int i,j;
	for (i=x;i<x+k;i++) {
		for (j=y;j<y+k;j++) { 
			a[i][j]=2;
		}
	}
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Making Chess Boards.out","w",stdout);
	int test,i,j,k,p,mmax,x,y;
	char s[10];
	cin>>test;
	for (i=1;i<=test;i++) {
		mm.clear();
		cin>>m>>n;
		for (j=1;j<=m;j++) {
			cin>>s;
			for (k=0;k<n/4;k++) {
				if ('0'<=s[k] && s[k]<='9') p=s[k]-'0'; else p=s[k]-'A'+10;
				a[j][k*4+4]=(p&1);p=(p>>1);
				a[j][k*4+3]=(p&1);p=(p>>1);
				a[j][k*4+2]=(p&1);p=(p>>1);
				a[j][k*4+1]=(p&1);p=(p>>1);
			}
		}
		while (true) {
			mmax=0;
			for (j=1;j<=m;j++) {
				for (k=1;k<=n;k++) {
					p=find(j,k);
					if (p>mmax) {
						mmax=p;
						x=j;y=k;
					}
				}
			}
			if (mmax==0) break;
			mm[mmax]++;
			clear(x,y,mmax);
		}
		cout<<"Case #"<<i<<": "<<mm.size()<<endl;
		j=0;
		for (mi=mm.begin();mi!=mm.end();mi++) {
			++j;
			ans[j][0]=mi->first;ans[j][1]=mi->second;
		}
		for (j=mm.size();j>0;j--) cout<<ans[j][0]<<" "<<ans[j][1]<<endl;
	}
	return 0;
}