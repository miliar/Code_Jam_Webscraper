#include <stdio.h>
#include <set>
#include <string>

using namespace std;

set<string> x;

char s[1000][1000];
int r,c,f;

int go(int a,int b)
{
	int i,j,rr,m=1<<30;
	string q = "";
	if (b==r-1) 
	{
	//	printf("%s\n",q.c_str());
		return 0;
	}

	i=a;
	while (i>0 && s[b][i-1]=='.' && s[b+1][i-1]=='#') --i;
	s[b][i]='P';
	for (j=0;j<r;++j) q+=s[j];
	s[b][i]='.';

	if (x.find(q)!=x.end()) return -1;
	x.insert(q);

	if (i>0 && s[b][i-1]=='.')
	{
		j=b;
		while (j<r && s[j][i-1]=='.') ++j;
		if (j-b-1<=f)
		{
			rr=go(i-1,j-1);
			if (rr!=-1) if (rr<m) m=rr;
		}
	}
	while (1)
	{
		if (i<c-1 && s[b][i+1]=='.' && s[b+1][i+1]=='#')
		{
			s[b+1][i+1]='.';
			rr=go(i,b);
			if (rr!=-1) if (rr+1<m) m=rr+1;
			s[b+1][i+1]='#';
		}
		if (i>0 && s[b][i-1]=='.' && s[b+1][i-1]=='#')
		{
			s[b+1][i-1]='.';
			rr=go(i,b);
			if (rr!=-1) if (rr+1<m) m=rr+1;
			s[b+1][i-1]='#';
		}

		if (i<c-1 && s[b][i+1]=='.' && s[b+1][i+1]=='#') ++i; else break;
	}

	if (i<c-1 && s[b][i+1]=='.')
	{
		j=b;
		while (j<r && s[j][i+1]=='.') ++j;
		if (j-b-1<=f)
		{
			rr=go(i+1,j-1);
			if (rr!=-1) if (rr<m) m=rr;
		}
	}

	if (m==1<<30) return -1;
	return m;
}

int main()
{
	int ni=1,i,j,k;
	scanf("%d",&i);
	while (scanf("%d %d %d",&r,&c,&f)==3)
	{
		for (i=0;i<r;++i) scanf("%s",s[i]);
		x.clear();
		k=go(0,0);
		printf("Case #%d: ",ni++);
		if (k==-1) printf("No\n"); else printf("Yes %d\n",k);
	}
	return 0;
}
