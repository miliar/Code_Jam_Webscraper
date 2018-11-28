#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <stdio.h>
#include <map>
#include <queue>

using namespace std;

//map<string,int> visitado;
int ordem(string str){
	int l=str.length();
	for(int i=0;i<l;i++){
		if(str[l-1-i]=='1')
			return i;
	}
}
int correct(vector<int> pos){
	int n = pos.size()-1;
	for(int i=0;i<n;i++){
		if(pos[i]<n-i-1){
		//	printf("incor %d\n",i);
			return 0;
		}
	}
	return 1;
}

vector<int> troca(vector<int> vetor, int pos){
	vector<int> ans;
	for(int i=0;i<vetor.size();i++){
		ans.push_back(vetor[i]);
	}
	int temp = ans[pos];
	ans[pos]=ans[pos+1];
	ans[pos+1]=temp;
	return ans;
}

int main() {
	int t;
	scanf("%d",&t);
	for(int k=0;k<t;k++){
		int n;
		scanf("%d",&n);
		map< string, int> visitado;
		vector<int> prob;

		for(int i=0;i<n;i++){
			char temp[100];
			scanf("%s",&temp);
			prob.push_back(ordem(string(temp)));
		}

		queue< vector<int> > fila;
		prob.push_back(0);
		fila.push(prob);
		int ans = 0;
		while(1){
			vector<int> topo = fila.front();
			int n = topo.size()-1;
			//verificar visitado
			char temp[400];
			for(int i=0;i<n;i++){
				temp[i] = '0'+topo[i];
			}
			string teste(temp);
			if(visitado.find(temp)==visitado.end()){
				visitado[teste]=1;
			}
			else{
				fila.pop();
				continue;
			}

			//printf("Teste %s\n",teste.c_str());


			/*printf("Topo\n");
			for(int i=0;i<topo.size();i++)
				printf("%d ",topo[i]);*/
			fila.pop();
			if(correct(topo)){
				ans = topo[topo.size()-1];
				break;
			}

			//gerar filhos
			for(int i=0;i<n-1;i++){
				vector<int> filho = troca(topo,i);
				filho[filho.size()-1] = topo[filho.size()-1]+1;
				fila.push(filho);
			}
		}

		/*printf("Prob %d\n",correct(prob));
		for(int i=0;i<n;i++)
			printf("%d ",prob[i]);
		printf("\n");*/

		printf("Case #%d: %d\n",k+1,ans);


	}


	return 0;
}
