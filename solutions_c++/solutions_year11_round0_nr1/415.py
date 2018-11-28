#include<cstdio>

const int mx=110;

int ca;
int n;
int a[mx];
char type[mx];

int find(int pos,char c)
{
	while(pos<n)
	{
		if(type[pos]==c)
			break;
		pos++;
	}
	return pos;
}

void solve()
{
	int pa=find(0,'O'),pb=find(0,'B');
	int pos_a=1,pos_b=1;
	int cnt=0;
	while(pa<n||pb<n)
	{
		//printf("pa=%d,pb=%d,pos_a=%d,pos_b=%d\n",pa,pb,pos_a,pos_b);
		if(pa<pb)
		{
			if(pos_a==a[pa])
			{
				pa=find(pa+1,'O');
				if(pb<n)
					pos_b+=(a[pb]==pos_b?0:(a[pb]<pos_b?-1:1));
			}
			else
			{
				pos_a+=(a[pa]==pos_a?0:(a[pa]<pos_a?-1:1));
				if(pb<n)
				{
					pos_b+=(a[pb]==pos_b?0:(a[pb]<pos_b?-1:1));
				}
			}
		}
		else
		{
			if(pos_b==a[pb])
			{
				pb=find(pb+1,'B');
				if(pa<n)
					pos_a+=(a[pa]==pos_a?0:(a[pa]<pos_a?-1:1));
			}
			else
			{
				pos_b+=(a[pb]==pos_b?0:(a[pb]<pos_b?-1:1));
				if(pa<n)
				{
					pos_a+=(a[pa]==pos_a?0:(a[pa]<pos_a?-1:1));
				}
			}
		}
		cnt++;
	}
	printf("Case #%d: %d\n",++ca,cnt);
}

char s[mx];

int main()
{
	int i,t;
	ca=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%d",s,&a[i]);
			type[i]=s[0];
		}
		solve();
	}
	return 0;
}

