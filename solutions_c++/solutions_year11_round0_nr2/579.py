#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

struct NODE{
    char a, b, c;
};

vector<char> keep;
vector<NODE> b, o;

int main(){
    
    freopen("bbi.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int cas, c=0, i, j, k, com, opp, len;
    char in[105];
    NODE tmp;
    int appear[26];
    
    scanf("%d", &cas);
    while( cas-- ){
        
        keep.clear();
        b.clear();
        o.clear();
        memset(appear,0,sizeof(appear));
        scanf("%d", &com);
        for( i=0; i<com; ++i ){
            scanf("%s", in);
            tmp.a = in[0];
            tmp.b = in[1];
            tmp.c = in[2];
            b.push_back(tmp);
        }
        scanf("%d", &opp);
        for( i=0; i<opp; ++i ){
            scanf("%s", in);
            tmp.a = in[0];
            tmp.b = in[1];
            o.push_back(tmp);
        }
        scanf("%d %s", &len, in);
        
        for( i=0; i<len; ++i ){
            j = keep.size();
            if( j > 0 ){
            for( k=0; k<com; ++k )
            if( (keep[j-1]==b[k].a && in[i]==b[k].b) || (keep[j-1]==b[k].b && in[i]==b[k].a) ){
                --appear[keep[j-1]-'A'];
                keep.pop_back();
                keep.push_back(b[k].c);
                ++appear[b[k].c-'A'];
                break;
            }
            }
            
            if( j==0 || k==com ){
                keep.push_back(in[i]);
                ++appear[in[i]-'A'];
            }
            
            for( k=0; k<opp; ++k )
            if( appear[o[k].a-'A'] && appear[o[k].b-'A'] ){
                keep.clear();
                memset(appear,0,sizeof(appear));
                break;
            }
        }
        
        if( keep.size()>0 ){
            printf("Case #%d: [", ++c);
            for( i=0,j=keep.size()-1; i<j; ++i )
                printf("%c, ", keep[i]);
            printf("%c]\n", keep[j]);
        }
        else    printf("Case #%d: []\n", ++c);
    }
    
    return 0;
}
