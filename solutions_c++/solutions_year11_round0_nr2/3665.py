#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <map>
using namespace std;

int main(){
    freopen( "1.txt","r",stdin );
    freopen( "2.txt","w",stdout );
    int t,ca=0;
    scanf("%d",&t);
    while(t--){

        int C,D;
        scanf("%d",&C);
        map< pair<char,char>,char > combine;
        char S[105];
        for(int i = 0;i<C;++i){
            scanf("%s",S);
            combine[ make_pair(S[0],S[1]) ] = S[2];
            combine[ make_pair(S[1],S[0]) ] = S[2];
        }
        scanf("%d",&D);
        map< char,char >inverse;
        for(int i = 0;i<D;++i){
            scanf("%s",S);
            inverse[ S[0] ] = S[1];
            inverse[ S[1] ] = S[0];
        }
        int N;
        scanf("%d",&N);
        scanf("%s",S);
        string res = "";
        for(int i = 0;i<N;++i){

            if( !i || res.empty() )
                res += S[i];
            else{

                if( combine[ make_pair( res[ res.size()-1 ] , S[i] ) ] ){
                    res[ res.size()-1 ] = combine[ make_pair( res[ res.size()-1 ] , S[i] ) ];
                    if( inverse[ res[res.size()-1] ] && res.find( inverse[ res[res.size()-1] ] ) < res.size() )
                        res = "";
                }
                else{
                    if( inverse[ S[i] ] && res.find( inverse[ S[i] ] ) < res.size() )
                        res = "";
                    else res += S[i];
                }

            }

        }
        printf("Case #%d: [",++ca);
        for(int i = 0;i<res.size();++i){
            printf("%c",res[i]);
            if( i != res.size()-1)printf(", ");
        }
        printf("]\n");

    }
    return 0;
}
