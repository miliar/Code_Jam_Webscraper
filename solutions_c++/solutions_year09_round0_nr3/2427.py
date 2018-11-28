
/*
 * 2009/09/02 20:28:51
 * 
 * */
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue> 
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <list>
#include <stack>
#include <cctype>

#define sb substr
#define st string
#define db double
#define rt return
#define fr(i,b) for((i) = 0; (i) < (b); i++)
#define fs(i,a,b) for((i) = (a); (i) < (b); i++)
#define cl clear
#define sz size
#define mm(a) memset(a,0,sizeof(a))
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pii pair<int,int>
#define all(c) (c).begin(), (c).end()
#define Sort(c) sort(all(c))
#define mp make_pair
#define fi first
#define sc second
#define stg(ss)  stringstream ss; ss.cl(); ss.str("");
#define LIM  1000001
#define LIM2 1000001

using namespace std;

int tam1,tam2,conta;
char vetor[4], texto[1000], source[]="welcome to code jam";
vector<char> temp;

void incrementa(){
	int i=3,vaium=0;
	
	while(i>=0){
		if(vaium){
			if( vetor[i] == '9'){
				vetor[i]='0';
				vaium=1;
			}
			else{
				vetor[i]++;
				vaium=0;
			}
		}
		else{
			if( vetor[i] == '9'){
				vetor[i]='0';
				vaium=0;
			}
			else{
				vetor[i]++;
				vaium=0;
				return;
			}
		}
			
		i--;
	}
	
	return;
}

int acha_letra(char letra, int posicao, int nivel){
	if (nivel == tam2) {
		incrementa();
		//conta++;
		//printf("<<<<\n");
		return 1;
	}
	else
		for(int i=posicao;i<tam1;i++){
			if(texto[i]==letra){
				//printf("%c",texto[i]);
				acha_letra( source[nivel+1],i+1,nivel+1 );
			}
		}
		
	return 0;
}

int main(){
	int x=1,n;
	
	
	scanf("%d",&n);
	
	gets(texto);
	while(n--){
		gets(texto);
		conta=0;
		//printf("string lida: --%s--\n",texto);
		
		memset(vetor,'0',sizeof(vetor));
		
		temp.clear();
		
		//testar a funcao incrementa 
		/*for (int i=0;i<10001;i++){
			printf("%s\n",vetor);
			incrementa();
		}*/
		
		tam1=strlen(texto);
		tam2=strlen(source);
		
		//for(int j=0;j<tam1-tam2;j++){
			acha_letra(source[0],0,0);
		//}
		
		printf("Case #%d: %s\n",x,vetor,conta);
		x++;
		
	}
	
	return 0;
}

