#include <stdio.h>

int solve()
{
	int po1 = 1,po2 = 1;
	int t1 = 0, t2 = 0;
	int n;
	int t = 0;
	scanf("%d",&n);
	char s[5];
	int po;
	for(int i=0;i<n;++i)
	{
		scanf("%s%d",s,&po);
		if(s[0] == 'B')
		{
			int tmp = po - po1;
			po1 = po;
			if(tmp < 0) tmp = -tmp;
			if(t1 + tmp > t)
				t = t1 + tmp;
			++ t;
			t1 = t;
		}
		else
		{
			int tmp = po - po2;
			po2 = po;
			if(tmp < 0) tmp = -tmp;
			if(t2 + tmp > t)
				t = t2 + tmp;
			++t;
			t2 = t;
		}
//		printf("t= %d\n",t);
	}
	return t;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		printf("Case #%d: %d\n",i+1,solve());
	}
	return 0;
}

