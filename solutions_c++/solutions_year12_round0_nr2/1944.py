#include <iostream>
#include <algorithm>
using namespace std;
int dd[1024];
int s,p,n;

void input(){
	scanf("%d %d %d",&n,&s,&p);
	
	for (int i = 0; i < n; i++)
	{
		scanf("%d",dd+i);
	}

}

bool cmp(const int a,const int b){
	return a > b;
}

int solve(){
	int lim = (p - 1)*2+p;//不特殊情况
	int lim2 = (p - 2)*2 + p;//特殊情况
	int i,ans = 0,ii = 0;
	sort(dd,dd+n,cmp);

	 if (p == 0)
	 {
		 lim = lim2 = 0;
	 }
	 else if (p == 1)
	 {
		 lim = 1;
		 lim2 =1;
	 }

	for (i = 0; i < n; i++)
	{
		if (dd[i] >= lim)
		{
			ans++;
		}
		else break;
	}
	for (ii = 0; i < n && ii < s; i++){
		if (dd[i] >= lim2)
		{
			ii++;
			ans++;
		}
		else break;
	}
	return ans;
	
}

int main(){
	int nCase;
	int ans;
	//	freopen("d:/2.in","r",stdin);
	//	freopen("d:/2.out","w",stdout);
	while (scanf("%d",&nCase) != EOF)
	{
		for (int i = 1; i <= nCase; i++)
		{
			input();
			printf("Case #%d: ",i);
			ans = solve();
			printf("%d\n",ans);
		}
	}
	return 0;
}