#include <stdio.h>
char str[1000000];
char match[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main (){
	int n;
	freopen ("in.in","r",stdin);
	freopen ("out.2","w",stdout);
	scanf ("%d",&n);
	getchar ();
	for (int test=1 ;test<=n ;test++){
		gets (str);
		printf ("Case #%d: ",test);
		for (int j=0 ;str[j] ;j++){
			if (str[j] == ' ')
				printf (" ");
			else
				printf ("%c",match[str[j]-'a']);
		}
		printf ("\n");
	}
	return 0;
}
