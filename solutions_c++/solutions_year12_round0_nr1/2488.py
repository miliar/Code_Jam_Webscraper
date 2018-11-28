#include <stdio.h>
#include <string.h>

char tab[] = {'y', 'h', 'e', 's', 'o',
              'c', 'v' , 'x', 'd', 'u', 'i',
              'g', 'l', 'b', 'k', 'r',
              'z',  't', 'n', 'w', 'j',
              'p', 'f', 'm', 'a', 'q'};

int main() {
	int t;
	scanf("%d\n", &t);
	
	for(int z=1; z<=t; z++) {
		char linia[200];
		scanf("%[^\n]\n", linia);
		//printf("%s\n", linia);
		
		int l = strlen(linia);
		for(int i=0; i<l; i++)
			if(linia[i]<='z' && linia[i]>='a')
				linia[i] = tab[ linia[i]-'a'];
		printf("Case #%d: %s\n", z, linia);
		
		
	}
	
	return 0;
}
