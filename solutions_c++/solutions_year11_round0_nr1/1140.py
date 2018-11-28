#include <cstdio>

int a[200], b[200], c[200], d[200];
int T,n;
int na,nb,la,lb,ta,tb,nowat,t,test,tot;
char ch;
int main()
{
    scanf("%d",&T);
    test=0;
    while (T--)
    {
        scanf("%d",&n);
        ta=tb=0;
        for (int i=0;i<n;++i)
        {
            scanf(" %c %d",&ch, &t);
            if (ch=='O') c[i]=-t; else c[i]=t;
            if (ch=='O') a[ta++]=t;
            else
                b[tb++]=t;
		}
		na=nb=0;
		la=lb=1;
		nowat=0;
		tot=0;
		while (nowat<n)
		{
		//	printf("%d %d %d %d\n",la,lb,nowat, c[nowat]);
			++tot;
			bool ca=false, cb=false;
			if (na<ta && la!=a[na])
			{
				if (la<a[na]) ++la; 
				if (la>a[na]) --la;
				ca=true;
			}
			if (nb<tb && lb!=b[nb])
			{
				if (lb<b[nb]) ++lb;
				if (lb>b[nb]) --lb;
				cb=true;
			}
			if (na<ta && la==a[na] && c[nowat]<0 && !ca)
			{
				++na;
				++nowat;
			}
			else if (nb<tb && lb==b[nb] && c[nowat]>0 && !cb)
			{
				++nowat;
				++nb;
			}
		}
		printf("Case #%d: %d\n",++test, tot);
	}
	return 0;
}
         
