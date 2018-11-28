
/*
 * Author: ajay0221
 * Email: ajay0221@gmail.com
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cmath>

using namespace std ;

int main () {
	int arr[26];
	char s[26] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
	for ( int i = 0 ; i < 26 ; i++ ) {
		arr[s[i]-'a'] = i;
	}

	int test;
	char input[120];
	scanf("%d",&test);
	for ( int i = 0 ; i < test ; i++ ) {
		getchar();
		scanf("%[^\n]",input);
		printf("Case #%d: ",i+1);
		//printf("Input rescieved : %s\n",input);
		for ( int j = 0 ; input[j] != '\0' ; j++ ) {
			if ( input[j] == ' ' ) printf(" ");
			else printf("%c",'a' + arr[input[j]-'a']);
		}
		printf("\n");
	}
	return 0 ;
}

