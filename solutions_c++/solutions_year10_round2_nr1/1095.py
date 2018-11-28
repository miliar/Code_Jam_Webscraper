#include <cstdio>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

typedef struct{
    vector<string> store;
    vector<int> index;
}NODE;
NODE trie[1000000];

int main(){
    
    //freopen("al.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int i, j, c, cas, a, b, count, len, num, inde, work;
    char in[105], *p;
    string str;
    
    scanf("%d", &cas);
    for( c=1; c<=cas; ++c ){
        
        count = 0;
        trie[0].store.clear();
        trie[0].index.clear();
        scanf("%d %d", &a, &b);
        
        for( j=0; j<a; ++j ){
            scanf("%s", in);
            len = strlen(in);
            for( i=1; i<len; ++i )
                in[i-1] = in[i];
            in[len-1] = 0;
            
            p = strtok(in,"/");
            inde = 0;
            while( p!=NULL ){
                str = p;
                num = trie[inde].index.size();
                for( i=0; i<num; ++i )
                    if( str.compare(trie[inde].store[i])==0 )
                        break;
                
                if( i!=num )
                    inde = trie[inde].index[i];
                else{
                    ++count;
                    trie[inde].store.push_back(str);
                    trie[inde].index.push_back(count);
                    inde = count;
                    trie[inde].store.clear();
                    trie[inde].index.clear();
                }
                p = strtok(NULL,"/");
            }
        }
        
        work = 0;
        for( j=0; j<b; ++j ){
            scanf("%s", in);
            len = strlen(in);
            for( i=1; i<len; ++i )
                in[i-1] = in[i];
            in[len-1] = 0;
            
            p = strtok(in,"/");
            inde = 0;
            while( p!=NULL ){
                str = p;
                num = trie[inde].index.size();
                for( i=0; i<num; ++i )
                    if( str.compare(trie[inde].store[i])==0 )
                        break;
                
                if( i!=num )
                    inde = trie[inde].index[i];
                else{
                    ++count;
                    trie[inde].store.push_back(str);
                    trie[inde].index.push_back(count);
                    inde = count;
                    trie[inde].store.clear();
                    trie[inde].index.clear();
                    ++work;
                }
                p = strtok(NULL,"/");
            }
        }
        
        printf("Case #%d: %d\n", c, work);
        
    }
    
    return 0;
}
