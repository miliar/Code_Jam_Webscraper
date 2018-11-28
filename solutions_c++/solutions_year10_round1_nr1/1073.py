#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<set>


using namespace std;
char arr[51][51],rev[51][51];
int contr = 0,contb=0;
int n,k;
int linl,linf,diar,dial;

void checklinl(char ch,int i,int j)
{
	if(rev[i][j] != ch)
	{
		if(linl < k-1)
			linl = 0;
		return;
	}
	if(i<n-1 && rev[i+1][j] == ch)
	{
		linl++;
		checklinl(ch,i+1,j);
	}
}


void checklinf(char ch,int i,int j)
{
	if(rev[i][j] != ch)
	{
		if(linf < k-1)
			linf = 0;
		return;
	}
	if(j<n-1 && rev[i][j+1] == ch)
	{
		linf++;
		checklinf(ch,i,j+1);
	}
}

void checkdiar(char ch,int i,int j)
{
	if(rev[i][j] != ch)
	{
		if(diar < k-1)
			diar = 0;
		return;
	}
	if(i<n-1 && j<n-1 && rev[i+1][j+1] == ch)
	{
		diar++;
		checkdiar(ch,i+1,j+1);
	}
}

void checkdial(char ch,int i,int j)
{
	if(rev[i][j] != ch)
	{
		if(dial < k-1)
			dial = 0;
		return;
	}
	if(i<n-1 && j>0 && rev[i+1][j-1] == ch)
	{
		dial++;
		checkdial(ch,i+1,j-1);
	}
}
int main(void){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t = 1; t<=T; t++)
	{
		memset(rev,0,sizeof(rev[0]));
		
		scanf("%d%d",&n,&k);

		int i,j;
		for(i=0;i<n;i++)
		{
			scanf("%s",arr[i]);
		}

		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				rev[j][i] = arr[n-i-1][j];
			}
			rev[i][j] = '\0';
		}

		j = 0;
		while(j<n)
		{
			for(i=n-1;i>0;i--)
			{
				if(rev[i][j] == '.')
				{
					int a = i;
					while(a>=0)
					{
						if(rev[a][j] == 'R' || rev[a][j] == 'B')
						{
							swap(rev[i][j],rev[a][j]);
							break;
						}
						a--;
					}
				}
			}

			j++;
		}

		bool flR = false, flB = false;

		
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(flB == false && rev[i][j] == 'B')
				{
					linl=0,linf=0,diar=0,dial=0;
					checklinl('B',i,j);
					if(linl == k-1)
						flB = true;
					if(flB == false)
					{
						checklinf('B',i,j);
						if(linf == k-1)
							flB = true;
					}

					if(flB == false)
					{
						checkdiar('B',i,j);
						if(diar == k-1)
							flB = true;
					}

					if(flB == false)
					{
						checkdial('B',i,j);
						if(dial == k-1)
							flB = true;
					}
				}

				if(flR == false && rev[i][j] == 'R')
				{
					linl=0,linf=0,diar=0,dial=0;
					checklinl('R',i,j);
					if(linl == k-1)
						flR = true;
					if(flR == false)
					{
						checklinf('R',i,j);
						if(linf == k-1)
							flR = true;
					}

					if(flR == false)
					{
						checkdiar('R',i,j);
						//printf("%d\n",diar);
						if(diar == k-1)
							flR = true;
					}

					if(flR == false)
					{
						checkdial('R',i,j);
						if(dial == k-1)
							flR = true;
					}
				}
			}
		}

		printf("Case #%d: ",t);
		if(flB == true && flR == true)
		{
			puts("Both");
		}
		else if(flB)
		{
			puts("Blue");
		}
		else if(flR)
		{
			puts("Red");
		}
		else
		{
			puts("Neither");
		}
	}
	return 0;
}