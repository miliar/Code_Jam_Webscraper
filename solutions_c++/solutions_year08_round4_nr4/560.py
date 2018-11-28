#include <stdio.h>
#include <string.h>

int cs,ct,k,min,l;
char s[1010],t[1010];
int a[10],mark[10];

void search(int h)
{
	int i,j;
	if (h==k) {
		t[l]=0;
		for (i=0;i<=l-k;i+=k)
		for (j=0;j<k;j++)
			t[i+a[j]]=s[i+j];
		int ans=0;
		for (j=0;j<l;j++)
			if (t[j]!=t[j+1]) ans++;
		if (ans<min) min=ans;
		return;
	}
	for (i=0;i<k;i++)
	if (!mark[i]) {
		a[h]=i;
		mark[i]=1;
		search(h+1);
		mark[i]=0;
	}
}

int main()
{
//	freopen("3.in","r",stdin);
	scanf("%d",&cs);
	for (ct=1;ct<=cs;ct++) {
		scanf("%d",&k);
		scanf("%s",s);
		l=strlen(s);
		memset(mark,0,sizeof(mark));
		min=0x3fffffff;
		search(0);
		printf("Case #%d: %d\n",ct,min);
	}	
	return 0;
}
