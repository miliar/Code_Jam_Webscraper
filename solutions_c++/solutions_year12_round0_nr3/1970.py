#include<cstdio>
#include<cstring>
#include<set>
using namespace std;

int count(int a, int B){
	char s[10];
	set<int> S;
	sprintf(s,"%d",a);
	int n = strlen(s);
	for(int i = n-1;i>0;i--){
		int b = 0;
		for(int j=i;j<n;j++){
			b *= 10;
			b += s[j]-'0';
		}
		for(int j=0;j<i;j++){
			b *= 10;
			b += s[j]-'0';
		}
		if(b>a && b<=B)
			S.insert(b);
	}
	return (int)S.size();
}

int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		int a,b, ans=0;
		scanf("%d %d",&a,&b);
		for(int i = a;i<b;i++)
			ans += count(i,b);
		printf("Case #%d: %d\n",caso,ans);
	}
	return 0;
}
