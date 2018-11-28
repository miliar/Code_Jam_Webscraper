#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for(int a = b ; a < c ; ++a )
#define db(x) cerr << #x " == " << x << endl
#define _ << ", " <<
typedef long long ll;

char normal[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi*rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd*de kr kd eoya kw aej tysr re ujdr lkgc jv*y qeez";
char codif[] =  "our language is impossible to understand*there are twenty six factorial possibilities*so it is okay if you want to just give up*a zooq";
char code[300];

char str[1<<20];

int main() {
	
	fr(i,0,300) code[i] = i;
	for( int i = 0 ; normal[i] ; ++i ) code[ normal[i] ] = codif[i];
	
	int t;
	scanf("%d", &t);
	gets(str);
	int caso = 1;
	while( t-- ) {
		gets(str);
		for( int i = 0 ; str[i] ; ++i ) str[i] = code[ str[i] ];
		printf("Case #%d: ", caso++);
		puts(str);
	}
	
	return 0;
}
