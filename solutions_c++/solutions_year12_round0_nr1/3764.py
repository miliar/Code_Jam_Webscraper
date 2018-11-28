#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

char translationTable[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(){
    int t;
    char c = ' ';
    cin >> t;
    scanf("%c", &c);
    for (int i = 0; i < t; ++i){
	printf("Case #%d: ", i+1);
	c = ' ';
	while (c != '\n'){
	    scanf("%c", &c);
	    //cout << c;
	    if (c == ' ' || c == '\n') cout << c;
	    else cout << translationTable[c-'a'];
	}
    }
    return 0;
}
