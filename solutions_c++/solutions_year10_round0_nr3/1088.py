#include<iostream>
#include<queue>
using namespace std;
int main(){
	FILE *in=fopen("C-small-attempt0.in","r"),*out=fopen("C-small-attempt0.out","w");
	int T,R,k,n;
	fscanf(in,"%d",&T);
	for(int i=1;i<=T;i++){
		fscanf(in,"%d%d%d",&R,&k,&n);
		queue<int> Q,P;
		int t,p=0;
		long long sum=0;
		for(int j=0;j<n;j++){
			fscanf(in,"%d",&t);
			Q.push(t);
		}
		while(R>0){
			while(p+Q.front()<=k&&!Q.empty()){
				p+=Q.front();
				sum+=Q.front();
				P.push(Q.front());	
				Q.pop();
			}
			R--;
			p=0;
			while(!P.empty()){
				Q.push(P.front());
				P.pop();	
			}
		}
		printf("Case #%d: %I64d\n",i,sum);
		fprintf(out,"Case #%d: %I64d\n",i,sum);
	}
	system("pause");
	return 0;
}
