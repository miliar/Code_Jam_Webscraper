#include<iostream>
#include<cstdio>
#include<set>
using namespace std;

FILE *fp,*fp2;

void Init()
{
	fp = fopen("C-small-attempt0.in","r");
	fp2 = fopen("C-small.out","w");
}

void Close()
{
	fclose(fp);
	fclose(fp2);
}

int dp[10];

inline int fun(int a)
{
	int i = 1;
	while(a > 0)
	{
		dp[i] = a%10;
		i++;
		a /= 10;
	}
	return i-1;
}

inline int fun2(int j,int len)
{
	int i;
	int k = 1;
	int sum = 0;
	for(i=j+1;i<=len;i++)
	{
		sum += k*dp[i];
		k *= 10;
	}
	for(i=1;i<=j;i++)
	{
		sum += k*dp[i];
		k *= 10;
	}
	return sum;
}

int main(void)
{
	Init();

	int i,j,T,cases;
	int a,b;
	fscanf(fp,"%d",&cases);
	for(T=1;T<=cases;T++)
	{
		int count = 0;
		fscanf(fp,"%d %d",&a,&b);
		for(i=a;i<b;i++)
		{
			int len = fun(i);
			if(len > 1)
			{
				set<int> s;
				for(j=1;j<len;j++)
				{
					int k = fun2(j,len);
					if(k <= b && k>i)
						s.insert(k);
				}
				count += s.size();
			}
		}
		
		fprintf(fp2,"Case #%d: %d\n",T,count);
	}

	Close();
	return 0;
}