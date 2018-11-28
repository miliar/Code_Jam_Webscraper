#include<string>
#include<map>
#include<iostream>
#define INF (1<<30)
using namespace std;

int a[1000][100];

int min(int a,int b){
	if(a<b) return a;
	return b;
}

int main(){
	int n,s,q,i,j,k;
	char ch[100];
	scanf("%d",&n);
	for(int nn=1;nn<=n;nn++){
		map<string, int> m;
		scanf("%d",&s);
		string str;
		gets(ch);
		for(i=0;i<s;i++){
			gets(ch);
			str=ch;
			m[str]=i;
		}
		scanf("%d",&q);
		if(q==0){
			printf("Case #%d: 0\n",nn);
			continue;
		}
		gets(ch);
		gets(ch);
		str=ch;
		int tt=m[str];
		for(i=0;i<s;i++){
			if(tt==i){
				a[0][i]=INF;
			}else{
				a[0][i]=0;
			}
		}
		for(j=1;j<q;j++){
			gets(ch);
			str=ch;
			int t=m[str];
			for(i=0;i<s;i++){//这层的每一个
				if(i==t){
					a[j][i]=INF;
					continue;
				}
				int mini=INF;
				for(k=0;k<s;k++){
					if(k==i){
						mini=min(a[j-1][k],mini);
					}else{
						mini=min(a[j-1][k]+1,mini);
					}
				}
				a[j][i]=mini;
			}
		}
		int ret=INF;
		for(i=0;i<s;i++){
			ret=min(a[q-1][i],ret);
		}
		printf("Case #%d: %d\n",nn,ret);
	}
}
