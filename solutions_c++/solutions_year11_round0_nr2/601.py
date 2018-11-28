#include <stdio.h>
#include <string.h>

int nr,np,len;
int top;
char input[110];
char trans[10][10];
char oppo[10][10];
char stack[110];

int toChar(char a) {
	if(a == 'Q')	return 0;
	else if(a == 'W')	return 1;
	else if(a == 'E')	return 2;
	else if(a == 'R')	return 3;
	else if(a == 'A')	return 4;
	else if(a == 'S')	return 5;
	else if(a == 'D')	return 6;
	else if(a == 'F')	return 7;
	else return 8;
}

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		memset(trans,0,sizeof(trans));
		memset(oppo,0,sizeof(oppo));
		scanf("%d",&nr);
		for(int i=0;i<nr;++i) {
			char tp[10];
			scanf("%s",tp);
			trans[toChar(tp[0])][toChar(tp[1])] = trans[toChar(tp[1])][toChar(tp[0])] = tp[2];
		}
		
		scanf("%d",&np);
		for(int i=0;i<np;++i) {
			char tp[10];
			scanf("%s", tp);
			oppo[toChar(tp[0])][toChar(tp[1])] = oppo[toChar(tp[0])][toChar(tp[1])] = 1;
		}
		scanf("%d",&len);
		scanf("%s",input);
		
		//printf("%d %d %d\n",nr,np,len);
		
		top = 0;
		for(int i=0;i<len;++i) {
			if(top <= 0) {
				stack[top++] = input[i];
				continue;
			}
			
			if(trans[toChar(stack[top-1])][toChar(input[i])]) {
				stack[top-1] = trans[toChar(stack[top-1])][toChar(input[i])];
			} else {
				stack[top++] = input[i];
				for(int k=0;k<top;++k) {
					bool flag = false;
					for(int j=0;j<top;++j)
						if( k != j && oppo[toChar(stack[k])][toChar(stack[j])] ) {
							top = 0;
							flag = true;
							break;
						}
					if(flag)	break;
				}
			}
		}
		//printf("%d\n",top);
		
		printf("Case #%d: [",++c);
		if(top > 0) {
			printf("%c", stack[0]);
			for(int i=1;i<top;++i)
				printf(", %c",stack[i]);
		}
		puts("]");
	}
	
	return 0;
}
