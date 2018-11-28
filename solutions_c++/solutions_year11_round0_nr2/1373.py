#include<stdio.h>

char p[100][4];
char q[100][3];
char s[101];
char s2[101];
int main()
{
	freopen("B-large.in", "r", stdin);

    freopen("sample.out", "w", stdout);

	int t,c,d,n;
	int i,j,k,m,mm;
	bool flag;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%d",&c);
		for(j=0;j<c;j++){
			scanf("%s",&p[j][0]);
		}
		scanf("%d",&d);
		for(j=0;j<d;j++){
			scanf("%s",&q[j][0]);
		}
		scanf("%d",&n);
		scanf("%s",s);

		k=0;
		for(j=0;j<n;j++){
			if(k==0){
				s2[k++]=s[j];
			}else{
				flag = false;
				for(m=0;m<c;m++){
					if(s2[k-1]==p[m][0]&&s[j]==p[m][1] || s2[k-1]==p[m][1]&&s[j]==p[m][0]){
						s2[k-1]=p[m][2];
						flag = true;
						break;
					}
				}
				if(flag==false){
					for(m=0;m<k;m++){
						for(mm=0;mm<d;mm++){
							if(s2[m]==q[mm][0]&&s[j]==q[mm][1] || s2[m]==q[mm][1]&&s[j]==q[mm][0]){
								k=0;
								flag = true;
								break;
							}
						}
						if(flag)break;
					}
				}
				if(flag==false)s2[k++]=s[j];
			}
		}
		printf("Case #%d: [",i+1);
		for(j=0;j<k-1;j++){
			printf("%c, ",s2[j]);
		}
		if(k>0)
			printf("%c",s2[k-1]);
		printf("]\n");
	}
}