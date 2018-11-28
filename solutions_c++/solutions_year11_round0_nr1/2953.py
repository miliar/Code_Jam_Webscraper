#include <stdio.h>
#define abs(q) (((q)<0)?-(q):q)

char in[102][2];int pos[102],last[2],save[2],need;

int main()
{
	int t,T=0,i,j,n,ans;

	//?freopen("A-small-attempt0.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		scanf("%d",&n);
		ans=0;
		for(i=1;i<=n;++i) scanf("%s%d",in[i],&pos[i]), in[i][0]=in[i][0]=='O';
		last[0]=last[1]=1; save[0]=save[1]=0;
		for(i=1;i<=n;++i)
		{
			need=abs(pos[i]-last[in[i][0]])-save[in[i][0]];
			if(need<0) need=0;
			++need; // push

			ans+=need;
			save[ in[i][0]]=0;
			save[!in[i][0]]+=need;

			last[in[i][0]]=pos[i];
		}
		printf("Case #%d: %d\n",++T,ans);
	}
	return 0;
}
