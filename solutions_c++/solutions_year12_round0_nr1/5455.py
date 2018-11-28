#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	
	FILE *f  = fopen(argv[1],"r");
	FILE *fop  = fopen("d:\\testgoo\\op.txt","w");
	char gooArr[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int T1;
	char T[6];
	fgets(T,6,f);
	T1 = atoi(T); 
	
	for (int i = 0; i < T1 || i < 30; i++){
		char G[105] = {'\0'};
		fgets(G,105,f);
		for (int j = 0; j < 105; j++){
			if (G[j] == NULL)
				break;
			if (G[j] == ' ')
				continue;
			int chara = G[j];
			if (chara>=97 && chara<=122)
			G[j] = gooArr[chara-97];
			else 
				G[j] = '\0';
		}
		fprintf(fop,"Case #%d: %s\n", i+1, G);
		
	}
	fclose(f);
	fclose(fop);
	return 0;
}