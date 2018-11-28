#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define MAXN 1010
#define MAXA 111
#define MAXLEN 111

struct Node{
	string s;
	double rate;
	int L,R;
};

const int R=1;

int A,size;
struct Node T[MAXN];
double ans;
vector<string> data;

void dfs(int x)
{
	ans*=T[x].rate;
	if (T[x].s=="")
		return;
	int i,len=data.size();
	bool flag=false;
	for (i=0;i<len;i++)
		if (data[i]==T[x].s)
		{
			flag=true;
			break;
		}
	if (flag)
		dfs(T[x].L);
	else
		dfs(T[x].R);

}

void run()
{
	dfs(R);
}

char getC()
{
	char c;
	do
	{
		cin>>c;
		if (c!=10 && c!=13 && c!=' ')
			return c;
	}while (true);
}

int build()
{
	int x=++size;
	char c;
	getC();
	cin>>T[x].rate;
	cin>>c;
	if (c==')')
		return x;
	else
	{
		ungetc(c,stdin);
		cin>>T[x].s;
		T[x].L=build();
		T[x].R=build();
		getC();
		return x;
	}
}


void ini()
{
	int i,k,p,line,C;
	string s,name;
	cin>>C;
	for (i=1;i<=C;i++)
	{
		printf("Case #%d:\n",i);

		size=0;
		memset(T,0,sizeof(T));


		cin>>line;
		build();
		scanf("%d\n",&A);
		for (k=1;k<=A;k++)
		{
			ans=1.000000;
			data.clear();
			cin>>name>>p;
			for (;p>0;p--)
			{
				cin>>s;
				data.push_back(s);
			}
			scanf("\n");
			run();
			printf("%lf\n",ans);
		}
		
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	ini();
	return 0;
}
