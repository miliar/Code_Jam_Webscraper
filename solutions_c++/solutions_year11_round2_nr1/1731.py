#include <cstdio>
#include <cstdlib>
int main()
{
	int mat[111][111];
	int wp[111][2];
	double owp[111],oowp[111];
	char s[150];
	int n;
	int ri,rp,j,i;
	freopen("d:\\gcj\\r1b\\A-small-attempt0(1).in","r",stdin);
	freopen("d:\\gcj\\r1b\\aout.txt","w",stdin);

	scanf("%d",&rp);
	for (ri=0;ri<rp;ri++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			int l,w;
			l=w=0;
			scanf("%s",s);
			for (j=0;j<n;j++)
			{
				switch (s[j])
				{
				case '0':mat[i][j]=-1; l++; break;
				case '1':mat[i][j]=1;  w++; break;
				case '.':mat[i][j]=0; break;
				}
			}
			wp[i][0]=w;
			wp[i][1]=l;
		}
		for (i=0;i<n;i++)
		{
			double tmp=0;
			int cnt=0;
			for (j=0;j<n;j++)
			{
				if (mat[i][j])
				{
					int w=wp[j][0],l=wp[j][1];
					if (mat[i][j]==1)
						l--;
					else
						w--;
					tmp+=1.0*w/(l+w);
					cnt++;
				}
			}
			owp[i]=tmp/cnt;
		}
		for (i=0;i<n;i++)
		{
			double tmp=0;
			int cnt=0;
			for (j=0;j<n;j++)
			{
				if (mat[i][j])
				{
					tmp+=owp[j];
					cnt++;
				}
			}
			oowp[i]=tmp/cnt;
		}
		printf("Case #%d:\n",ri+1);
		/*for (i=0;i<n;i++)
		{
			printf("%.9lf\n",owp[i]);
		}
		printf("\n");
		for (i=0;i<n;i++)
		{
			printf("%.9lf\n",oowp[i]+);
		}*/
		for (i=0;i<n;i++)
		{
			double tmp=1.0*wp[i][0]/(wp[i][1]+wp[i][0]);
			tmp*=0.25;
			tmp+=0.5*owp[i];
			tmp+=0.25*oowp[i];
			printf("%.12lf\n",tmp);
		}
	}
	return 0;
}

