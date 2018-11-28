#include <iostream>
#include <cstring>
#include <string>
#include <map>

using namespace std;

int num_s,num_q;

int c[105][1005];  // c[i][j] 表示搜索引擎 i 从第 j 个查询开始能够处理的个数 

char s[105][105];      // 搜索引擎, 从位置 1 开始存放 
map<string,int> s2pos; // 根据字串查询位置 

char q[1005][105];     // 查询记录 

int main(){
    //freopen("a.txt","r",stdin);
    //freopen("out2.txt","w",stdout);
    
    int i,j,k,m,n;
    
    // 初始化 c[][]
    for( i=0;i<105;i++ ){
        c[i][0] = 0; 
    } 
    
    scanf("%d",&n);
    
    for( i=1;i<=n;i++ ){
        // 读入搜索引擎 
        scanf("%d",&num_s);
        gets(s[0]);
        for( j=1;j<=num_s;j++ ){
            gets( s[j] ); 
            s2pos[ s[j] ] = j;
        }  
        
        // 读入查询
        scanf("%d",&num_q);
        gets(q[0]); 
        for( j=1;j<=num_q;j++ ){
            gets( q[j] ); 
            int pos = s2pos[ q[j] ]; // 得到当前查询名称相同的搜索引擎的位置
            for( k=1;k<pos;k++ ){
                c[k][j] = 1;
                m = j-1;
                while( c[k][m] ){
                    c[k][m] ++;
                    m--;   
                }   
            } 
            c[pos][j] = 0;
            for( k=pos+1;k<=num_s;k++ ){
                c[k][j] = 1;
                m = j-1;
                while( c[k][m] ){
                    c[k][m] ++;
                    m--;   
                }   
            }
        }

        // 从位置 1 开始处理 
        int pos = 1;
        int num_swich = 0;
        while( num_q>=pos ){
            // 贪心搜索开始
            int max = 1;
            for( j=1;j<=num_s;j++ ){
                if( c[j][pos] > max )
                    max = c[j][pos]; 
            }   
            pos += max;
            if( pos<=num_q ) num_swich++;
        }
        printf("Case #%d: %d\n",i,num_swich);
        s2pos.clear();
    }
    
    return 0;
}
