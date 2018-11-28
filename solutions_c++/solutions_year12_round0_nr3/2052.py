#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

int Map[2000100];

bool Check(int a,int b)
{
	if (Map[b]==a)	return false;
	Map[b]=a;
	return true;
}

void Solve(int TestNo)
{
	int A,B,Ans=0;
	memset(Map,0,sizeof(Map));
	char str[30],tmp[30];
	scanf("%d%d",&A,&B);
	for (int i=A;i<=B;++i)
	{
		memset(str,0,sizeof(str));
		sprintf(str,"%d%d",i,i);
		int len=strlen(str)/2;
		for (int t=1;t<len;++t)
			if (str[t]!='0')
			{
				memset(tmp,0,sizeof(tmp));
				strncpy(tmp,str+t,len);
				int j;
				sscanf(tmp,"%d",&j);
				Ans+= (A<=j&&j<i&&j<=B)&&Check(i,j);
			}
	}
	printf("Case #%d: %d\n",TestNo,Ans);
	cerr<<Ans<<endl;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
		Solve(i);
	return 0;
}

