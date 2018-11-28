#include<stdio.h>
#include<iostream>
#include<string>
#include<sstream>
using namespace std;
int a[20];
char mark[11][13000010];
char tp[11][13000010];
void fill(int bas,int tar) {
	int t=tar,ans;
			while (1) {
				ans=0;
				tp[bas][t]=2;
				while (t) {
					ans+=(t%bas)*(t%bas);
					t/=bas;
				}
				//if (tp[bas][ans]==1) break;
				if (ans==1) {mark[bas][tar]=1;break;}
				t=ans;
			}
}
int main()
{
	int nn,t;
	char ts[5];
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&nn);
	gets(ts);
	int ans;
	for (int bas=2;bas<=10;bas++) {
		mark[bas][1]=1;
		for (int i=2;i<=13000000;i++) {
			//if (i%1000000==0) printf("%d %d\n",bas,i);
		//	memset(tp,0,sizeof(tp));
			t=i;
			if (tp[bas][t]==2) {mark[bas][i]=1;continue;}
			while (1) {
				ans=0;
				//if (tp[bas][t]==2) {mark[bas][i]=1;break;}
				tp[bas][t]=1;
				
				while (t) {
					ans+=(t%bas)*(t%bas);
					t/=bas;
				}
				if (tp[bas][ans]==1) break;
				if (ans==1||tp[bas][i]==2) {
					mark[bas][i]=1;fill(bas,i);break;}
				t=ans;
			}
			//printf("%d ",i);
		}
	}
	for (int ii=1;ii<=nn;ii++) {
		printf("Case #%d: ",ii);
		int n=0,t;
		string s;
		getline(cin,s);
		istringstream ss(s);
		while (ss>>t) {
			a[++n]=t;
		}
		if (n==2) {
			int ans=0;
			for (int i=2;i<=13000000;i++) if (mark[a[1]][i]&&mark[a[2]][i]) {ans=i;break;}
			printf("%d\n",ans);
		}
		else if (n==3) {
			int ans=0;
			for (int i=2;i<=13000000;i++) if (mark[a[1]][i]&&mark[a[2]][i]&&mark[a[3]][i]) {ans=i;break;}
			printf("%d\n",ans);
		}
		else {
			int ans=0;
			for (int i=2;i<=13000000;i++) {
				int ok=1;
				for (int j=1;j<=n;j++) if (mark[a[j]][i]==0) {ok=0;break;}
				if(ok) {ans=i;break;}
			}
			printf("%d\n",ans);
		}
	}
}
