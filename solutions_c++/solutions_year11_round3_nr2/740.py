#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;
int dis[20000];
void work(int x)
{
	long long l,t,n,c;
	long long ans = 0;
        printf("Case #%d: ",x);
		cin >> l >> t >> n >>c;
		for(int i = 0; i <c; i++){
			int tt;
			scanf("%d", &tt);
			for(int k = 0; k*c+i <n; k++)dis[k*c+i]= tt;
		}
		long long first = 0; 

		for(int i =0; i <n; i++)ans +=dis[i]*2;
		int i= 0;

		while(first<t && i < n)first += 2*dis[i++];
		if(first > t){
			i--;
			dis[i] = (first-t)/2;
		}
		if(i >=n){
			cout << ans << endl;
			return;
		}
		sort(dis+i, dis+n);
		int end;
		for(int j =1; j <=l && n-j >=i; j++){
			if(n-j >= end)ans-=dis[n-j];
		}
		cout << ans << endl;
}
int main()
{
        int t;
        scanf("%d",&t);
        for(int i = 1; i <= t; i++)work(i);
}
