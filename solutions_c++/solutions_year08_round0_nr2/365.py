#include <iostream>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

struct node
{
	int tim , isadd , isa;
	bool operator<(const node &ot)
	{
		if (tim != ot.tim) return tim<ot.tim;
		return isadd>ot.isadd;
	}
};

int ct(char *s)
{
	int h,m;
	h = s[0]*10+s[1];
	m = s[3]*10+s[4];
	return h*60+m;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	node ns[420];
	int ca,T,i,ti,a,b,aa,ab,t,na,nb,n;
	char s[100];
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		scanf("%d%d%d",&ti,&na,&nb);
		for (i = 0 ; i < na ; i++)
		{
			scanf("%s",s);
			ns[i*2].tim = ct(s);
			ns[i*2].isadd = 0;
			ns[i*2].isa = 1;
			scanf("%s",s);
			ns[i*2+1].tim = ct(s)+ti;
			ns[i*2+1].isadd = 1;
			ns[i*2+1].isa = 0;
		}
		n = na*2;
		for (i = 0 ; i < nb ; i++)
		{
			scanf("%s",s);
			ns[n+i*2].tim = ct(s);
			ns[n+i*2].isadd = 0;
			ns[n+i*2].isa = 0;
			scanf("%s",s);
			ns[n+i*2+1].tim = ct(s)+ti;
			ns[n+i*2+1].isadd = 1;
			ns[n+i*2+1].isa = 1;
		}
		n += nb*2;
		sort(ns,ns+n);
		a = b = t = 0;
		aa = ab = 0;
		for (i = 0 ; i < n ; i++)
		{
			if (ns[i].isadd)
			{
				if (ns[i].isa) a++;
				else b++;
			}
			else
			{
				if (ns[i].isa)
				{
					if (a > 0) a--;
					else aa++;
				}
				else
				{
					if (b > 0) b--;
					else ab++;
				}
			}
		}
		printf("Case #%d: %d %d\n",ca,aa,ab);
	}
	return 0;
}
