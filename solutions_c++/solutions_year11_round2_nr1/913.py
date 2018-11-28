#include<iostream>
using namespace std;
char ch[105][105];
double wb[105],owb[105],oowb[105];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T,k,n;
	int i,j;
	scanf("%d",&T);
	for(k=1;k<=T;k++)
	{
		scanf("%d",&n);
		getchar();
		int coun[105];
		int sum[105];
		memset(sum,0,sizeof(sum));
		memset(coun,0,sizeof(coun));
		for(i=0;i<n;i++)
		{
			scanf("%s",ch[i]);
			getchar();
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(ch[i][j]=='.') continue;
				if(ch[i][j]=='1')  coun[i]++;
				sum[i]++;
			}
		}
		for(i=0;i<n;i++)
		{
			wb[i]=(coun[i]*1.0)/(sum[i]*1.0);
		}
		int c;
		double temp;
		for (int j = 0; j < n; j++)
		{
			c = 0, temp = 0;
			for (int k = 0; k < n; k++)
			{
				if (j == k || ch[k][j] == '.')
					continue;
				else
				{
					c++;
					if (ch[k][j] == '1')
						temp += double(coun[k] - 1) / double(sum[k] - 1);
					else
						temp += double(coun[k]) / double(sum[k] - 1);

				}
			}
			owb[j] = temp / double(c);
		}
		double num;
		for(i=0;i<n;i++)
		{
			num = 0.0;
			for(j=0;j<n;j++)
			{
				if(ch[i][j]=='.') continue;
				num+=owb[j];
			}
			oowb[i]=num/(sum[i]*1.0);
		}
		printf("Case #%d:\n",k);
		for(i=0;i<n;i++)
		{
			printf("%.12f\n",0.25 * wb[i] + 0.50 * owb[i] + 0.25 * oowb[i]);
		}

	}
	return 0;
	fclose(stdin);
	fclose(stdout);
}