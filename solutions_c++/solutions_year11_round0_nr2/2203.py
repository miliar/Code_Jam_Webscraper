#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int t, c,d, n;
char com[40][3], del[30][3], kalimat[101];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	
	for (int tc=0;tc<t;tc++){
		scanf("%d ",&c);
		for (int i=0;i<c;i++)scanf("%s",com[i]);
		scanf("%d ",&d);
		for (int i=0;i<d;i++)scanf("%s",del[i]);
		scanf("%d ",&n);
		
		for (int i=0;i<n;i++){
//			printf("%d\n",i);
			scanf("%c",&kalimat[i]);
//			printf("%d %c\n",i,kalimat[i]);
			if (i>0)
			for (int k=0;k<c;k++){
				if (n>0)
				if ((kalimat[i]==com[k][0] && kalimat[i-1]==com[k][1]) ||
				(kalimat[i]==com[k][1] && kalimat[i-1]==com[k][0])){
					n--;
					i--;
					kalimat[i]=com[k][2];
				}
			}
			for (int j=0;j<i;j++){
				for (int k=0;k<d;k++){
					if (n>0)
					if ((kalimat[i]==del[k][0] && kalimat[j]==del[k][1]) ||
					(kalimat[i]==del[k][1] && kalimat[j]==del[k][0])){
						n=n-(i+1);
						i=-1;
//						n=n-(i-j+1);
//						i=j-1;
					}
				}
			}
		}
						
		printf("Case #%d: [",tc+1);
		for (int i=0;i<n-1;i++)printf("%c, ",kalimat[i]);
		if (n>0)printf("%c",kalimat[n-1]);
		printf("]\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
