#include <iostream>

using namespace std;
int N,L,D;
char str[10000][1000];
char qstr[10001];
bool prs[32][1000];

void parse()
{
	memset(prs,0,sizeof(prs));
	
	for(int i=0,j=0;qstr[i]!=0;)
	{
		//cout<<j<<":";
			if(qstr[i]=='(')
			{
				i++;
				while(qstr[i]!=')')
				{
					prs[j][qstr[i]]=1;
			//		cout<<qstr[i];
					i++;
				}
			}
			else
				prs[j][qstr[i]]=1;
			i++;j++;
		//	cout<<endl;
	}
		
}
int query()
{
	int cnt=0;
	for(int i=1;i<=D;i++)
	{
		bool flag=1;
		for(int j=0;j<L;j++)
		{
			if(prs[j][str[i][j]]==0) {flag=0;break;}
		}	
		if(flag)
			cnt++;
	}	
	
	return cnt;
}


int main(int argc,char* argv[])
{
//	cout<<argv[1]<<endl;
	//system("PAUSE");
	freopen(argv[1],"r",stdin);
	freopen("G:\\Documents and Settings\\ivan\\Desktop\\A.txt","w",stdout);
	
	scanf("%d %d %d",&L,&D,&N);
	
	for(int i=1;i<=D;i++)
	{
		scanf("%s",str[i]);
		//cout<<str[i]<<endl;
	}
	for(int i=1;i<=N;i++)
	{
		memset(qstr,0,sizeof(qstr));
		
		scanf("%s",qstr);
		//cout<<qstr<<endl;
		parse();
		
		printf("Case #%d: %d\n",i,query());  
	}
}
