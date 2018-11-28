#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>

#define INF 100000000
#define MAX 1048576

using namespace std;

char *a = "yhesocvxduiglbkrztnwjpfmaq";
         //abcdefghijklmnopqrstuvwxyz
char b[1000];

int n;

int main() {
    scanf("%d", &n);
    
    for (int t=0; t<n; t++) {
	do gets(b); while (b[0] == '\n' || b[0] == ' ' || b[0] == 0);
	printf("Case #%d: ", t+1);
	for (int i=0; b[i]; ++i) {
	    if (b[i] == ' ') printf("%c", b[i]);
	    else printf("%c", a[b[i] - 'a']);
	}
	printf("\n");
    }
   
    return 0;
}