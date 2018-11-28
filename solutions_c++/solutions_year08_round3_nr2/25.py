#include <cstdio>
#include <cstring>
using namespace std;

int nt;

char mas[16];
int len,h[16];
int nums[16][16];
int br;

void rec(int ind)
{
	if(ind==len-1)
	{
		long long cs=mas[0]-'0';
		
		int i=0;
		while(h[i]==0&&i<len-1)
		{
			cs*=10;
			cs+=mas[i+1]-'0';
			i++;
		}
		while(i<len-1)
		{
			if(h[i]==1)
			{
				long long c=mas[i+1]-'0';
				i++;
				while(h[i]==0&&i<len-1)
				{
					c*=10;
					c+=mas[i+1]-'0';
					i++;
				}
				cs-=c;
			}
			if(h[i]==2)
			{
				long long c=mas[i+1]-'0';
				i++;
				while(h[i]==0&&i<len-1)
				{
					c*=10;
					c+=mas[i+1]-'0';
					i++;
				}
				cs+=c;
			}
		}
		
		if(cs%2==0||cs%3==0||cs%5==0||cs%7==0) br++;
		
		return ;
	}
	
	h[ind]=0;
	rec(ind+1);
	h[ind]=1;
	rec(ind+1);
	h[ind]=2;
	rec(ind+1);
	
}

void read()
{
	memset(mas,0,sizeof(mas));
	memset(h,0,sizeof(h));
	memset(nums,0,sizeof(nums));
	br=0;
	scanf("%s\n",mas);
	len=strlen(mas);
	
	
	long long sum=0;
	for(int i=0;i<len;i++)
	{
		sum=0;
		for(int j=i;j<len;j++)
		{
			sum*=10;
			sum+=mas[j]-'0';
			nums[i][j]=sum;
		}
	}
	
	rec(0);
}

int main()
{
	scanf("%d\n",&nt);
	
	for(int i=0;i<nt;i++)
	{
		read();
		printf("Case #%d: %d\n",i+1,br);
	}


    return 0;
}
