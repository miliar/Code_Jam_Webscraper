#include <cstdio>
int main()
{
//	freopen("d:\\gj\\r1a\\A-small-attempt1.in","r",stdin);
//	freopen("d:\\gj\\r1a\\a.txt","r",stdin);
//	freopen("d:\\gj\\r1a\\ao.txt","w",stdout);
	char m[51][51];
	int kk,n,rp,i,j,k,ri;
	int wr,wb;
	scanf("%d",&rp);
	for (ri=1;ri<=rp;ri++)
	{
		scanf("%d%d",&n,&kk);
		wr=wb=0;
		gets(m[0]);
		for (i=0;i<n;i++)
		{
			gets(m[i]);
		}
		for (i=0;i<n;i++)
		{
			for (j=n-1;j>=0;j--)
				for (k=0;k<j;k++)
				{
					if ((m[i][k]!='.') && (m[i][k+1]=='.'))
					{
						m[i][k+1]=m[i][k];
						m[i][k]='.';
					}
			//		printf("%d: %s\n",i,m[i]);
				}
			/*for (int ii=0;ii<n;ii++)
			puts(m[ii]);
			printf("\n");*/
		}

		//heng
		for (i=0;i<n;i++)
		{
			int r=0,b=0;
			for (j=0;j<n;j++)
			{
				switch (m[i][j])
				{
				case '.':r=b=0; break;
				case 'R':r++; b=0; break;
				case 'B':b++; r=0; break;
				}
				if (r==kk) wr=1;
				if (b==kk) wb=1;
			//	printf("heng %d,%d\n",r,b);
			}
		}

		//shu
		for (i=0;i<n;i++)
		{
			int r=0,b=0;
			for (j=0;j<n;j++)
			{
				switch (m[j][i])
				{
				case '.':r=b=0; break;
				case 'R':r++; b=0; break;
				case 'B':b++; r=0; break;
				}
				if (r==kk) wr=1;
				if (b==kk) wb=1;
			//	printf("shu %d,%d\n",r,b);
			}
		}

		//xie1
		for (k=0;k<n+n-1;k++)
		{
			int r=0,b=0;
			for (i=(k<n-1?0:k-n+1),j=k-i;i<n && j>=0;i++,j--)
			{
				switch (m[i][j])
				{
				case '.':r=b=0; break;
				case 'R':r++; b=0; break;
				case 'B':b++; r=0; break;
				}
				if (r==kk) wr=1;
				if (b==kk) wb=1;
			//	printf("xie1 %d,%d\n",i,j);
			}
		}

		//xie2
		for (k=-n+1;k<n;k++)
		{
			int r=0,b=0;
			for (i=(k>=0?0:-k),j=i+k;i<n && j<n;i++,j++)
			{
				switch (m[i][j])
				{
				case '.':r=b=0; break;
				case 'R':r++; b=0; break;
				case 'B':b++; r=0; break;
				}
				if (r==kk) wr=1;
				if (b==kk) wb=1;
			//	printf("xie 2 %d,%d\n",i,j);
			}
		}
		printf("Case #%d: ",ri);
		switch (wr*2+wb)
		{
		case 0:printf("Neither\n"); break;
		case 1:printf("Blue\n"); break;
		case 2:printf("Red\n"); break;
		case 3:printf("Both\n"); break;
		}


	}
	return 0;
}