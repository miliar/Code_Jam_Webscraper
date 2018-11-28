#include <cstdio>
#include <cstring>
using namespace std;

int cas;
char ans[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q','\0'};
char ent[111];

int main(){
	scanf("%d\n",&cas);
	for ( int c = 1 ; c <= cas ; c++ ){
		gets(ent);
		printf("Case #%d: ",c);
		for ( int i = 0 ; ent[i] ; i++ ){
			if ( ent[i] == ' ' ) printf(" ");
			else printf("%c",ans[ent[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}
