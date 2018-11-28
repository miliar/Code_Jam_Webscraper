#include<cstdio>
const int N=110;
char a[N][5],b[N][5],out[N],ch,m;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,n,c,d,t,tt=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&c);
		for(i=0;i<c;i++)
			scanf("%s",a[i]);
		scanf("%d",&d);
		for(i=0;i<d;i++)
			scanf("%s",b[i]);
		scanf("%d",&n);
		m=0;
		while(n--){
			scanf(" %c",&ch);
			out[m++]=ch;
			if(m<2)continue;
			for(i=0;i<c;i++){
				if(out[m-1]==a[i][0]&&out[m-2]==a[i][1]){
					m--;
					out[m-1]=a[i][2];
				}
				else if(out[m-1]==a[i][1]&&out[m-2]==a[i][0]){
					m--;
					out[m-1]=a[i][2];
				}
			}
			if(m<2)continue;
			for(i=0;i<d;i++)
				if(out[m-1]==b[i][0]){
					for(j=0;j<m-1;j++)
						if(out[j]==b[i][1])break;
					if(j==m-1)continue;
					m=0;
				}
			for(i=0;i<d;i++)
				if(out[m-1]==b[i][1]){
					for(j=0;j<m-1;j++)
						if(out[j]==b[i][0])break;
					if(j==m-1)continue;
					m=0;
				}			
		}
		printf("Case #%d: ",tt++);
		putchar('[');
		if(m)putchar(out[0]);
		for(i=1;i<m;i++)
			printf(", %c",out[i]);
		putchar(']');
		putchar(10);
	}
	return 0;
}