#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int main()
{
	//freopen("entrada.txt","r",stdin);
	//freopen("salida.txt","w",stdout);

	int casos;
	scanf("%d",&casos);
	vector < pair<char,int> > secuencia;
	vector <int> objO,objB;
	for(int i=0;i<casos;++i){
		char basura,basura2;
		int tamSecuencia;
		scanf("%d",&tamSecuencia);
		for(int j=0; j<tamSecuencia;++j){
			char auxChar;
			int auxInt;
			scanf("%c%c%c%d",&basura,&auxChar,&basura2,&auxInt);
			secuencia.push_back( pair<char,int>(auxChar,auxInt));
			(auxChar=='O')? objO.push_back(auxInt):objB.push_back(auxInt);
		}
		reverse(secuencia.begin(),secuencia.end());
		reverse(objB.begin(),objB.end());
		reverse(objO.begin(),objO.end());
		int pasos=0;
		int actO=1,actB=1;
		while(!secuencia.empty()){
			//presiono O
			pair<char,int> actButton = secuencia.back();
			bool yaO =false,yaB=false;
			//presiono para O
			if(!objO.empty()){
				if(actButton.first=='O' && actButton.second==actO){
					yaO=true;objO.pop_back();
				}else{
					int proxO = objO.back();
					if(!yaO && actO!=proxO){
						(actO<proxO)? actO++: actO--;
					}
				
				}
			}
			if(!objB.empty()){	
			 if(actButton.first=='B' && actButton.second==actB){
					yaB=true;objB.pop_back();
				}else{
					int proxB = objB.back();
					if(!yaB && actB!=proxB){
						(actB<proxB)? actB++: actB--;
					}
				
				}
			}
			//desapilo secuencia si alguno presiono
			if(yaB || yaO){
				secuencia.pop_back();
			}
			pasos++;
		}
	
		printf("Case #%d: %d\n",(i+1),pasos);
	}
	

return 0;
}
