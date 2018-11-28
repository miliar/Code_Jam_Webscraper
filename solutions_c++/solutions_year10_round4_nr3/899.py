//C

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

const int N = 110;
int mp[200][200];

void dbgOut()
{
    for(int i=0;i<=6;++i){
        for(int j=0;j<=6;++j){
            printf("%d",mp[i][j]);
        }
        putchar('\n');
    }    
}


void setone(int x1,int y1,int x2,int y2)
{
    for(int i=x1;i<=x2;++i){
        for(int j=y1;j<=y2;++j)mp[i][j]=1;
    }    
}

bool Addone()
{
    bool over = true;
    int i,j,k;
    
    //puts("before");dbgOut();
    
    
    for(k=2*N;k>=0;k--){
        for(i=0;i<N;++i){
            if( k-i < N && k-i>=0 ){
                
                if( mp[k-i][i] == 1 ){
                    if( (i>0 && mp[k-i][i-1]==1) || (k-i>0 && mp[k-i-1][i]==1  ) ){
                        mp [k-i][i] = 1;
                        over = false;
                    }
                    else mp[k-i][i] = 0;
                }
                else{
                
                    if( (i>0 && mp[k-i][i-1]==1) &&  (k-i>0 && mp[k-i-1][i]==1  ) ){
                        mp [k-i][i] = 1;
                        over = false;
                    }
                    else mp [k-i][i] = 0;                
                    
                }
                

            }
        }
    }    
    //puts("after");dbgOut();system("pause");
    
    
    
    return over ;
}

/*
2
3
5 1 5 1
2 2 4 2
2 3 2 4

*/



int main()
{
    int c;
    int cs=0;
    scanf("%d",&c);
    
    while(++cs<=c){
        int r,x1,x2,y1,y2;
        scanf("%d",&r);
        while(r--){
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            setone(x1,y1,x2,y2);
        }
        
        int ct = 1;
        while(Addone() == false) ct++;
        
        printf("Case #%d: %d\n",cs,ct);
               
    }
    
    
    
    
    return 0;    
}
