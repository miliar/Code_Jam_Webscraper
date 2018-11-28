#include<cstdio>
#include<conio.h>
#include<algorithm>
using namespace std;

int main(){
	int tc;
	scanf("%d",&tc);
for(int z=0;z<tc;z++){
    int keypad[100][1001],angka[1001];
	int P,K,L,pos,total;
	scanf("%d %d %d",&P,&K,&L);
	for(int i=0;i<L;i++){
	  scanf("%d",&angka[i]);		
	}
	sort(angka,angka+L);
	
	total = 0;
	pos = 0;
	for(int i=L-1;i>=0;i--){
	  total += angka[i] * ((pos/K) +1);
	  pos++; 			
	}
	printf("Case #%d: %d\n",(z+1),total);	
}
	
return 0;	
}
