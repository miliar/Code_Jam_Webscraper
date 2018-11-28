#include<cstdio>
#include<vector>

using namespace std;

vector<pair<int,int> > coord(0);
int main() {
	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int N;
	scanf("%d",&N);
	for(int i=0;i<N;++i) {
		coord.clear();
		int n,A,B,C,D,x0,y0,M;
		scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&x0,&y0,&M);
		__int64 X=x0;
		__int64 Y=y0;
		coord.push_back(make_pair(X,Y));
		for(int j=0;j<n-1;++j) {
			X = A * X;
			X=(X+B) % M;
			Y = C * Y;
			Y=(Y+D)%M;
			coord.push_back(make_pair(X,Y));
		}
		
		int res=0;
		for(int j=0;j<n;++j)
			for(int k=j+1;k<n;++k)
				for(int l=k+1;l<n;++l)
					if (!((coord[j].first+coord[k].first+coord[l].first)%3)&&!((coord[j].second+coord[k].second+coord[l].second)%3))
						res++;
		printf("Case #%d: %d\n",(i+1),res);
	}
	return 0;
}