#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,ti;
	int n;
	int A[101];
	char S[101][3];
	scanf("%d",&T);
	for(ti=1;ti<=T;ti++){
		int to=0,tb=0,po=1,pb=1;
		char s[3];
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%s",&S[i]);
			scanf("%d",&A[i]);
		}
		for(int i=0;i<n;i++){
			if(S[i][0]=='O'){
				to=max(to+abs(A[i]-po)+1,tb+1);
				po=A[i];
			}else{
				tb=max(tb+abs(A[i]-pb)+1,to+1);
				pb=A[i];
			}
		}
		printf("Case #%d: %d\n",ti,max(to,tb));
	}
	return 0;
}
