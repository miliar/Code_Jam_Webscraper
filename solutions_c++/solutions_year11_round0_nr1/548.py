#include<cstdio>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int main(){
	int T0; scanf("%d",&T0);
	for(int T=1;T<=T0;T++){
		int n; scanf("%d ",&n);
		pair<char,int> seq[100];
		rep(i,n) scanf("%c%d ",&seq[i].first,&seq[i].second);

		int t=0;
		int b=1,o=1;
		rep(i,n){
			char c=seq[i].first;
			int pos=seq[i].second;
			if(c=='B'){
				int dif=abs(pos-b)+1;
				t+=dif;
				b=pos;

				int nexto=o;
				for(int j=i+1;j<n;j++){
					if(seq[j].first=='O'){ nexto=seq[j].second; break; }
				}
				if     (o<nexto) o=min(o+dif,nexto);
				else if(o>nexto) o=max(o-dif,nexto);
			}
			else{
				int dif=abs(pos-o)+1;
				t+=dif;
				o=pos;

				int nextb=b;
				for(int j=i+1;j<n;j++){
					if(seq[j].first=='B'){ nextb=seq[j].second; break; }
				}
				if     (b<nextb) b=min(b+dif,nextb);
				else if(b>nextb) b=max(b-dif,nextb);
			}
		}

		printf("Case #%d: %d\n",T,t);
	}

	return 0;
}
