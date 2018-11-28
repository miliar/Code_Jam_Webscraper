#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <string>
#include <vector>
using namespace std;

string in="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvzq";
string ou="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upqz";
int main(){
    
	char inp[550];
	int test,kas=0;
	cin>>test;
	getchar();
	while(test--){
	    gets(inp);
	    printf("Case #%d: ",++kas);
	    for(int i=0; inp[i]; i++)
		    for(int j=0;j<(int)in.size();j++)
		        if(inp[i]==in[j]) { printf("%c",ou[j]); break; }
	    printf("\n");
	}
    return 0;
}
