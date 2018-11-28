#include <stdio.h>
#include <queue>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <map>

#define MALTED   1
#define UNMALTED 2
using namespace std;


int isSatisfied( vector<int> customer, vector<int> shake){
	int satisfied = 0;
	for(int i=0;i<customer.size();i++){
		if(customer[i]==shake[i])
			satisfied++;
	}
	//printf("Satisfied %d\n",satisfied);
	if(satisfied)
		return 1;
	else
		return 0;
	
	
}
vector<int> buildShake(int num, int n){
	vector<int> ans;
	for(int i=0;i<n;i++){
		if(num & 1){
			ans.push_back(MALTED);
		}
		else{
			ans.push_back(UNMALTED);
		}
		num = num >> 1;
	}
	return ans;
}
int getMaltedCount(vector<int> shake){
	int ans = 0;
	for(int i=0;i<shake.size();i++){
		if(shake[i]==MALTED) ans++;
	}
	return ans;
}
void printShake(vector<int> shake){
	for(int i=0;i<shake.size();i++){
		//printf("%d ",shake[i]);
		
		if(shake[i]==MALTED)
			printf("1 ");
		else
			printf("0 ");
	}
	
}
int main(){
	int cases;
	scanf("%d",&cases);
	for(int k=0;k<cases;k++){
		int n;
		scanf("%d",&n);
		int m;
		scanf("%d",&m);
		vector< vector<int> > customers;
		for(int i=0;i<m;i++){
			int numMilk;
			vector<int> atual;
			for(int j=0;j<n;j++)
				atual.push_back(0);
			
			scanf("%d",&numMilk);
			int cMilk=0;
			for(int j=0;j<numMilk;j++){
				int x,y;
				scanf("%d%d",&x,&y);
				if(y){
					atual[x-1]=MALTED;
				}
				else{
					atual[x-1]=UNMALTED;
				}				
			}
			//printf("cMilk(%d): %d\n",i,cMilk);
			customers.push_back(atual);
		}
		int menorIndex = -1;
		int menorValor = 10000;
		int impossible = 1;
		vector<int> menorShake;
		for(int i=0;i< (1<<n);i++){
			vector<int> shake = buildShake(i,n);
			//printf("Built shake ");
			//printShake(shake);
			int numSatisfied = 0;
			for(int j=0;j<m;j++){
				numSatisfied+= isSatisfied(customers[j],shake);
			}
			if(numSatisfied==m){
				//printf("Shake ");
				//printShake(shake);
				impossible=0;
				int shakeCount =getMaltedCount(shake); 
				if(shakeCount<menorValor){
					menorValor = shakeCount;
					menorShake = shake;
				}
			}
		}
		printf("Case #%d: ",k+1);
		if(impossible){
			printf("IMPOSSIBLE");
		}
		else{
			printShake(menorShake);
		}
		printf("\n");
		//printf("Menor Valor %d\n",menorValor);
	}
	
}