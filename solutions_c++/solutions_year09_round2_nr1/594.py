#include<iostream>
#include<cstring>
#include<string>
#include<sstream>
#include<map>
#include<cctype>
#include<vector>

using namespace std;

int L,A;
string name;
bool flag[1000];
char buffer[1000];
map<string,int>mymap;
vector<string>text;
int mp;

struct Node
{
	bool leaf; //leaf
	int p[2];
	double w;
	int fea;
};

Node Tree[100000];
int pt;

double Get(string st)
{
	stringstream ssin(st);
	double v;
	ssin>>v;
	return v;
}

void Parse(int cur,int f,int r)
{	
	Tree[cur].w=Get(text[f+1]);
	Tree[cur].leaf=false;
	if (f+2==r) //leaf
	{
		Tree[cur].leaf=true;
	}
	else
	{
		Tree[cur].fea=mymap[text[f+2]]=mp++;
		int add=1;
		int i;
		for (i=f+4;add;i++)
			if (text[i]=="(") add++;
			else
				if (text[i]==")") add--;
		i--;
		Tree[cur].p[0]=++pt;
		Parse(Tree[cur].p[0],f+3,i);
		Tree[cur].p[1]=++pt;
		Parse(Tree[cur].p[1],i+1,r-1);
	}
}

double Solve(int at,double v)
{
	if (Tree[at].leaf) return Tree[at].w*v;
	else
	{
		v*=Tree[at].w;
		if (flag[Tree[at].fea])
			return Solve(Tree[at].p[0],v);
		else
			return Solve(Tree[at].p[1],v);
	}
}

int main()
{
	int t;
	int i,j,k;
	int cas=0;
	int tot;
	string str;

	freopen("in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);

	while (t--)
	{
		cas++;
		scanf("%d",&L);
		while (getchar()!='\n');
		text.clear();
		for (i=0;i<L;i++)
		{
			gets(buffer);
			for (j=0;buffer[j];j++)
			{
				switch (buffer[j])
				{
				case '(':
					text.push_back("(");
					break;
				case ')':
					text.push_back(")");
					break;
				default:
					if (isdigit(buffer[j]))  //digit
					{
						str="";
						for (k=j;buffer[k] && (isdigit(buffer[k]) || buffer[k]=='.') ;k++)str+=buffer[k];
						text.push_back(str);
						j=k-1;
					}
					else
					{
						if (isalpha(buffer[j]))
						{
							str="";
							for (k=j;buffer[k] &&isalpha(buffer[k]) ;k++) str+=buffer[k];;
							text.push_back(str);
							j=k-1;
						}
					}
				}
			}
		}

	//	for (i=0;i<text.size();i++) printf("%s ",text[i].c_str());putchar('\n');
		mymap.clear();mp=0;pt=0;
		Parse(0,0,text.size()-1);

		printf("Case #%d:\n",cas);
		scanf("%d",&A);
		for (i=0;i<A;i++)
		{
			scanf("%s",buffer);
			name=buffer;
			memset(flag,0,sizeof(flag));
			scanf("%d",&tot);
			for (j=0;j<tot;j++)
			{
				scanf("%s",buffer);
				if (mymap.find(buffer)!=mymap.end())
					flag[mymap[(string)buffer]]=true;				
			}
			printf("%.7lf\n",Solve(0,1));
		}
	}
	return 0;
}