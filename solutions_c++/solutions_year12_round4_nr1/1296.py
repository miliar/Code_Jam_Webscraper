
#include <stdio.h>
#include <map>
using namespace std;

const int maxn = 10010;

int n;
int pos[maxn],len[maxn];
int tol;

map<pair<int,int>,bool> hash;

inline int min(int a,int b)
{
	return a<b?a:b;
}

bool solve(int bak,int cur)
{
	if(hash.find(make_pair(bak,cur))!=hash.end())
		return hash[make_pair(bak,cur)];
	int i;
	if(pos[cur] + bak>=tol)
        return hash[make_pair(bak,cur)] = true;

	for(i=cur+1;i<=n;i++)
	{
        if(pos[cur]+bak<pos[i])
			break;
		if(solve(min(len[i],pos[i]-pos[cur]),i))
			return true;
	}
	return hash[make_pair(bak,cur)] = false;
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-out.txt","w",stdout);
	int ct,caset = 1;
	scanf("%d",&ct);
	while(ct--)
	{
		printf("Case #%d: ",caset++);
        scanf("%d",&n);
		int i;
		pos[0] = 0;
		for(i=1;i<=n;i++) scanf("%d%d",&pos[i],&len[i]);
		scanf("%d",&tol);
		hash.clear();
		if(solve(pos[1],1))
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}