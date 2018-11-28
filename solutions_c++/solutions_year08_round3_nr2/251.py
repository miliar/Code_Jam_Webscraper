#include<stdio.h>
#include<string.h>


__int64 a[111], n;



__int64 func(__int64 now, __int64 sum, __int64 prenum, char op)
{
	if(now==n)
	{
		if(op=='-')
			sum=sum-prenum;
		else
			sum=sum+prenum;
		if(sum%2==0 || sum%3==0 || sum%7==0 || sum%5==0)
			return 1;
		return 0;
	}
	__int64 pn, ret;
	if(op=='-')
		pn=sum-prenum;
	else
		pn=sum+prenum;
	ret=func(now+1, pn, a[now], '+');
	ret+=func(now+1, pn, a[now], '-');
	ret+=func(now+1, sum, prenum*10+a[now], op);
	return ret;
}



int main()
{
	freopen("B-small-attempt5.in.txt", "r", stdin);
	freopen("bbbb.ans", "w", stdout);

	__int64 t, test, i, res;
	char str[111];
	scanf("%I64d", &test);
	for(t=0; t<test; t++)
	{
		scanf("%s", str);
		n=strlen(str);
//		printf("%s", str);
		for(i=0; i<n; i++)
			a[i]=str[i]-'0';
		res=func(1, 0, a[0], '+');
	//	res+=func(1, 0, a[0], '-');
		printf("Case #%I64d: %I64d\n", t+1, res);
	}
	return 0;
}
