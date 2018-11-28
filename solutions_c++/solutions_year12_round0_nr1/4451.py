#include <stdio.h>
#include <cstring>

int main(){
	char tmp, buf[102], alfa[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	int i, n, line = 1;
	scanf("%d ", &n);
	printf("Case #%d: ", line);
	while(line < (n+1)){
		if(scanf("%c", &tmp)==0)
			return 0;
		if(tmp == '\n'){
			printf("\n");
			line++;
			if(line<(n+1))
				printf("Case #%d: ", line);
			continue;
		}

		i = (tmp - 'a');
		if( i >= 0 && i <=25)
			tmp = alfa[i];
		printf("%c", tmp);
	}
	return 0;
}
