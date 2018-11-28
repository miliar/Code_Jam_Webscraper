#include<stdio.h>
#include<string.h>

int f1,f2,cnt,k;
char str[100][100];

int check(int i, int j)
{
	if(cnt==k)
	{
		if(str[i][j] == 'R')
			f1 = 1;
		else if(str[i][j] == 'B')
			f2=1;
		return 1;
	}
	return 0;
}
int main()
{
	int t,n,i,j,p,q,caseno=1;

	//freopen("input.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	scanf("%d",&t);

	while(t--)
	{
		scanf("%d%d",&n,&k);
		getchar();

		for(i=1; i<=n; i++)
		{
			gets(str[i]);

			for(p=j=n-1; p>=0; p--)
			{
				if(str[i][p]!='.' && str[i][j]=='.')
				{
					str[i][j] = str[i][p];
					str[i][p]='.';
					j--;
				}

				if(str[i][j]!='.')
					j--;
			}
		}

		f1=0, f2=0;

		for(i=n; i>=1; i--)
		{
			for(j=n-1; j>=0; j--)
			{
				if((f1==1 && str[i][j] == 'R') || (f2==1 && str[i][j] == 'B'))
					continue;

				if(str[i][j]!='.')
				{
					cnt=1;

					for(p=j;p>j-k+1; p--)
					{
						if(str[i][p]==str[i][p-1] && cnt<k)
							cnt++;
						else
							break;
					}

					if(check(i,j)==0)
					{
						cnt=1;

						for(p=i;p>i-k+1; p--)
						{
							if(str[p][j]==str[p-1][j] && cnt<k)
								cnt++;
							else
								break;
						}

						if(check(i,j)==0)
						{
				
							cnt=1;
							for(p=i,q=j; p>i-k+1 && q>j-k+1; p--,q--)
							{
								if(str[p][q]==str[p-1][q-1] && cnt<k)
									cnt++;
								else
									break;
							}

							if(check(i,j)==0)
							{
								cnt=1;
								for(p=i,q=j; p>i-k+1 && q<n; p--,q++)
								{
									if(str[p][q]==str[p-1][q+1] && cnt<k)
										cnt++;
									else
										break;
								}
							}
							check(i,j);
						}
					}
				}
				
				
			}

			if(f1==1 && f2==1)
				break;
		}

		if(f1==1 && f2==1)
			printf("Case #%d: Both\n",caseno++);
		else if(f1==1)
			printf("Case #%d: Red\n",caseno++);
		else if(f2==1)
			printf("Case #%d: Blue\n",caseno++);
		else
			printf("Case #%d: Neither\n",caseno++);


	}
	return 0;
}