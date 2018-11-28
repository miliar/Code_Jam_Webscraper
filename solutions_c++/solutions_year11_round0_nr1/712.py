#include<iostream>
#include<algorithm>
using namespace std;
#define max(a,b) (a)>(b)?(a):(b)

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cases,n,m;
	char str[2];
	cin>>cases;
	for(int cas=1;cas<=cases;cas++)
	{
		cin>>n;
		int curB = 1,curO = 1;
		int lastBT = 0,lastOT = 0,ansT = 0;
		char lastState = 'X';
		for(int i=0;i<n;i++)
		{
			scanf("%s%d",str,&m);
			if(str[0]=='O'){
				if(lastState == 'X' || lastState == 'O'){
					int tmp = abs(m - curO) + 1;
					ansT += tmp;
					lastOT += tmp;
				}
				else if(lastState == 'B'){
					int tmp = abs(m - curO);
					if(tmp>lastBT){
						ansT += (tmp - lastBT) + 1;
						lastOT = (tmp - lastBT) + 1;
						lastBT = lastBT - tmp -1;
					}
					else{
						ansT += 1;
						lastOT = 1;
						lastBT = 0;
					}
					
				}
				lastState = 'O';
				curO = m;
			}
			else{
				if(lastState == 'X' || lastState == 'B'){
					int tmp = abs(m - curB) + 1;
					ansT += tmp;
					lastBT += tmp;
				}
				else if(lastState == 'O'){
					int tmp = abs(m - curB);
					if(tmp>lastOT){
						ansT += (tmp - lastOT) + 1;
						lastBT = (tmp - lastOT) + 1;
						lastOT = lastOT - tmp -1;
					}
					else{
						ansT += 1;
						lastBT = 1;
						lastOT = 0;
					}
					
				}
				lastState = 'B';
				curB = m;
			}
		}
		printf("Case #%d: %d\n",cas,ansT);
	}
}
//#include<iostream>
//#include<string>
//#include<queue>
//using namespace std;
//int main()
//{
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-attempt0.out","w",stdout);
//	int cases,c,d,n;
//	char C[36][3];
//	char D[28][2];
//	char str[128];
//	queue<char>que;
//	scanf("%d",&cases);
//	for(int cas = 1;cas <= cases; cas++)
//	{
//		scanf("%d",&c);
//		for(int i=0;i<c;i++)scanf("%s",C[i]);
//		scanf("%d",&d);
//		for(int i=0;i<d;i++)scanf("%s",D[i]);
//		scanf("%d",&n);
//		scanf("%s",str);
//		char ans[128];
//		int cnt = 0;
//		for(int i=0;i<n;i++){
//			
//			if(!cnt)ans[cnt++] =str[i];
//			else{
//				char last = str[i];
//				for(int j=0;j<c;j++)
//					if(cnt>0 && ((ans[cnt-1]==C[j][0]&&last==C[j][1])||ans[cnt-1]==C[j][1]&&last==C[j][0]))
//				{
//					cnt--;
//					last = C[j][2];
//				}
//					for(int j=0;j<d;j++)if(cnt>0 && (last==D[j][0]||last==D[j][1]))
//				{
//					for(int k=0;k<cnt;k++)
//						if((ans[k]==D[j][0]&&last == D[j][1])||(ans[k]==D[j][1]&&last == D[j][0]))
//						{
//							cnt = k-1;
//							last=' ';
//							if(cnt<0)cnt = 0;
//						}
//				}
//				if(last!=' ')
//					ans[cnt++] = last;
//			}
//		}
//		printf("Case #%d: [",cas);
//		for(int i=0;i<cnt;i++)
//		{
//			if(!i)printf("%c",ans[i]);
//			else printf(", %c",ans[i]);
//		}
//		printf("]\n");
//	}
//}

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