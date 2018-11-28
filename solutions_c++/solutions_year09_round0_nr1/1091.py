#include<algorithm>
#include<iostream>
#include<math.h>
#include<map>
#include<string>
using namespace std;
#define memo(a,b) memset(a,b,sizeof(a))


int L,D,N;
char a[5005][100],b[10000];
bool dic[20][50];
int main(){
//	freopen("A.in","r",stdin);
//	freopen("A.ans","w",stdout);
	int i,j,flag,cs=1,k,cnt;
	
	while(scanf("%d %d %d",&L,&D,&N)==3){

		
		for(i=0;i<D;i++){
			scanf("%s",a[i]);
		}
		for(i=0;i<N;i++){
			scanf("%s",b);
			for(j=0;j<L;j++) {
				memo(dic[j],0);
			}
			for(j=0,k=0,flag=0;b[j];j++){
				if(b[j]=='('){
					flag=1;
				}
				else if(b[j]==')'){
					
					k++;
					flag=0;
					
				}
				else if(flag){
					dic[k][b[j]-97]=1;
				}
				else{
					dic[k][b[j]-97]=1;
					k++;
				}
			}
			for(j=0,cnt=0;j<D;j++){
				for(k=0;k<L;k++){
					if(!dic[k][a[j][k]-97]) break;
				}
				if(k==L) cnt++;
			}
			printf("Case #%d: %d\n",cs++,cnt);
		}
	}
	return 0;
}