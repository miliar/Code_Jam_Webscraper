#include <cstdio>
#include <cstring>

const int N=110;
char s[N],a[N][N],b[N][N];
int n,cnt[256];

int main(){
	gets(s);
	int T,i,j,k,cas,cc,su;
	sscanf(s,"%d",&T);
	for (cas=1;cas<=T;cas++){
		gets(s);
		sscanf(s,"%d%d",&n,&k);
		for (i=0;i<n;i++)
			gets(a[i]);
		memset(b,0,sizeof(b));
		for (i=0;i<n;i++)
			for (j=0;j<n;j++)
				b[j][n-i-1]=a[i][j];
		for (j=0;j<n;j++){
			int pos=n-1;
			for (i=n-1;i>=0;i--)
				if (b[i][j]!='.')
					b[pos--][j]=b[i][j];
			while (pos>=0) b[pos--][j]='.';
		}
		cnt['R']=cnt['B']=0;
		for (i=0;i<n;i++)
			for (cc=1,j=1;j<n;j++){
				if (b[i][j]==b[i][j-1])
					cc++;
				else cc=1;
				if (cc>=k) cnt[b[i][j]]=1;
			}
		for (j=0;j<n;j++)
			for (cc=1,i=1;i<n;i++){
				if (b[i][j]==b[i-1][j])
					cc++;
				else cc=1;
				if (cc>=k) cnt[b[i][j]]=1;
			}
		for (su=0;su<2*n;su++)
			for (cc=1,j=1;j<n;j++)
			if (su-j+1<n&&su-j>0){
				if (b[su-j][j]==b[su-(j-1)][j-1])
					cc++;
				else cc=1;
				if (cc>=k) cnt[b[su-j][j]]=1;
			}
		for (su=-n+1;su<n;su++)
			for (cc=1,j=1;j<n;j++)
			if (su+j-1>=0&&su+j<n){
				if (b[su+j][j]==b[su+(j-1)][j-1])
					cc++;
				else cc=1;
				if (cc>=k) cnt[b[su+j][j]]=1;
			}
		printf("Case #%d: ",cas);
		if (cnt['R']&&!cnt['B']) puts("Red");
		if (!cnt['R']&&cnt['B']) puts("Blue");
		if (!cnt['R']&&!cnt['B']) puts("Neither");
		if (cnt['R']&&cnt['B']) puts("Both");
	}
	return 0;
}
