#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<vector>
#include<list>
#define TRACE(x...) x

using namespace std;

int nonbase [1000];
int oposed [1000];
char dic[1000];
int cont = 1;
list < char > lista;


int palavra ( char a, char b ) {
	return (a-'A')*100 + b-'A';
}

void printa(void) {
	printf("Case #%d: [",cont++);
	list<char>::iterator fim = lista.end(); fim--;
	for ( list<char>::iterator it = lista.begin(); it != fim; ++it ) {
			printf("%c, ",*it);
		}
	printf("%c]\n",*fim);
}




int main (void) {
	int t,c,d,n, tam_nonbase, tam_oposed, p1, p2;
	char s[110];
	list<char>::iterator fim, c1, c2;
	scanf("%d",&t);
	while (t--) {
		lista.clear();
		scanf(" %d",&c);
		tam_nonbase = tam_oposed = 0;
		while (c--) {
			scanf(" %s",s);
			p1 = palavra(s[0],s[1]);
			p2 = palavra(s[1],s[0]);
			nonbase[tam_nonbase++] = p1;
			nonbase[tam_nonbase++] = p2;
			dic[p1] = dic[p2] = s[2];
		}
		
		scanf(" %d",&d);
		while (d--) {
			scanf(" %s",s);
			oposed[tam_oposed++] = palavra(s[0],s[1]);
			oposed[tam_oposed++] = palavra(s[1],s[0]);
		}
		
		sort(nonbase,nonbase+tam_nonbase);
		sort(oposed,oposed+tam_oposed);
		
		scanf("%d %s",&n,s);

		for ( int i = 0; s[i] != '\0'; i++ ) {
			lista.push_back(s[i]);
			if ( lista.size() < 2 ) continue;
			fim = lista.end();
			fim--; c1 = fim;
			fim--; c2 = fim;
			p1 = palavra(*c1,*c2);
			if ( binary_search( nonbase ,nonbase+tam_nonbase ,p1 ) ) {
				lista.pop_back(); lista.pop_back();
				lista.push_back(dic[p1]);
			}
			
			
			else {
				for ( list<char>::iterator it = lista.begin(); it != lista.end(); ++it ) {
					p1 = palavra(*c1,*it);
					if ( binary_search( oposed,oposed+tam_oposed,p1 ) ) { lista.clear(); break; }

				}
			}
			
		}
						
			//printf(">>%d %d\n",*c2,*c1);
		//printf("%s\n",s);
		printa();
		
		//printf(">> %d\n",*(fim--));
			
		
	}
	
	return 0;
}
