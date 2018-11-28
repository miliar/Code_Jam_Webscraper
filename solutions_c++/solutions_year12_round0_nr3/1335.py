#include<cstdio>

using namespace std;

int i , j , t , t_case , ans , pows[10] , A , B;

int ret(int x) {
	
	int len = 0 , ans = 0, i , tmp;
	
	for(tmp = x; tmp;) {
		tmp /= 10;
		len++;
	}
	
	for(tmp = x, i = 1; i < len; ++i) {
		
		int c = tmp % 10;
		tmp /= 10; tmp += pows[len - 1] * c;
		if(tmp == x) 
			return ans;
		ans += (tmp > x && tmp <= B);
	}

return ans;
}
	

int main()
{
	freopen("recycled.in","r",stdin);
	freopen("recycled.out","w",stdout);
	
	scanf("%d",&t);
	
	pows[0] = 1;
	for(i = 1; i <= 6; ++i)
		pows[i] = pows[i - 1] * 10;
	
	for(t_case = 1; t_case <= t; ++t_case) {
		
		ans = 0;
		scanf("%d %d",&A,&B); 
		
		ret(1212);
		
		for(i = A; i <= B; ++i) {
			//printf("%d %d\n",i,ret(i));
			ans += ret(i);
		}
		
		printf("Case #%d: %d\n",t_case,ans);
	}
	
return 0;
}