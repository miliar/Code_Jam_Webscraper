#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

struct NODE{
    int order, num;
};
vector<NODE> b, o;

int main(){
    
    freopen("abi.in", "r", stdin);
    freopen("abo.txt", "w", stdout);
    
    int cas, c=0, i, j, n, blue, orange, bindex, oindex, bsize, osize, bpos, opos, ans;
    char col;
    NODE tmp;
    
    scanf("%d", &cas);
    while( cas-- ){
        
        b.clear();
        o.clear();
        scanf("%d", &n);
        for( i=0; i<n; ++i ){
            tmp.order = i;
            scanf(" %c %d", &col, &tmp.num);
            if( col=='O' )  o.push_back(tmp);
            else            b.push_back(tmp);
        }
        
        osize = o.size();
        bsize = b.size();
        bindex = 0;
        oindex = 0;
        ans = 0;
        opos = 1;
        bpos = 1;
        while( bindex<bsize || oindex<osize ){
            //printf("%d %d %d %d\n", bindex, bsize, oindex, osize);
            if( bindex==bsize ){
                ans += (abs(opos-o[oindex].num)+1);
                opos = o[oindex].num;
                ++oindex;
            }
            else if( oindex==osize ){
                ans += (abs(bpos-b[bindex].num)+1);
                bpos = b[bindex].num;
                ++bindex;
            }
            else{
                i = b[bindex].num - bpos;
                j = o[oindex].num - opos;
                if( b[bindex].order < o[oindex].order ){
                    if( abs(i) >= abs(j) )  opos += j;
                    else{
                        if( j > 0 ) opos += (abs(i)+1);
                        else        opos -= (abs(i)+1);
                    }
                    ans += (abs(i)+1);
                    bpos = b[bindex].num;
                    ++bindex;
                }
                else{
                    if( abs(j) >= abs(i) )  bpos += i;
                    else{
                        if( i > 0 ) bpos += (abs(j)+1);
                        else        bpos -= (abs(j)+1);
                    }
                    ans += (abs(j)+1);
                    opos = o[oindex].num;
                    ++oindex;
                }
            }
        }
        printf("Case #%d: %d\n", ++c, ans);
        
    }
    
    return 0;
}
