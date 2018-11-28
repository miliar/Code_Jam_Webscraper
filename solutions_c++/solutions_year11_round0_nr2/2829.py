#include <stdio.h>
#include <algorithm>

int top;
char c[40][4],d[40][3],spell[110],stack[110];

int main()
{
	int t,T=0,i,j,k,C,D,N;

	//freopen("B-small-attempt0.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		top=0;
		scanf("%d",&C); for(i=0;i<C;++i) scanf("%s",c[i]);
		scanf("%d",&D); for(i=0;i<D;++i) scanf("%s",d[i]);
		scanf("%d",&N); scanf("%s",spell);

		for(i=0;i<N;++i)
		{
			for(j=0;j<C;++j)
				if((c[j][0]==stack[top] && c[j][1]==spell[i])
				|| (c[j][1]==stack[top] && c[j][0]==spell[i]))
				{
					stack[top]=c[j][2];
					break;
				}
			if(j==C)
			{
				for(j=0;j<D;++j)
				{
					for(k=1;k<=top;++k)
						if((d[j][0]==stack[k] && d[j][1]==spell[i])
						|| (d[j][1]==stack[k] && d[j][0]==spell[i]))
							break;
					if(k<=top) {top=0;break;}
				}
				if(j==D) stack[++top]=spell[i];
			}
		}

		printf("Case #%d: ",++T);		
		printf("[");
		for(i=1;i<top;++i) printf("%c, ",stack[i]);
		if(top) printf("%c",stack[top]);
		printf("]\n");
	}
	return 0;
}
