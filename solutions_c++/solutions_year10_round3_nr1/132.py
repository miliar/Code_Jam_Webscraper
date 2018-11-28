#include <cstdio>
#include <map>

using namespace std;
typedef struct{
    int start;
    int end;
}NODE;
NODE node[1000];
map <double,int> record[1000];

int main(){
    
    //freopen("al.in","r",stdin);
    //freopen("al.txt","w",stdout);
    
    int i, j, c, cas, num, num2; 
    int dif1, dif2, cnt;
    double seg;
    
    scanf("%d", &cas);
    for( c=1; c<=cas; ++c ){
        
        scanf("%d", &num);
        for( i=0; i<num; ++i ){
            scanf("%d %d", &node[i].start, &node[i].end);
            record[i].clear();
        }
        num2 = num-1;
        for( i=0; i<num2; ++i ){
            dif1 = node[i].end-node[i].start;
            for( j=i+1; j<num; ++j ){
                
                if( (node[j].start > node[i].start && node[j].end > node[i].end) || (node[j].start < node[i].start && node[j].end < node[i].end) )
                    continue;
                    
                dif2 = node[j].end-node[j].start;
                
                seg = ((double)(node[i].start-node[j].start))/(dif1-dif2);
                
                if( record[i].find(seg)==record[i].end() )
                    record[i][seg] = 1;
                if( record[j].find(seg)==record[j].end() )
                    record[j][seg] = 1;
            }
        }
        
        for( i=0,cnt=0; i<num; ++i )
            cnt += record[i].size();
        
        printf("Case #%d: %d\n", c, cnt/2);
    }
    
    return 0;
}
