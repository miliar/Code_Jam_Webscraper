#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

char s[1000000];

vector <string> p;

int process(char * q)
{
	size_t i,j,k=0;
	for (i=0;i<p.size();++i) 
	{
		for (j=0;j<p[i].size() && q[j];++j) if (p[i][j]!=q[j]) break;
		if (q[j]==0 || q[j]=='/') if (j<p[i].size() && p[i][j]!='/' && j>0) --j;
		if (j>k) k=j;
	}
	p.push_back(q);
	if (q[k]==0) return 0;
	j=0;
	if (q[k]!='/') ++j;
	for (;q[k];++k) if (q[k]=='/') ++j;
	return j;
}

int main()
{
	int i,j,n,m,t=0;
	scanf("%d",&n);
	while (scanf("%d %d",&n,&m)==2)
	{
		p.clear();
		for (i=0;i<n;++i) { scanf("%s",s); process(s); }
		j=0;
		for (i=0;i<m;++i) { scanf("%s",s); j+=process(s); /*printf(">%d\n",j);*/ }
		printf("Case #%d: %d\n",++t,j);
	}
	return 0;
}
