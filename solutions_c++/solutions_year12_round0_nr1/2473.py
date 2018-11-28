#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cmath>

using namespace std;


char dic[500], linha2[500], linha[500];

int main(){
	dic['a'] = 'y'; dic['b'] = 'h'; dic['c'] = 'e'; dic['d'] = 's'; dic['e'] = 'o'; 
	dic['f'] = 'c'; dic['g'] = 'v'; dic['h'] = 'x'; dic['i'] = 'd'; dic['j'] = 'u'; 
	dic['k'] = 'i'; dic['l'] = 'g'; dic['m'] = 'l'; dic['n'] = 'b'; dic['o'] = 'k'; 
	dic['p'] = 'r'; dic['q'] = 'z'; dic['r'] = 't'; dic['s'] = 'n'; dic['t'] = 'w'; 
	dic['u'] = 'j'; dic['v'] = 'p'; dic['w'] = 'f'; dic['x'] = 'm'; dic['y'] = 'a'; dic['z'] = 'q';
	dic[' '] = ' ';
	int casos; scanf("%d", &casos); gets(linha);
	int caso = 0;
	while(casos--){ ++ caso;
		gets(linha);
		for(int i = 0; linha[i]; ++i){
			linha[i] = dic[linha[i]];
		}
		
		printf("Case #%d: %s\n", caso, linha);
	}
	
	return 0;
}