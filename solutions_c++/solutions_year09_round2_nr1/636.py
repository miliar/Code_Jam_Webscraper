#include<iostream>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;

string	s[1000],tt[1000];
double  a[1000];

int		m;
char	ch;

void	read(int rt){
		while(scanf("%c",&ch)==1 && ch!='(');
		scanf("%lf", &a[rt]); 
		scanf("%c",&ch);
		s[rt] = "";
		if (ch==' ') cin>>s[rt];

		if (s[rt]!=""){
			read(rt*2);
			read(rt*2+1);
			while(scanf("%c",&ch)==1 && ch!=')');
		} 
}

double	get(int i){
		if (s[i]=="") return a[i];
		for(int j=0; j<m; j++){
			if (tt[j]==s[i]) return get(i*2)*a[i];
		}
		return get(i*2+1)*a[i];
}

int		main(){
		int i, n, t, T;
		string S;
		memset(a,0,sizeof(a));
		//freopen("in.txt","r",stdin);
		//freopen("out.txt","w",stdout);
		for(cin>>T,t=1; t<=T; t++){
			if (t==20){
				int dd = 1;
			}
			scanf("%d",&n);
			read(1);
			scanf("%d",&n);
			printf("Case #%d:\n",t);
		
			for(; n; n--){
				cin>>S>>m;
				for(i=0; i<m; i++) cin>>tt[i];
				printf("%.7lf\n", get(1));
			}
		}


		return 0;
}





