#include<cstdio>

int main() {
	int T,S,n,i,v,_sum,_chk,_min;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		scanf("%d",&n);
		_sum=0;
		_chk=0;
		_min=0x7fffffff;
		for(i=0;i<n;i++) {
			scanf("%d",&v);
			_sum+=v;
			_chk^=v;
			if(v<_min)_min=v;
		}
		if(_chk)printf("Case #%d: NO\n",S);
		else printf("Case #%d: %d\n",S,_sum-_min);
	}
	return 0;
}
