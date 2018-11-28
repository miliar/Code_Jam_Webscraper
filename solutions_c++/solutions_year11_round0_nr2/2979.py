#include <iostream>
#include <string>
#include <map>
#include <utility>
using namespace std;

#define mp make_pair

int main()
{
	int t; 
	string ans;
	map<pair<char,char>, char> inv;
	map <char, char> op;
	map <char, int> cl;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int qw=1; qw<=t; qw++)
	{
		cl.clear(); op.clear(); inv.clear(); ans.clear();
		int c,d,n;
		char f,s,w;
		scanf("%d ",&c);
		for (int i=0; i<c; i++)
		{
			scanf("%c%c%c ",&f,&s,&w);
			inv[mp(f,s)]=w;
		}
		scanf("%d ",&d);
		for (int i=0; i<d; i++)
		{
			scanf("%c%c ",&f,&s);
			op[f]=s;
			op[s]=f;
		}
		scanf("%d %c",&n,&f);
		ans.push_back(f);
		int last=0;
		if (op[f]) cl[op[f]]++;
		for (int i=1; i<n; i++)
		{
			scanf("%c",&f);
			if (last<0) {ans.push_back(f); if(op[f]) cl[op[f]]++; last=0; continue;}
			w=ans[last];
			if (inv[mp(f,w)] ) {ans[last]=inv[mp(f,w)]; if (cl[op[w]]) cl[op[w]]--;} else
			if (inv[mp(w,f)] ) {ans[last]=inv[mp(w,f)]; if (cl[op[w]]) cl[op[w]]--;} else
			if (cl[f]) { ans.clear(); last=-1; cl.clear();}else
			{ans.push_back(f); if(op[f]) cl[op[f]]++; last++;}
		}
		printf("Case #%d: [",qw);
		if (ans.size()) printf("%c",ans[0]);
		for (int i=1; i<ans.size(); i++)
			printf(", %c",ans[i]);
		printf("]\n");
	}
	return 0;
}