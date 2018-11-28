#include <cstdio>
#include <cstring>
using namespace std;

char dic[5010][16];
char in[16][26];

int L,D,N;


void Ini_In(char *buf)
{
	int i;
	memset(in,0,sizeof(in));
	for (i=0;i<L;++i,++buf)
	{
		if (*buf=='(')
		{
			for (++buf;(*buf)!=')';++buf)
			{
				in[i][(*buf)-'a'] = 1;
			}
		}
		else in[i][(*buf)-'a'] = 1;;
	}
}


bool Is(char *d)
{
	int i;
	for (i=0;i<L;++i,++d)
	{
		if (!in[i][(*d)-'a']) return false;
	}
	return true;
}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//freopen("Download A-large.in","r",stdin);
	//freopen("Download A-large.out","w",stdout);
	char buf[512];
	int i,j,ans;
	while (scanf("%d %d %d",&L,&D,&N)!=EOF)
	{
		for (i=0;i<D;++i) scanf("%s",dic[i]);
		for (i=0;i<N;++i)
		{
			scanf("%s",buf);
			Ini_In(buf);
			for (ans = j=0;j<D;++j)
			{
				if (Is(dic[j])) ++ans;
			}
			printf("Case #%d: %d\n",i+1,ans);
		}
	}
	return 0;
}


