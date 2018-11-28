#include <stdio.h>
#include <string.h>


int main(void){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	//fflush(stdin);
	//FILE *ofp,*ifp;
	//ifp = fopen("A-small-attempt0.in","r");
	//ofp = fopen("A-small-attempt0.out","w+");
	int count=0;
	char input[35][110];
	int up=0;
	tt++;
	while(tt--){
		gets(input[count]);
		int len=strlen(input[count]);
		int j=0;
		while(len--){
			switch(input[count][j]){
				case 'a' : input[count][j] = 'y'; break;
				case 'b' : input[count][j] = 'h'; break;
				case 'c' : input[count][j] = 'e'; break;
				case 'd' : input[count][j] = 's'; break;
				case 'e' : input[count][j] = 'o'; break;
				case 'f' : input[count][j] = 'c'; break;
				case 'g' : input[count][j] = 'v'; break;
				case 'h' : input[count][j] = 'x'; break;
				case 'i' : input[count][j] = 'd'; break;
				case 'j' : input[count][j] = 'u'; break;
				case 'k' : input[count][j] = 'i'; break;
				case 'l' : input[count][j] = 'g'; break;
				case 'm' : input[count][j] = 'l'; break;
				case 'n' : input[count][j] = 'b'; break;
				case 'o' : input[count][j] = 'k'; break;
				case 'p' : input[count][j] = 'r'; break;
				case 'q' : input[count][j] = 'z'; break;
				case 'r' : input[count][j] = 't'; break;
				case 's' : input[count][j] = 'n'; break;
				case 't' : input[count][j] = 'w'; break;
				case 'u' : input[count][j] = 'j'; break;
				case 'v' : input[count][j] = 'p'; break;
				case 'w' : input[count][j] = 'f'; break;
				case 'x' : input[count][j] = 'm'; break;
				case 'y' : input[count][j] = 'a'; break;
				case 'z' : input[count][j] = 'q'; break;
				case ' ' : input[count][j] = ' '; break;
				case 10 : break; 
				default : break;
			}

			j++;
		}
		if(count){
			printf("Case #%d: %s \n",count,input[count]);

		}
	//	fprintf(ofp,"Case #%d: %s \n",count,input[count]);
		count++;
		up=0;
	}
	return 0;
}	