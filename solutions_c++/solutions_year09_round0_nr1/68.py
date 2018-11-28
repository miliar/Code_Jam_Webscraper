/*
    Qualification Round 2009 -
    Alien Language
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
using namespace std ;

    int L , D , N , ans ;
    char dict[5000][20] , line[1000000] , *p ;
    bool exist[15][26] ;

bool check(int th){
    bool correct = true ;
    for(int j=0;j<L;++j)
        if(!exist[j][dict[th][j]-'a']){
            correct = false ;
            break ;
        }
    if(correct) return true ;
    return false ;
}

int main(){
    scanf("%d %d %d\n",&L,&D,&N) ;
    for(int i=0;i<D;++i)
        scanf("%s\n",dict[i]) ;
    for(int i=0;i<N;++i){
        ans = 0 ;
        memset(exist,false,sizeof(exist)) ;
        gets(line) ;
        p = line ;
        for(int j=0;j<L;++j){
            if(*p=='('){
                ++p ;
                while(*p!=')'){
                    exist[j][*p-'a'] = true ;
                    //printf("%c",*p) ;
                    ++p ;
                }
                ++p ;
            }
            else{
                exist[j][*p-'a'] = true ;
                //printf("%c",*p) ;
                ++p ;
            }
        }
        for(int j=0;j<D;++j)
            if(check(j)) ++ans ;
        printf("Case #%d: %d\n",i+1,ans) ;
    }
	return 0 ;
}
