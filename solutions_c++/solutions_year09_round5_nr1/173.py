#include<iostream>
#include<algorithm>
#include<set>
#define X first
#define Y second
using namespace std;
const int N=12;
const int M=5;
const int D=1000;
const int dx[4]={0,1,0,-1};
const int dy[4]={1,0,-1,0};
int T,n,m,p,q,h,t,fa[M],f[D];
long long d[D],ansh;
pair<int,int> c[M],b[M],g[M];
set<long long> hash;
char a[N][N];
long long gethash(){
	long long tmp=0;
	for (int i=0;i<p;i++)
		tmp+=(b[i].X<<(i*8))+(b[i].Y<<(i*8+4));
	return tmp;
}
long long getans(){
	long long tmp=0;
	for (int i=0;i<p;i++)
		tmp+=(g[i].X<<(i*8))+(g[i].Y<<(i*8+4));
	return tmp;
}
int in(int x,int y){
	return x>=0 && x<n && y>=0 && y<m && a[x][y]!='#';
}
int no(int x,int y){
	if (!in(x,y))
		return 0;
	for (int i=0;i<p;i++)
		if (b[i].X==x && b[i].Y==y)
			return 0;
	return 1;
}
int stable(){
	for (int i=0;i<p;i++)
		fa[i]=-1;
	int cnt=1;
	for (int i=0;i<p;i++)
		for (int j=i+1;j<p;j++)
			if (abs(b[i].X-b[j].X)+abs(b[i].Y-b[j].Y)==1){
				int k=i,o=j;
				while (fa[k]!=-1)k=fa[k];
				while (fa[o]!=-1)o=fa[o];
				if (k!=o){
					fa[k]=o;
					cnt++;
					if (cnt==p)
						break;
				}
			}
	return cnt==p;
}
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	cin>>T;
	for (int test=1;test<=T;test++){
		cin>>n>>m;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				cin>>a[i][j];
		p=0;q=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				if (a[i][j]=='x' || a[i][j]=='w')
					g[q++]=make_pair(i,j);
				if (a[i][j]=='o' || a[i][j]=='w')
					b[p++]=make_pair(i,j);
			}
		sort(b,b+p);
		sort(g,g+p);
		hash.clear();
		h=0;t=1;d[0]=gethash();f[0]=0;
		ansh=getans();
		hash.insert(d[0]);
		int ans=-1;
		if (d[0]==ansh)
			ans=0;
		while (h<t && ans==-1){
			for (int i=0;i<p;i++){
				b[i]=make_pair((d[h]>>(i*8))&15,(d[h]>>(i*8+4))&15);
				c[i]=b[i];
			}
			int flag=stable();
			for (int i=0;i<p;i++)
				for (int j=0;j<4;j++)
					if (in(b[i].X+dx[j],b[i].Y+dy[j]) && no(b[i].X-dx[j],b[i].Y-dy[j])){
						b[i].X+=dx[j];
						b[i].Y+=dy[j];
						sort(b,b+p);
						int ok=1;
						for (int k=1;k<p;k++)
							if (b[k-1]==b[k])
								ok=0;
						long long nowh=gethash();
						if (ok && hash.find(nowh)==hash.end() && (flag || stable())){
							d[t]=nowh;
							f[t]=f[h]+1;
							if (nowh==ansh)
								ans=f[t];
							t++;
							hash.insert(nowh);
						}
						for (int k=0;k<p;k++)
							b[k]=c[k];
					}
			h++;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
