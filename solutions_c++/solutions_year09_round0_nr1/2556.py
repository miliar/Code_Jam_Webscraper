/*
 * 2009/09/02 21:57:47
 * */

#include <algorithm>
#include <string>
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

int main(){
	
	int l,d,n,x=1, letras[16][27],i,j;
	char temp[500],words[5001][16];
	
	scanf("%d %d %d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",words[i]);
	
	gets(temp);
	
	while(n--){
		gets(temp);
		
		//printf("string lida:%s\n",temp);
		
		memset(letras,0,sizeof(letras));
		
		//le a string anotando as possiveis entre cada letra[i] da palavra (token)
		int letraatual=0;
		int dentro=0;
		for(i=0;i<strlen(temp);i++){
			if(temp[i]=='('){
				dentro=1;
				continue;
			}
			else if( isalpha(temp[i]) ) {
				letras[letraatual][ temp[i]%96 ]=1;
				//printf("'%c' vale %d e letras[%d][%d]=1\n",temp[i],temp[i],letraatual,temp[i]%96);
			}
			else if(temp[i]==')'){
				dentro=0;
			}
			
			if(!dentro) letraatual++;
		}
		
		//verifica cada palavra se pode dar certo;
		int result=0;
		//varre em palavras
		for(i=0;i<d;i++){
			//varre em letras das palavras
			for(j=0;j<l;j++){
				if( letras[j][ words[i][j]%96 ] == 0 ) {
					//printf("letra '%c' da pos[%d] de '%s' eh 0\n",words[i][j],j,words[i]);
					break;
				}
			}
			if (j==l) result++; //se chegou ao fim soh com 1s no caminho
		}
		
		printf("Case #%d: %d\n",x,result);
		x++;
		
	}
	
	return 0;
}

