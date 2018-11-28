#include <iostream>

using namespace std;
long long ans,e[20];

int T,L,R,len;
int a[20];


int smaller(int i, int j) {
	return i<j;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);
	
	scanf("%d",&T);
	for (int ttt=1; ttt<=T; ttt++)
	{
		scanf("%d%d",&L,&R);
		printf("Case #%d: ",ttt);
		ans=0;
		e[0]=1;
		for (int i=1; i<=10; i++) e[i]=e[i-1]*10;
		for (len=1; len<=10; len++) if (L<e[len]) break; 
	//	printf("len : %d ",len);
		for (int i=L; i<R; i++)
		{
			int x=i,y=0,m;
			int cnt=0;
			for (int j=0; j<len; j++)
			{
				y = y+ e[j]*(x%10);
				x = x/10;				
				m = y*e[len-j-1]+x;
			//	printf("(%d , %d) ",i,m);
				if (smaller(i,m) && smaller(m,R+1)) {
					a[cnt++]=m;
				}				
			}
			for (int j=0; j<cnt; j++)
			{
				int ok=1;
				for (int jj=0;jj<j;jj++) if (a[jj]==a[j]) { ok=0; break; }
				ans+=ok;
			}
		}
		cout << ans<<endl;
	}
}