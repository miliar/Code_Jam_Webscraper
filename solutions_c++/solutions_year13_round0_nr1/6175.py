#include <cstdio>
#include <algorithm>

using namespace std;

char matrix[4][4];

bool horizontal (char evaluar,int x,int y){
    int cont=0;
    for (int k=y;k<4;++k){
        if (matrix[x][k]==evaluar || matrix[x][k]=='T')
        cont++;
        
    }
    if (cont>=4)
    return true;
    cont=0;
    
    for (int k=y;k>=0;--k){
        if (matrix[x][k]==evaluar || matrix[x][k]=='T')
        cont++;
    }
    
    if (cont>=4)
    return true;
    
    return false;
    
}

bool vertical (char evaluar,int x,int y){
    int cont=0;
    for (int k=x;k<4;++k){
        if (matrix[k][y]==evaluar || matrix[k][y]=='T')
        cont++;
        
    }
    if (cont>=4)
    return true;
    cont=0;
    
    for (int k=x;k>=0;--k){
        if (matrix[k][y]==evaluar || matrix[k][y]=='T')
        cont++;
    }
    
    if (cont>=4)
    return true;
    
    return false;
    
}

bool diagonalder (char evaluar,int x,int y){
    int cont=0;
    int movy=y;
    int n=4;
    for (int k=x;k<n && movy<n;++k){
        if (matrix[k][movy]==evaluar || matrix[k][movy]=='T')
        cont++;
        movy++;
    }
    if (cont>=4)
    return true;
    movy=y;
    cont=0;
    
      for (int k=x;k>=0 && movy<n;--k){
        if (matrix[k][movy]==evaluar || matrix[k][movy]=='T')
        cont++;
        movy++;
    }
    if (cont>=4)
    return true;
    
    return false;
}

bool diagonalizq (char evaluar,int x,int y){
    int cont=0;
    int movy=y;
    int n=4;
    for (int k=x;k<n && movy>=0;++k){
        if (matrix[k][movy]==evaluar || matrix[k][movy]=='T')
        cont++;
        movy--;
    }
    if (cont>=4)
    return true;
    movy=y;
    cont=0;
    
      for (int k=x;k>=0 && movy>=0;--k){
        if (matrix[k][movy]==evaluar || matrix[k][movy]=='T')
        cont++;
        movy--;
    }
    if (cont>=4)
    return true;
    
    return false;
}

int main(){
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;++i){
        printf("Case #%d: ",i);
        
        for (int o=0;o<4;++o){
            scanf("%s",matrix[o]);
        }
        int ganador=-1;
        int cont=0;
        for (int s=0;s<4 && ganador==-1;++s){
            for (int k=0;k<4 && ganador==-1;++k){
                if (matrix[s][k]=='.')
                cont++;
                else if (matrix[s][k]=='X'){
                    if (horizontal('X',s,k) || vertical('X',s,k) || diagonalder('X',s,k)|| diagonalizq('X',s,k))
                    ganador=1;
                    }
                else if (matrix[s][k]=='O'){
                    if (horizontal('O',s,k) || vertical('O',s,k) || diagonalder('O',s,k)|| diagonalizq('O',s,k))
                    ganador=2;
                    
                }
                    
                }
                
            }
            
            if (ganador==1)
            printf("X won\n");
            else if (ganador==2)
            printf("O won\n");
            else if (cont>0)
            printf("Game has not completed\n");
            else
            printf("Draw\n");
            
        }
        return 0;
    }
    
    
