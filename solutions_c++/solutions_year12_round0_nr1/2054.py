#include <cstdlib>
#include <cstdio>

char map[128];
char set[128];
int main(){
	int i,j,k;
	char buff[3][1024] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
		};

	char aux[3][1024] = {"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
	};
	
	for(i=0;i<128; i++){
		map[i] = '*';
		set[i] = '*';
	}
	map[' '] = ' ';
	
	for(i=0; i<3; i++){
		for(j=0; buff[i][j]!='\0';j++){
			map[buff[i][j]] = aux[i][j];
			set[aux[i][j]] = '1';
		}
	}
	map['q'] = 'z';
	map['z'] = 'q';
	
	int T;
	char input[1024];
	scanf("%d\n",&T);
	for(i=0; i<T; i++){
		gets(input);
		printf("Case #%d: ",i+1);
		for(j=0; input[j]!='\0'; j++){
			printf("%c", map[input[j]]);
		}
		printf("\n");
	}
	

}
