#include<stdio.h>
main()
{
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int L,D,N,X,K,i,j,k,match[5000],l;
	char s[5000][16],m[26],c;
	scanf("%d %d %d",&L,&D,&N);
	for(i=0;i<D;i++)
	    scanf("%s",s[i]);
	for(X=1;X<=N;X++)
	{
		for(i=0;i<D;i++)
		    match[i]=1;
		for(i=0,K=D;i<L;i++)
		{
			for(c=getchar();c=='\n';c=getchar());
			if(c=='(')
			{
			    for(c=getchar(),l=0;c!=')';l++)
			    {
					m[l]=c;
					c=getchar();
				}
				for(j=0;j<D;j++)
				    if(match[j])
					{
						for(k=0;k<l;k++)
						{
						    if(s[j][i]==m[k])
								break;
						}
						if(k==l)
						    match[j]=0,K--;
					}
			}
			else
				for(j=0;j<D;j++)
				    if(match[j]&&s[j][i]!=c)
				        match[j]=0,K--;
		}
		printf("Case #%d: %d\n",X,K);
	}
}
