#include <map>
#include <vector>
#include <cstdio>
#include <cstring>

typedef unsigned int uint;

using namespace std;

int main() {

//    FILE * learn = fopen("learn","r");


    map<char, char > translate;
    translate[' ']=' ';
    translate['a']='y';
    translate['b']='h';
    translate['c']='e';
    translate['d']='s';
    translate['e']='o';
    translate['f']='c';
    translate['g']='v';
    translate['h']='x';
    translate['i']='d';
    translate['j']='u';
    translate['k']='i';
    translate['l']='g';
    translate['m']='l';
    translate['n']='b';
    translate['o']='k';
    translate['p']='r';
    translate['r']='t';
    translate['s']='n';
    translate['t']='w';
    translate['u']='j';
    translate['v']='p';
    translate['w']='f';
    translate['x']='m';
    translate['y']='a';
    translate['z']='q';
    translate['q']='z';

//    char*  learn_plain[4], *learn_translated[4];

//    //read plain text
//    for( int i=0; i<4; ++i) {
//        learn_plain[i] = new char[101];
//        fscanf(learn,"%[^\n]", learn_plain[i]);
//        fgetc(learn);
////        printf("%s\n", learn_plain[i]);
//    }
//    //read translated
//    for( int i=0; i<4; ++i) {
//        learn_translated[i] = new char[101];
//        fscanf(learn,"%[^\n]", learn_translated[i]);
//        fgetc(learn);
//    }

//    for( int i=0; i<4; ++i) {
//        int n = strlen(learn_plain[i]);
//        for( int j=0;j<n; ++j) {
//            translate[learn_plain[i][j]]=learn_translated[i][j];
//        }
//    }
//        for ( map<char,char >::iterator i= translate.begin(); i!=translate.end(); ++i) {
//            printf("translate['%c']='%c';\n", (*i).first,(*i).second);
//        }

    int N,slen;
    scanf("%d\n",&N);
    for( int i=0; i<N; ++i) {
        char test[101];
        scanf("%[^\n]\n",test);
//        printf("%s\n",test);
        slen=strlen(test);
        printf("Case #%d: ",i+1);
        for( int j =0;j<slen; ++j ) {
            printf("%c",translate[test[j]]);
        }
        putchar('\n');
    }

    return 0;
}
