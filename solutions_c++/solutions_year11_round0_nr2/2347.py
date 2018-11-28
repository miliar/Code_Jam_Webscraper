#include <iostream>
#include <cstdio>
#include <cstring>

#define floop(i,a,b) for(int i=(a);i<(b);i++)
#define rloop(i,a,b) for(int i=(a);i>=(b);i--)

char create[8][8],destroy[8][8],spell[200],stack[200];

void _clear(){
	floop(i,0,8){
		memset(create[i],' ',8);
		memset(destroy[i],' ',8);
	}
}

int value(char ch){
	switch(ch){
		case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
		default: return -1;
	}
}

void process(int testcase){
	_clear();
	int create_spell,destroy_spell,size,index=-1,terminate=0;
	char a,b,c;
	int p,q;
	scanf("%d",&create_spell);
	floop(i,0,create_spell){
		scanf(" %c%c%c",&a,&b,&c);
		p=value(a);
		q=value(b);
		create[p][q]=c;
		create[q][p]=c;
	}
	
	scanf("%d",&destroy_spell);
	floop(i,0,destroy_spell){
		scanf(" %c%c",&a,&b);
		p=value(a);
		q=value(b);
		destroy[p][q]='\0';
		destroy[q][p]='\0';
	}

	scanf("%d %s\n",&size,spell);
	
	floop(i,0,size){
		b=spell[i];
		if(index>=0){
			a=stack[index];
			p=value(a);
			q=value(b);

			if(p>=0 && q>=0 && create[p][q]!=' '){
				stack[index]=create[p][q];
			}else{
				terminate=0;
				
				if(q>=0){
					rloop(j,index,0){
						p=value(stack[j]);
						terminate=(p>=0 && destroy[p][q]=='\0')?1:terminate;
					}
					if(terminate){
						index=-1;
					}else{
						stack[++index]=b;
					}
				}else{
					stack[++index]=b;
				}

				terminate=0;
			}
		}else{
			stack[++index]=b;
		}

/********************testing********************
printf("i=%d spell[i]=%c stack=",i,spell[i]);
floop(k,0,index+1){
	printf("%c,",stack[k]);
}
putchar('\n');
/**********************************************/

	}
	
	printf("Case #%d: [",testcase);
	
	floop(k,0,index+1){
		printf("%c",stack[k]);
		if(k<index) printf(", ");
	}
	
	printf("]\n");

}

main(){
	int testcases;
	scanf("%d",&testcases);
	floop(i,0,testcases){
		process(i+1);
	}
}
