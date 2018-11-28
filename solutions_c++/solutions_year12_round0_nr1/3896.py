#include <cstdio>
#include <cstring>
using namespace std;

int main(){
	int n; scanf("%d\n",&n);
	for(int tc = 1 ; tc <= n; tc++){
		char kal[105]; scanf("%[^\n]\n",kal);
		int len = strlen(kal);
		for(int i = 0; i<len; i++){
			switch(kal[i]){
				case 'a' : kal[i]='y'; break;
				case 'b' : kal[i]='h'; break;
				case 'c' : kal[i]='e'; break;
				case 'd' : kal[i]='s'; break;
				case 'e' : kal[i]='o'; break;
				case 'f' : kal[i]='c'; break;
				case 'g' : kal[i]='v'; break;
				case 'h' : kal[i]='x'; break;
				case 'i' : kal[i]='d'; break;
				case 'j' : kal[i]='u'; break;
				case 'k' : kal[i]='i'; break;
				case 'l' : kal[i]='g'; break;
				case 'm' : kal[i]='l'; break;
				case 'n' : kal[i]='b'; break;
				case 'o' : kal[i]='k'; break;
				case 'p' : kal[i]='r'; break;
				case 'q' : kal[i]='z'; break;
				case 'r' : kal[i]='t'; break;
				case 's' : kal[i]='n'; break;
				case 't' : kal[i]='w'; break;
				case 'u' : kal[i]='j'; break;
				case 'v' : kal[i]='p'; break;
				case 'w' : kal[i]='f'; break;
				case 'x' : kal[i]='m'; break;
				case 'y' : kal[i]='a'; break;
				case 'z' : kal[i]='q'; break;
			}
		}
		printf("Case #%d: %s\n",tc,kal);
	}
	return 0;
}