#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <stdio.h>
#include <map>

using namespace std;

int converte(char c){
	int atual;
	if(c>='0' && c<='9'){
		atual = c - '0';
	}
	else{
		atual = c - 'a' + 10;
	}
	return atual;
}

int main() {
	int n;
	char temp[1000];
	scanf("%d",&n);
	for(int k=0;k<n;k++){
		map<char,int> bases;
		scanf("%s",&temp);
		string numero(temp);

		bases[numero[0]]=1;
		int counter = 0;

		for(int i=0;i<numero.size();i++){

			//printf("Basesconv %d\n",bases[conv]);
			if(bases.find(numero[i])==bases.end()){
				bases[numero[i]]=counter;
		//		printf("Count %d %c",counter,numero[i]);
				counter = (counter==0)?2 :counter+1;

			}
		}
		if(counter==0){
			//bases[numero[0]]=2;
			counter = 2;
		}
		long long seq = 1;
		long long ans = 0;
		for(int i=numero.size()-1;i>=0;i--){

			ans += bases[numero[i]]*seq;
			//printf("bases[%c](%d)* seq(%d) = %lld\n",numero[i],bases[numero[i]],seq,ans);
			seq*=counter;
		}



		printf("Case #%d: %lld\n",k+1,ans);
	}
}
