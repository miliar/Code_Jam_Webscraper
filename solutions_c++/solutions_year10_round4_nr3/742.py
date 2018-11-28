#include <iostream>
#include <cstring>
#define REP(i,n) for(int i=1;i<=(n);i++)
using namespace std;


bool buf1[300][300],buf2[300][300]={0};
int n;
/*void Print(void)
{
			REP(i,n)
		{
			REP(j,n)
				printf("%d",buf1[i][j] ? 1 : 0);
			cout<<endl;
		}
			cout<<endl;
}*/

int main(void)
{
	freopen("s.in","r",stdin);
	freopen("s.out","w",stdout);
	int T;
	cin>>T;
	REP(W,T)
	{
		int R;
		n=0;
		scanf("%d",&R);
		int ans=0;
		memset(buf1,0,sizeof(buf1));
		memset(buf2,0,sizeof(buf2));
		REP(I,R){
		int x1,x2,y1,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		if(n<x2) n=x2;
		if(n<y2) n=y2;
		for(int i=x1;i<=x2;i++)
			for(int j=y1;j<=y2;j++)
				buf1[j][i]=true;
		}
		//Print();
		while(1)
		{
			int tag=0;
			REP(i,n) REP(j,n)
			{
				if(!buf1[i][j] && buf1[i][j-1] && buf1[i-1][j])
				{buf2[i][j]=true; tag=1;}
				else if(buf1[i][j] && !(!buf1[i][j-1] && !buf1[i-1][j]))
				{buf2[i][j]=true; tag=1;}
			}
			if(tag==0) break;
			memcpy(buf1,buf2,sizeof(buf1));
			memset(buf2,0,sizeof(buf2));
			//Print();
			ans++;
		}
		printf("Case #%d: %d\n",W,ans+1);
	}
	return 0;
}