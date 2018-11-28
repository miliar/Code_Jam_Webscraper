#include<cstdio>
#include<cstring>

typedef struct
{

	char ch;
	int k;
} A;

A a[500];

int todec(char *s)
{
	int len=strlen(s);

	if(len==1) return s[0]-'0';
	else if(len==2) return ( (s[0]-'0')*10 +(s[1]-'0'));
	else if(len==3) return 100;

}

int main()
{

	int i,j,k,l,o[500],b[500],oi,bi,T,stime,bn,on,C;
	char str[1000], *p;
	
	freopen("A-large.in","r",stdin);
	freopen("outAL1.out","w",stdout);
	scanf("%d",&T);

	C=0;
	getchar();
	while(T--)
	{
		//getchar();
		gets(str);

		strtok(str," ");

		bn=on=j=0;

		while(1)
		{
			p=strtok(NULL," ");
			if(p==NULL) break;
			a[j].ch=p[0];
			p=strtok(NULL," ");
			a[j].k=todec(p);

			if(a[j].ch=='O')
			{
				o[on++]=a[j].k;
			}
			if(a[j].ch=='B')
			{
				b[bn++]=a[j].k;
			}
			j++;

		}


		k=1;l=1;

		stime=oi=bi=0;
		i=0;

		while(j--)
		{
			if(a[i].ch=='O')	
			{
				oi++;

				if(l==a[i].k)
				{
					stime++;
					
					if(k<b[bi] && bi<bn)
					{
						k++;
					}
					else if(k>b[bi] && bi<bn)
					{
						k--;
					}

				}
				else if(l<a[i].k)
				{
					stime+=(a[i].k-l+1);
					

					if(k<b[bi] && bi<bn)
					{
						if((b[bi]-k)<(a[i].k-l+1))
							k=b[bi];
						else 
							k=k+(a[i].k-l+1);
					}
					else if(k>b[bi] && bi<bn)
					{
						if((k-b[bi])<(a[i].k-l+1))
							k=b[bi];
						else k=k-(a[i].k-l+1);
					}
					l=a[i].k;
				}
				else if(l>a[i].k)
				{
					stime+=(l-a[i].k+1);

					if(k<b[bi] && bi<bn)
					{
						if((b[bi]-k)<(l-a[i].k+1))
							k=b[bi];
						else 
							k=k+(l-a[i].k+1);
					}
					else if(k>b[bi] && bi<bn)
					{
						if((k-b[bi])<(l-a[i].k+1))
							k=b[bi];
						else k=k-(l-a[i].k+1);
					}
					l=a[i].k;
				}

			}
			else if(a[i].ch=='B')
			{
				bi++;

				if(k==a[i].k)
				{
					stime++;

					if(l<o[oi] && oi<on)
					{
						l++;
					}
					else if(l>o[oi] && oi<on)
					{
						l--;
					}
				
				}
				else if(k<a[i].k)
				{
					stime+=(a[i].k-k+1);
					
					if(l<o[oi] && oi<on)
					{
						if((o[oi]-l)<(a[i].k-k+1))
						{
							l=o[oi];
						}
						else 
							l=l+(a[i].k-k+1);
							
					}
					else if(l>o[oi] && oi<on)
					{
						if((l-o[oi])<(a[i].k-k+1))
						{
							l=o[oi];
						}
						else 
							l=l-(a[i].k-k+1);
					}
					
					k=a[i].k;

				}
				else if(k>a[i].k)
				{
					stime+=(k-a[i].k+1);
					if(l<o[oi] && oi<on)
					{
						if((o[oi]-l)<(k-a[i].k+1))
						{
							l=o[oi];
						}
						else 
							l=l+(k-a[i].k+1);
							
					}
					else if(l>o[oi] && oi<on)
					{
						if((l-o[oi])<(k-a[i].k+1))
						{
							l=o[oi];
						}
						else 
							l=l-(k-a[i].k+1);
					}
					
					k=a[i].k;
				}
			}
			i++;
			//printf("%d %d topb%d topo%d\n",k,l,bi,oi);

		}

		printf("Case #%d: %d\n",++C,stime);
		/*for(i=0;i<oi;i++) printf("%d ",o[i]);
		printf("\n");
		for(i=0;i<bi;i++) printf("%d ",b[i]);
		printf("\n");*/

	}



	return 0;
}
