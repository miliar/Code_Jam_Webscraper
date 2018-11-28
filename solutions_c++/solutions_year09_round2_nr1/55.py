#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int N,LL,L,A,le[1 << 10],ri[1 << 10],NN;
double p[1 << 10];
char s1[100],str[1 << 20],len;
string fea[1 << 10];

map<string,int> mymap;

void expand(int l,int r,int n)
{
	int i,lp,rp,ll;
	char ss[100];
	double w;
	for(i = l;i <= r;i++)
	{
		if(str[i] == '(')
			break;
	}
	p[n] = 0;
	for(i++;i <= r && !(str[i] >= '0' && str[i] <= '9');i++);
	if(str[i] == '1')
		p[n] += 1.0;
	i += 2;
	w = 0.1;
	for(;i <= r && str[i] >= '0' && str[i] <= '9';i++)
		p[n] += w*(double)(str[i] - '0'),w /= 10.0;
	for(;i <= r && str[i] == ' ';i++);
	if(str[i] == ')' || i == r + 1)
	{
		le[n] = ri[n] = -1;
		return;
	}
	int j = 0;
	for(;i <= r && str[i] != ' ' && str[i] != ')';i++,j++)
		ss[j] = str[i];
	ss[j] = 0;
	//puts(ss);
	fea[n] = string(ss);
	for(i++;i <= r;i++)
	{
		if(str[i] == '(')
			break;
	}
	ll = i;
	lp = 1,rp = 0;
	for(i++;i <= r;i++)
	{
		if(str[i] == '(')
			lp++;
		else if(str[i] == ')')
			rp++;
		if(lp == rp)
			break;
	}
	le[n] = NN;
	NN++;
	expand(ll,i,NN - 1);
	ri[n] = NN;
	NN++;
	expand(i + 1,r,NN - 1);
}

double getp(int n)
{
	if(le[n] == -1)
		return p[n];
	if(mymap.find(fea[n]) != mymap.end())
		return p[n] * getp(le[n]);
	else
		return p[n] * getp(ri[n]);
}
	

int main()
{
	int i,j,t,fn;
	char s[100];
	//freopen("A-large.in","r",stdin);
	//freopen("A.txt","w",stdout);
	scanf("%d",&N);
	for(t = 1;t <= N;t++)
	{
		scanf("%d\n",&LL);
		L = 0;
		while(LL--)
		{
			gets(s1);
			for(i = 0;s1[i];i++)
				str[L++] = s1[i];
			str[L++] = ' ';
		}
		str[L] = 0;
		//puts(str);
		NN = 1;
		expand(0,L - 1,0);
		//for(i = 0;i < NN;i++)
		//	printf("%d %d %lf %s\n",le[i],ri[i],p[i],fea[i].c_str());
		printf("Case #%d:\n",t);
		scanf("%d",&A);
		while(A--)
		{
			scanf("%s",s);
			scanf("%d",&fn);
			mymap.clear();
			while(fn--)
				scanf("%s",s),mymap[string(s)] = fn;
			printf("%.10lf\n",getp(0));
		}
	}
	//system("PAUSE");
	return 0;
}
			
		
		
		
