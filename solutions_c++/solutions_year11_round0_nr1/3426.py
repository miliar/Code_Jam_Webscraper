#include<cstdio>
#include<iostream>
using namespace std;
int c[2000];
int n;
char w[1000];
int p[1000];
int nexto(int x){
	for(int i = x; i< n; i++)if(w[i]=='O')return p[i];
	return 1000;
}
int nextb(int x)
{
	for(int i = x; i< n; i++)if(w[i]=='B')return p[i];
	return 1000;
}

void work(int x)
{
	int nowp, time, po, pb;
	printf("Case #%d: ",x);
	cin >> n;
	for(int i = 0; i < n; i++)cin >> w[i] >> p[i];
	nowp = 0; 
	time = 0;
	po = 1;
	pb = 1;
	while(nowp <n){

//		printf("%d\n",nowp);
		int temp =nowp;
		if(w[nowp] == 'O' && po == p[nowp]){
			temp++;
		}else if(po < nexto(nowp)){
			po++;
		}
		else if(po > nexto(nowp)){
			po--;
		}
		
		if(w[nowp] == 'B' && pb == p[nowp]){
			temp++;
		}
		else if (pb < nextb(nowp)) pb ++;
		else if(pb > nextb(nowp))pb--;
		nowp = temp;
		time++;
	}
	printf("%d\n",time);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)work(i);
}
