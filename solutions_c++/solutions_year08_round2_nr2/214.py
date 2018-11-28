#include<cstdio>
#include<vector>
using namespace std;

vector<vector<bool> > bmask(0);
vector<int> prime(0);

int main() {
	freopen("B-small.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
	int C;
	scanf("%d",&C);
	for(int i=0;i<C;++i) {
		bmask.clear();
		prime.clear();
		int A,B,P;
		scanf("%d%d%d",&A,&B,&P);
		for(int j=P;j<=B;++j) {
			bool pr=true;
			for(int k=2;k*k<=j;++k) if (!(j%k)) {
				pr=false;
				break;
			}
			if (pr) prime.push_back(j);
		}
		
		for(int j=A;j<=B;++j) {
			vector<bool> tmp(prime.size());
			bmask.push_back(tmp);
			for(int k=0;k<prime.size();++k)
				if (!(j%prime[k])) bmask[j-A][k]=true;
		}
		
		for(;;) {
			bool ex=false;
			for(int k=0;k<bmask.size();++k) {
				for(int l=0;l<bmask.size();++l) {
					//if (i==4) printf("%d %d %d %d\n",A+k,A+l,bmask[k],bmask[l]);
					if (k!=l) {
						bool eq=false;
						for(int d=0;d<prime.size();++d)
							if (bmask[k][d]&&bmask[l][d]) {
								eq=true;
								break;
							}
						if (eq) {
							for(int d=0;d<prime.size();++d)
								bmask[k][d]=bmask[k][d]||bmask[l][d];
							bmask.erase(bmask.begin()+l);
							ex=true;
							--l;
							//break;
						}
					}
				}
				//if (ex) break;
			}
			if (!ex) break;
		}
		printf("Case #%d: %d\n",(i+1),bmask.size());
	}
	return 0;
}