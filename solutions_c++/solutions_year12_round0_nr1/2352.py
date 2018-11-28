#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

#define MAX 105
char s[ 105 ], a[ 28 ] =  "yhesocvxduiglbkrztnwjpfmaq";

int main(){
    int t, len;
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );
    gets( s );
    for( int q = 1 ; q <= t ; ++q ){
        gets( s );
        len = strlen( s );
        printf("Case #%d: " , q );
        for( int i = 0 ; i < len ; ++i ){
            if( s[ i ] == ' ' )printf(" ");
            else printf("%c" , a[ s[ i ] - 'a' ] );
        }
        printf("\n");
    }
    return 0;
}
