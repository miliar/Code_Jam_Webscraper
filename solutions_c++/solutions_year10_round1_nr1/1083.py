#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;

int n,k;

int getcolor(char ch)
{
	if(ch=='R')
		return 1;
	else if(ch=='B')
		return 2;

	return 0;
}


int iswin(char table[][70], int i, int j)
{
	/*
	int m;
	char cur=table[i][j];

	int c=0;
	for(m=0;m<k;m++)
	{
		if(j+m>=n)
			break;

		if(cur==table[i][j+m])
			c++;
	}

	if(c == k)
	{
		if(j==0 || (j>0 && table[i][j-1] != table[i][j]))
			if(j+m>=n || table[i][j] != table[i][j+m])
				return getcolor(table[i][j]);

	}

	c=0;
	for(m=0;m<k;m++)
	{
		if(i+m>=n)
			break;
		if(cur==table[i+m][j])
			c++;
	}

	if(c == k)
	{
		if(i==0 || (i>0 && table[i-1][j] != table[i][j]))
			if(i+m>=n || table[i][j] != table[i+m][j])
			return getcolor(table[i][j]);
	}


	c=0;
	for(m=0;m<k;m++)
	{
		if(i+m>=n || j+m>=n)
			break;

		if(cur==table[i+m][j+m])
			c++;
	}

	if(c == k)
	{
		if(i==0 || j==0 || (i>0 && j>0 && table[i-1][j-1] != table[i][j]))
			if(i+m>=n || j+m>=n || table[i][j] != table[i+m][j+m])
			return getcolor(table[i][j]);
	}

	c=0;
	for(m=0;m<k;m++)
	{
		if(i+m>=n || j-m<0)
			break;

		if(cur==table[i+m][j-m])
			c++;
	}

	if(c == k)
	{
		if(i==0 || j==n-1 || (table[i-1][j+1] != table[i][j]))
			if(i+m>=n || j-m<0 || table[i][j] != table[i+m][j-m])
				return getcolor(table[i][j]);
	}
	*/
	int m;
	char cur=table[i][j];

	int c=0;
	for(m=0;m<k;m++)
	{
		if(j+m>=n)
			break;

		if(cur==table[i][j+m])
			c++;
	}

	if(c == k)
	{
		return getcolor(table[i][j]);
	}

	c=0;
	for(m=0;m<k;m++)
	{
		if(i+m>=n)
			break;
		if(cur==table[i+m][j])
			c++;
	}

	if(c == k)
	{
		return getcolor(table[i][j]);
	}


	c=0;
	for(m=0;m<k;m++)
	{
		if(i+m>=n || j+m>=n)
			break;

		if(cur==table[i+m][j+m])
			c++;
	}

	if(c == k)
	{
		return getcolor(table[i][j]);
	}

	c=0;
	for(m=0;m<k;m++)
	{
		if(i+m>=n || j-m<0)
			break;

		if(cur==table[i+m][j-m])
			c++;
	}

	if(c == k)
	{
		return getcolor(table[i][j]);
	}
	return 0;
}

int main()
{
	int T;
	freopen("A-large.in","r",stdin);

	scanf("%d",&T);
	
	char table[70][70];
	
	for(int C=1;C<=T;C++)
	{
		char buf[100]={0,};

		scanf("%d %d", &n, &k);

		gets(buf);
		memset(table,0,sizeof(table));

		for(int i=0;i<n;i++)
		{
			gets(buf);
			int c=n-1;
			for(int j=n-1;j>=0;j--)
			{
				if(buf[j] == '.')
					continue;

				table[i][c] = buf[j];
				c--;
			}
		}

		bool red=false, blue=false;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(red && blue)
					goto exit;
				
				if(table[i][j] == '.')
					continue;

				int who=0;
				if(who=iswin(table,i,j))
				{
					if(who==1)
						red=true;
					else if(who==2)
						blue=true;
				}
			}
		}

exit:
		if(red && blue)
		{
			printf("Case #%d: Both\n",C);
		}
		else if(red)
		{
			printf("Case #%d: Red\n",C);
		}
		else if(blue)
		{
			printf("Case #%d: Blue\n",C);
		}
		else
		{
			printf("Case #%d: Neither\n",C);
		}
	}


	return 0;
}