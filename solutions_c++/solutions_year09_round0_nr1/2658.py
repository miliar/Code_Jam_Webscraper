#include <iostream>
#include <bitset>

enum {
    MAX_DIC=5000,
    MAX_WORD_LEN=15
};

/* global vars */
int wordLength; //the word length
int dicSize;    //how many word in dictionary
int numCase;    //number of test case
char dic[MAX_DIC][MAX_WORD_LEN+1];


/* StringToker */
class StringToker{
    int currentStr;
    char substr[ MAX_WORD_LEN ][26+1];
public:
    StringToker( char*, int );
    char* next();
};

StringToker::StringToker( char* pattern , int numSubStr){

    currentStr = 0;

    char *src = pattern;
    for(int k=0; k<numSubStr; ++k){

        if( *src =='(' ){
            ++src;

            char *des = substr[k];
            while( *src != ')' ){
                *des++ = *src++;
            }
            ++src;
            *des = NULL; //null end
        }else{
            substr[k][0] = *src++;
            substr[k][1] = NULL; //null end
        }
    }
}

char* StringToker::next(){
    return substr[currentStr++];
}

/* match */
int match( char pattern[MAX_WORD_LEN] ){

    std::bitset<MAX_DIC> kickList;

    StringToker toker( pattern , wordLength );
    //printf("pattern=%s\n", pattern);

    //for(int i=0;i<wordLength;++i){
    //    printf("c%d=(%s) ", i, toker.next() );
    //}
    for(int i=0;i<wordLength;++i){
        char* closure = toker.next();

        for(int j=0;j<dicSize;++j){

            if ( kickList[j]==0 && strchr(closure, dic[j][i])==NULL ){
                //not match!
                kickList.set(j); //kick it!
            }
        }
    }

    return dicSize - kickList.count();
}

/* main */
int main(){

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout );

    //read the three constant
    scanf("%d %d %d ", &wordLength, &dicSize, &numCase);


    //built the alien dic
    for(int i=0;i<dicSize;++i)
        scanf("%s ", dic[i]);


    //for each case
    for(int counter=1; counter<=numCase ; ++counter){

        char pattern[ (26+2)*MAX_WORD_LEN ];
        scanf("%s", pattern);

        int result = match( pattern );

        printf("Case #%d: %d\n", counter, result);
    }
    return 0;
}
