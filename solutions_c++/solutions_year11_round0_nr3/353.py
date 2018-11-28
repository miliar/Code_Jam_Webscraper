// gcj C
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<map>
#include<string>
#include<cmath>
#include<set>
using namespace std;
const int MAX=1000000+10;

int a[MAX],N;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int T;scanf("%d",&T);
	int CN=0;
	
	while(T--)
	{
		scanf("%d",&N);
		for(int i=1;i<=N;i++) scanf("%d",&a[i]);
		sort(&a[1],&a[N+1]);
		
		int tmp=0,total=0;
		for(int i=1;i<=N;i++) total+=a[i];
		for(int i=1;i<=N;i++) tmp=tmp^a[i];
		
		printf("Case #%d: ",++CN);
		
		if(tmp!=0) printf("NO\n");
		else printf("%d\n",total-a[1]);
	}
	
	return 0;
}
