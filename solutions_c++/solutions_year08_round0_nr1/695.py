#include <iostream>
#include <cstring>
#include <string>
#include <map>

using namespace std;

int num_s,num_q;

int c[105][1005];  // c[i][j] ��ʾ�������� i �ӵ� j ����ѯ��ʼ�ܹ�����ĸ��� 

char s[105][105];      // ��������, ��λ�� 1 ��ʼ��� 
map<string,int> s2pos; // �����ִ���ѯλ�� 

char q[1005][105];     // ��ѯ��¼ 

int main(){
    //freopen("a.txt","r",stdin);
    //freopen("out2.txt","w",stdout);
    
    int i,j,k,m,n;
    
    // ��ʼ�� c[][]
    for( i=0;i<105;i++ ){
        c[i][0] = 0; 
    } 
    
    scanf("%d",&n);
    
    for( i=1;i<=n;i++ ){
        // ������������ 
        scanf("%d",&num_s);
        gets(s[0]);
        for( j=1;j<=num_s;j++ ){
            gets( s[j] ); 
            s2pos[ s[j] ] = j;
        }  
        
        // �����ѯ
        scanf("%d",&num_q);
        gets(q[0]); 
        for( j=1;j<=num_q;j++ ){
            gets( q[j] ); 
            int pos = s2pos[ q[j] ]; // �õ���ǰ��ѯ������ͬ�����������λ��
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

        // ��λ�� 1 ��ʼ���� 
        int pos = 1;
        int num_swich = 0;
        while( num_q>=pos ){
            // ̰��������ʼ
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
