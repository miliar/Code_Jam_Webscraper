#include <cstdio>
#include <algorithm>
using namespace std;

pair<int,int> index[1010];
int r[1010],order[1010],ansx[1010],ansy[1010];
int T,n,w,l;

bool solve(int w,int l){
	int curx=0,cury=0;
	int lastr=index[n-1].first;
	for (int i=n-1;i>=0;--i){
		ansx[i]=curx;
		ansy[i]=cury;
		if (i!=0){
			cury+=index[i].first+index[i-1].first;
			if (cury>l){
				curx+=lastr+index[i-1].first;
				cury=0;
				lastr=index[i-1].first;
			}
		}
	}
	for (int i=0;i<n;++i){
		if (ansx[i]>w) return false;
		if (ansy[i]>l) return false;
	}
	for (int i=0;i<n;++i)
		for (int j=i+1;j<n;++j){
			int a=abs(ansx[i]-ansx[j]);
			int b=abs(ansy[i]-ansy[j]);
			int c=index[i].first+index[j].first;
			if ((long long)a*a+(long long)b*b<(long long)c*c) return false;
		}
	return true;
}

int main(){
	scanf("%d",&T);
	for (int cases=0;cases<T;++cases){
		scanf("%d%d%d",&n,&w,&l);
		for (int i=0;i<n;++i){
			scanf("%d",&r[i]);
			index[i]=make_pair(r[i],i);
		}
		sort(index,index+n);
		for (int i=0;i<n;++i) order[index[i].second]=i;
		printf("Case #%d:",cases+1);
		if (solve(w,l)){
			for (int i=0;i<n;++i) printf(" %d %d",ansx[order[i]],ansy[order[i]]);
		}
		else if (solve(l,w)){
			for (int i=0;i<n;++i) printf(" %d %d",ansy[order[i]],ansx[order[i]]);
		}
		printf("\n");
	}
	return 0;
}
