#include <iostream>
#include <cstring>
#include <string>
using namespace std;

char feature[101][1000];
int n,l,a;
int m;
char tree[1000000];
int p;
char name[1001];

int has(char *s)
{
	int i;
	for(i=0;i<m;i++)
		if(strcmp(feature[i],s)==0)
			return 1;
	return 0;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	//scanf("%d",&n);
	cin>>n;
	int c;
	for(c=1;c<=n;c++)
	{
		printf("Case #%d:\n",c);
		memset(tree,0,sizeof(tree));
		int i;
		cin>>l;
		//string tmp;
		char tmp[10001];
		getchar();
		for(i=0;i<l;i++)
		{
			//getline(cin,tmp);
			//tree=tree+tmp;
			gets(tmp);
			strcat(tree,tmp);
		}
		p=0;
		scanf("%d",&a);
		int j;
		for(j=0;j<a;j++)
		{
			scanf("%s",name);
			
			scanf("%d",&m);
			for(i=0;i<m;i++) scanf("%s",feature[i]);
			p=0;
			double ans=1;
			while(true)
			{
				if(tree[p]=='(')
				{
					p++;
					//while(!(tree[p]>='0' && tree[p]<='9')) p++;
					while(tree[p]==' ') p++;
					double pro;
					sscanf(tree+p,"%lf",&pro);
					ans*=pro;
					while(tree[p]>='0' && tree[p]<='9' || tree[p]=='.')
						p++;
					while(tree[p]==' ') p++;
					if(tree[p]==')')
						break;
				}
				if(tree[p]==' ') p++;
				if(tree[p]>='a' && tree[p]<='z' || tree[p]>='A' && tree[p]<='Z')
				{
					sscanf(tree+p,"%s",tmp);
					if(has(tmp))
					{
						while(tree[p]!='(') p++;
					}
					else
					{
						int t=0;
						while(true)
						{
							if(tree[p]=='(') t++;
							if(tree[p]==')') 
							{
								t--;
								if(t==0) break;
							}
							++p;
						}
						while(tree[p]!='(') p++;
					}

				}
			}
			printf("%.7lf\n",ans);
		}
	}
	return 0;
}