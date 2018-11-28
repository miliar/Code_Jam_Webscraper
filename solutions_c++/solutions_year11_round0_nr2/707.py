#include<iostream>
#include<string>
#include<queue>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cases,c,d,n;
	char C[37][3];
	char D[29][2];
	char str[128];
	queue<char>que;
	scanf("%d",&cases);
	for(int cas = 1;cas <= cases; cas++)
	{
		scanf("%d",&c);
		for(int i=0;i<c;i++)scanf("%s",C[i]);
		scanf("%d",&d);
		for(int i=0;i<d;i++)scanf("%s",D[i]);
		scanf("%d",&n);
		scanf("%s",str);
		char ans[128];
		int cnt = 0;
		for(int i=0;i<n;i++){
			
			if(!cnt)ans[cnt++] =str[i];
			else{
				char last = str[i];
				for(int j=0;j<c;j++)
					if(cnt>0 && ((ans[cnt-1]==C[j][0]&&last==C[j][1])||ans[cnt-1]==C[j][1]&&last==C[j][0]))
				{
					cnt--;
					last = C[j][2];
				}
					for(int j=0;j<d;j++)if(cnt>0 && (last==D[j][0]||last==D[j][1]))
				{
					for(int k=0;k<cnt;k++)
						if((ans[k]==D[j][0]&&last == D[j][1])||(ans[k]==D[j][1]&&last == D[j][0]))
						{
							cnt = 0;
							last=' ';
						}
				}
				if(last!=' ')
					ans[cnt++] = last;
			}
		}
		printf("Case #%d: [",cas);
		for(int i=0;i<cnt;i++)
		{
			if(!i)printf("%c",ans[i]);
			else printf(", %c",ans[i]);
		}
		printf("]\n");
	}
}

//#include<iostream>
//using namespace std;
//int V[1024];
//int main()
//{
//	int cases,n;
//
//	scanf("%d",&cases);
//	for(int cas=1;cas<=cases;cas++)
//	{
//		scanf("%d",&n);
//		int sum = 0;
//		for(int i=0;i<n;i++)
//		{
//			scanf("%d",&V[i]);
//			sum = sum^V[i];
//		}
//		if(sum != 0 )printf("Case #%d: NO\n",cas);
//		else
//		{
//
//		}
//
//	}
//}