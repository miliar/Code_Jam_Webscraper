#include<iostream>
#include<algorithm>
using namespace std;


int		a[200];
int		b[100];

int		n,m,tmp,ans;

int		calc(){
		memset(a,0,sizeof(a));
		int tmp = 0;
		int i,j;
		for(i=0; i<m; i++){
			a[b[i]] = 1;
			j = b[i]-1;
			while(j>0 && a[j]!=1){ j--; tmp++; };
			j = b[i]+1;
			while(j<=n && a[j]!=1){ j++; tmp++; };
		}
		return tmp;
}

int		main(){
		int i,t,T;
		//freopen("in.txt","r",stdin);
		//freopen("out.txt","w",stdout);
		for(cin>>T,t=1; t<=T; t++)
		{
			cin>>n>>m; ans = 100000000;
			memset(a,0,sizeof(a));
			memset(b,0,sizeof(b));
			for(i=0; i<m; i++) cin>>b[i];
			sort(b,b+m);
			do{
				tmp = calc();
				if (tmp<ans) ans = tmp;
			}
			while(next_permutation(b,b+m));
			printf("Case #%d: %d\n", t, ans);
		}


		return 0;
}



