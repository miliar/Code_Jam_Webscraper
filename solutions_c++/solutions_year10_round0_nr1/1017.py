#pragma warning(disable:4996)
#pragma warning(disable:4010)//注释
#include<iostream>
#include<cstdio>
#include<ctime>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<cmath>
#include<cstring>
#include<map>
#include<string>
using namespace std;
const int sup=100;
int main()
{
	int bina[sup];
    int T,pzjay=0;
    int n,k;
	bool on;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
		on=true;
		++pzjay;
        memset(bina,0,sizeof(bina));
        scanf("%d%d",&n,&k);
        int i=0;
        while (k>0)
        {
            bina[++i]=k%2;
			k>>=1;
        }
        for (i=1;i<=n;++i)
            if (0==bina[i])
			{
				on=false;
                break;
			}
        if (on) 
			printf("Case #%d: ON\n",pzjay);
        else 
			printf("Case #%d: OFF\n",pzjay);
    }
}





//int main()
//{
//	int t;
//	int pzj=0;
//	int r,k,n;
//	int peo;
//	queue <int> wait,roller;
//	freopen("C.in","r",stdin);
//	freopen("C-small.txt","w",stdout);
//	scanf("%d",&t);
//	while(t--)
//	{
//		while(!wait.empty())
//			wait.pop();
//		while(!roller.empty())
//			roller.pop();
//		scanf("%d %d %d",&r,&k,&n);//嗯k次
//		for(int i=0;i<n;++i)
//		{
//			scanf("%d",&peo);
//			wait.push(peo);
//		}
//		printf("Case #%d: ",++pzj);
//		int tmp,ans=0;
//		for(int i=0;i<r;++i)//一天运行r次
//		{
//			tmp=0;
//			while(tmp<=k && !wait.empty())
//			{
//				if(tmp+wait.front()>k)
//					break;
//				roller.push(wait.front());
//				tmp+=wait.front();
//				wait.pop();
//			}
//			//cout<<" tmp "<<tmp<<endl;
//			while(!roller.empty())
//			{
//				ans+=roller.front();
//				wait.push(roller.front());
//				roller.pop();
//			}
//		}
//		printf("%d\n",ans);
//	}
//	return 0;
//}
