#include <cstdio>

int main() {

freopen("B.in","r",stdin);
freopen("B.out","w",stdout);

int t;
scanf("%d",&t);

char r[128][128];
char o[128][128];

for (int j=0;j<t;j++) {
	for (int ii=0;ii<128;ii++)
		for (int jj=0;jj<128;jj++) 
			{
			r[ii][jj]=0;
			o[ii][jj]=0;
			}
	
	int c;
	scanf("%d",&c);
	char ts[101];	
	for (int i=0;i<c;i++) {
		scanf("%s",ts);

		r[ts[0]][ts[1]]=ts[2];
		r[ts[1]][ts[0]]=ts[2];
		}
	scanf("%d",&c);
	for (int i=0;i<c;i++) {
		scanf("%s",ts);

		o[ts[0]][ts[1]]=1;
		o[ts[1]][ts[0]]=1;
		}
	scanf("%d",&c);
	scanf("%s",ts);

	int l=-1;
	char res[101];
	for (int i=0;i<c;i++) {
		char cur=ts[i];
		l++;
		res[l]=cur;
		if (l>0) {
			if (r[cur][res[l-1]]>0) 
				{
				l--;
				res[l]=r[cur][res[l]];
				}
			else {
				for (int k=0;k<=l;k++)
					if (o[cur][res[k]]) {
						l=-1;
						}
				}
			}

		}
	printf("Case #%d: [",j+1);
	for (int i=0;i<=l-1;i++) printf("%c, ",res[i]);
	if (l>=0) printf("%c",res[l]);
	printf("]\n");
	}

return 0;

}
