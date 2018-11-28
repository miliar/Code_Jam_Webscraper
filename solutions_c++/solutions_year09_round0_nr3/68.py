/*
    Qualification Round 2009 -
    Welcome to Code Jam
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
using namespace std ;

    const char wel[20] = "welcome to code jam" ;
    int N , tab[5000][20] ;
    char line[10000] ;

int main(){
    gets(line) ;
    sscanf(line,"%d",&N) ;
    for(int z=1;z<=N;++z){
        memset(tab,0,sizeof(tab)) ;
        gets(line) ;
        int lnh = strlen(line) ;
        for(int i=0;i<lnh;++i){
            for(int j=0;j<19;++j)
                tab[i+1][j] = tab[i][j] ;
            for(int j=0;j<19;++j){
                if(line[i]==wel[j]){
                    if(j==0)
                        ++tab[i+1][j] ;
                    else{
                        tab[i+1][j] += tab[i][j-1] ;
                    }
                    tab[i+1][j] %= 10000 ;
                }
            }
        }
        printf("Case #%d: %04d\n",z,tab[lnh][18]) ;
        //fprintf(stderr,"%d %d %d\n",z,lnh,tab[lnh][18]) ;
    }
	return 0 ;
}
