#include<iostream>

using namespace std;

int num[2000];
int bin[2000][100];
int count[100];
int maxp;

void getbin(int val, int index){
	int p = 0;
	while(val!=0){
		bin[index][p] = val%2;
		if(val%2==1){
			count[p] ++;
		}
		p++;
		val /=2;
	}
	maxp = max(p, maxp);
}
int compare (const void * a, const void * b) 
{  
	return ( *(int*)b - *(int*)a );
}

int main(){
	int cs,n, ans;
	cin>>cs;
	freopen("C.out","w",stdout);
	for(int css=1;css<=cs;css++){
		cin>>n;
		memset(count,0,sizeof(count));
		maxp = -1;
		for(int i=0;i<n;i++){
			int k;
			cin>>k;
			num[i] = k;	
		}
		qsort(num, n, sizeof(int), compare);
		ans = 0;
		for(int i=0;i<n;i++) 
		{
			ans += num[i]; 
			getbin(num[i], i);
		}
		
		for(int i=maxp-1;i>=0;i--)
		{
			if(count[i]%2==1){
				ans = -1;
				break;
			}
		}
		if(ans==-1){
			printf("Case #%d: NO\n", css);
		}else
		{
			ans -= num[n-1];
			printf("Case #%d: %d\n", css,ans);
		}
		
	}
	return 0;
}