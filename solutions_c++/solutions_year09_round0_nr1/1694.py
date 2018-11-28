//Pipe input file to program and pipe output of program to outfile

#include <stdio.h>
#include <map>
#include <string>
using namespace std;

#define debug 0
#define dprintf debug&&printf

char word[6000][32];
char test[1000];

int main(){
	int L,D,N;
	scanf("%d %d %d", &L, &D, &N);
	for(int i=0;i<D;i++){
		scanf("%s", word[i]);
	}
	for(int fall=0;fall<N;fall++){
		scanf("%s", test);

		int svar = 0;
		for(int i=0;i<D;i++){
			char* t = test;
			char* w = word[i];
			int ok = 1;
			do{
				if(*t == '('){
					int letterOk = 0;
					do{
						if(*t == *w){
							letterOk = 1;
						}
					}while(*++t != ')');
					if(!letterOk){
						ok = 0;
						break;
					}
				}else{
					if(*t != *w){
						ok = 0;
						break;
					}
				}
				++w;
			}while(*++t);
			svar += ok;
		}
		printf("Case #%d: %d\n", fall+1, svar);
	}
	return 0;
}
