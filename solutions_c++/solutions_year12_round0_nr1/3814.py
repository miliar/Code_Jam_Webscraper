#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

char str[100000];
char s[100000];

int main(){
	int n;
	gets(str);
	sscanf(str,"%d",&n);

	for(int i=0; i<n; i++){
		gets(str);
		int j=0;
		while(str[j] != '\0' && str[j] != '\n'){
			if(str[j] == 'a') s[j] = 'y';
			else if(str[j] == 'b') s[j] = 'h';
			else if(str[j] == 'c') s[j] = 'e';
			else if(str[j] == 'd') s[j] = 's';
			else if(str[j] == 'e') s[j] = 'o';
			else if(str[j] == 'f') s[j] = 'c';
			else if(str[j] == 'g') s[j] = 'v';
			else if(str[j] == 'h') s[j] = 'x';
			else if(str[j] == 'i') s[j] = 'd';
			else if(str[j] == 'j') s[j] = 'u';
			else if(str[j] == 'k') s[j] = 'i';
			else if(str[j] == 'l') s[j] = 'g';
			else if(str[j] == 'm') s[j] = 'l';
			else if(str[j] == 'n') s[j] = 'b';
			else if(str[j] == 'o') s[j] = 'k';
			else if(str[j] == 'p') s[j] = 'r';
			else if(str[j] == 'q') s[j] = 'z';
			else if(str[j] == 'r') s[j] = 't';
			else if(str[j] == 's') s[j] = 'n';
			else if(str[j] == 't') s[j] = 'w';
			else if(str[j] == 'u') s[j] = 'j';
			else if(str[j] == 'v') s[j] = 'p';
			else if(str[j] == 'w') s[j] = 'f';
			else if(str[j] == 'x') s[j] = 'm';
			else if(str[j] == 'y') s[j] = 'a';
			else if(str[j] == 'z')  s[j] = 'q';
			else s[j] = str[j];
			j++;
		}
		//printf("%d\n",j);
		s[j] = '\0';
		printf("Case #%d: %s\n",i+1,s);
	}
	
	return 0;
}

