#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
using namespace std;
int T,n,i,j,x,but,cntO,cntB,cnt,posO,posB,curO,curB,ans,temp;
char ch;
int O[202][2];
int B[202][2];
int main()
{
	freopen("data.in", "r", stdin);
	freopen("data.out", "w+", stdout);\
	scanf("%d",&T);
	//while (scanf("%d",&T)!=EOF) {
		for(i=1;i<=T;i++) {
			scanf("%d",&n);getchar();
			cntO=cntB=cnt=0;
			memset(O,0,sizeof(O));
			memset(B,0,sizeof(B));
			for(j=0; j<n; j++) {
				scanf("%c %d",&ch,&but);getchar();
				if(ch=='O') {
					O[cntO][0]=but;
					O[cntO][1]=cnt;
					cntO++;
				}
				if(ch=='B') {
					B[cntB][0]=but;
					B[cntB][1]=cnt;
					cntB++;
				}
				cnt++;
			}
			posO=1;posB=1;
			curO=curB=ans=0;
			for(x=0;x!=cnt;x++) {
				if (curO<cntO && O[curO][1]==x) {
					temp=abs(O[curO][0]-posO)+1;
					ans+=temp;
					posO=O[curO][0];
					curO++;
					for(j=0;j<temp;j++)
					{
						if(posB<B[curB][0]) 
							posB++;
						else if(posB>B[curB][0])
							posB--;
						else break;
					}
				}
				if (curB<cntB && B[curB][1]==x) {
					temp=abs(B[curB][0]-posB)+1;
					ans+=temp;
					posB=B[curB][0];
					curB++;
					for(j=0; j<temp; j++)
					{
						if(posO<O[curO][0])
							posO++;
						else if(posO>O[curO][0])
							posO--;
						else break;
					}
				}
			}
			printf("Case #%d: %d\n",i,ans);
		}
	//}
	return 0;
}