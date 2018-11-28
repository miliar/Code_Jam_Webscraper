#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

const int MW=5555;
const int ML=21;
const int BL=111111;

int L,D,N,M,cur;
char wrd[MW][ML];
char pat[BL];
bool apply[MW];
bool mask[30];

void proc(int& x)
{
	int i,j;
	for(i=0;i<30;i++) mask[i]=0;

	if(pat[x]=='(')
		while(pat[++x]!=')') mask[pat[x]-'a']=1;
	else mask[pat[x]-'a']=1;
	x++;
	for(i=0;i<D;i++)
		if(apply[i])
		{
			apply[i]=(apply[i]&&(mask[wrd[i][cur]-'a']));
		}

	cur++;
}
void test()
{
	cur=0;
	scanf("%s",pat);
	M=strlen(pat);
	int i;

	for(i=0;i<D;i++) apply[i]=1;

	i=0;
	while(i<M) proc(i);

	int ans=0;
	for(i=0;i<D;i++) ans+=apply[i];

	printf("%d\n",ans);
	
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int i,t;

	scanf("%d%d%d",&L,&D,&N);

	for(i=0;i<D;i++) scanf("%s",wrd[i]);
	for(t=0;t<N;t++)
	{
		printf("Case #%d: ",t+1);
		test();
	}
}