#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


char buf[200];


void testcase(int num){

scanf("%s", buf);

int ss = strlen(buf);

//cout << "len (" << buf << ") ss " << ss << endl;

if ( next_permutation(buf, buf + ss) ){
    printf("Case #%d: %s\n", num, buf);
} else {
    printf("Case #%d: ", num);
    for(int i=0; i<ss; ++i){
        if ( buf[i] != '0' ){
            printf("%c0", buf[i]);
            buf[i] = '-';
            break;
        }
    }
    
    for(int i=0; i<ss; ++i){
        if ( buf[i] != '-' ) printf("%c", buf[i]);
    }
    printf("\n");
}

}

int main(){
int t; scanf("%d", &t);
for(int i=1; i<=t; ++i) testcase(i);
return 0;
}

