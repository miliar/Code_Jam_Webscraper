#include <iostream>
#include <cstring>
using namespace std;
struct HP
{
	int len,digit[60];
};
HP s[1010],key,ans;
char T[100000];
int i,j,n,m,testcase,curcase = 1;
bool cmp(HP &q,HP &p)
{
	int i;
	if (q.len>p.len) return false;
	if (q.len<p.len) return true;
	for ( i = q.len ; i ; i-- ) if (q.digit[i]!=p.digit[i]) break;
	if (q.digit[i]<=p.digit[i]) return true; else return false;
}
HP sub(HP q,HP p)
{
	int i;
	HP ret;
	memset(ret.digit,0,sizeof(ret.digit));
	for ( i = 1 ; i <= q.len ; i++ )
	{
		ret.digit[i] += q.digit[i]-p.digit[i];
		if (ret.digit[i]<0)
		{
			ret.digit[i+1]--;
			ret.digit[i] += 10;
		}
	}
	ret.len = q.len;
	while ((ret.len>1)&&(ret.digit[ret.len]==0)) ret.len--;
	return ret;
}
HP mod(HP &q,HP &p)
{
	HP ret;
	int i,j;
	memset(ret.digit,0,sizeof(ret.digit));
	ret.len = 1;
	for ( i = q.len ; i ; i-- )
	{
		ret.len++;
		for ( j = ret.len ; j>1 ; j-- ) ret.digit[j] = ret.digit[j-1];
		ret.digit[1] = q.digit[i];
		while (cmp(p,ret)) ret = sub(ret,p);
		while ((ret.digit[ret.len]==0)&&(ret.len>1)) ret.len--;
	}
	return ret;
}
HP gcd(HP a,HP b)
{
	if ((b.len==1)&&(b.digit[1]==0)) return a; else return gcd(b,mod(a,b));
}
void ana()
{
	int p = -1;
	for ( i = 0 ; i < n ; i++ )
	{
		memset(s[i].digit,0,sizeof(s[i].digit));
		s[i].len = 0;
		p++;
		while ((T[p]!=0)&&(T[p]!=' '))
		{
			s[i].digit[++s[i].len] = T[p]-48;
			p++;
		}
		for ( j = 1 ; j <= s[i].len/2 ; j++ )
			swap(s[i].digit[j],s[i].digit[s[i].len+1-j]);
	}
}
void work1()
{
	s[n] = s[0];
	for ( i = 0 ; i < n ; i++ )
		if (cmp(s[i],s[i+1])) s[i] = sub(s[i+1],s[i]); else s[i] = sub(s[i],s[i+1]);
	key = s[0];
	for ( i = 1 ; i < n ; i++ )
		if ((s[i].len>1)||(s[i].digit[1]!=0)) key = gcd(key,s[i]);
}
void work2()
{
	ans = mod(s[n],key);
	if ((ans.len==1)&&(ans.digit[1]==0)) ;
	else
	{
		ans = sub(key,ans);
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d\n",&testcase) ; curcase <= testcase ; curcase++ )
	{
		scanf("%d ",&n);
		gets(T);
		ana();
		work1();
		work2();
		printf("Case #%d: ",curcase);
		for ( i = ans.len ; i ; i-- ) printf("%d",ans.digit[i]);
		printf("\n");
	}
}
