#include <cstdio>
#include <string>
int l,d,n,b[5005][20];
char s[5005][20],q[100005];
int main(){
	scanf("%d%d%d",&l,&d,&n);
	for (int i=1;i<=d;i++) scanf("%s",s[i]);
	for (int k=1;k<=n;k++){
		for (int i=1;i<=d;i++) for (int j=0;j<l;j++) b[i][j]=0;
		scanf("%s",q);
		int ln=strlen(q);
		int t=0,cnt=0;
		while (t<ln){
			if (q[t]=='('){
				int y=t+1;
				while (q[y]!=')') y++;
				for (int lk=t+1;lk<y;lk++)
					for (int j=1;j<=d;j++)
						if (s[j][cnt]==q[lk]) b[j][cnt]=1;
				t=y;
			}
			else {
				for (int j=1;j<=d;j++)
					if (s[j][cnt]==q[t]) b[j][cnt]=1;
			}
			t++; cnt++;
		}
		int AC=0;
		for (int j=1;j<=d;j++){
			int kk=1;
			for (int u=0;u<l&&kk;u++)
				if (!b[j][u]) kk=0;
			if (kk) AC++;
		}
		printf("Case #%d: %d\n",k,AC);
	}
	scanf("\n");
	return 0;
}
