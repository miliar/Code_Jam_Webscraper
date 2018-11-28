#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int main(){
	int nteste;
	scanf("%d",&nteste);
	
	for(int nt=1;nt <= nteste;nt++){
		printf("Case #%d: ",nt);
		
		int n,s,p,i,resp=0,total;
		scanf("%d %d %d",&n,&s,&p);
		
		for(i=0;i<n;i++){
			scanf("%d",&total);
			if(total >= 2*max((p-1),0) + p){ resp++; }
			else if(s!=0 && total >= 2*max(0,(p-2)) + p){
				resp++;
				s--;
			}
		}
		
		printf("%d\n",resp);
		
	}
}
