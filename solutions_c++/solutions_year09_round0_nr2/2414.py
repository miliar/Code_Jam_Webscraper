#include <stdio.h>

int n;
int linhas, colunas;
int mat[100][100];
char resp[100][100];
bool visited[100][100];
char current;
bool vizinhoSuperior(int linha){
    if(linha-1 >= 0){
        return true;    
    }
    return false;
}
bool vizinhoInferior(int linha){
    if(linha+1 < linhas){
        return true;
    }
    return false;
}   
bool vizinhoDireita(int coluna){
    if(coluna+1 < colunas){
        return true;
    }
    return false;
}
bool vizinhoEsquerda(int coluna){
    if(coluna-1 >= 0){
        return true;
    }
    return false;
}

void bfs(int line,int column){
    int lowestSoFar = mat[line][column];
    int newline=-1,newcolumn=-1;
//    printf("----%d %d",line,column);
    visited[line][column] = true;
    if(vizinhoSuperior(line)){
        if(mat[line-1][column] < lowestSoFar){
            newline = line-1;
            newcolumn = column;
            lowestSoFar = mat[newline][newcolumn];
        }
    }
    if(vizinhoEsquerda(column)){
        if(mat[line][column-1] < lowestSoFar){
            newline = line;
            newcolumn = column-1;
            lowestSoFar = mat[newline][newcolumn];
        }
    
    }
    if(vizinhoDireita(column)){
        if(mat[line][column+1] < lowestSoFar){
            newline = line;
            newcolumn = column+1;
            lowestSoFar = mat[newline][newcolumn];
        }
    
    }
    if(vizinhoInferior(line)){
        if(mat[line+1][column] < lowestSoFar){
            newline = line+1;
            newcolumn = column;
            lowestSoFar = mat[newline][newcolumn];
        }
    }
    if(newline!=-1 && newcolumn!=-1){ //printf("aqui - %d %d\n",newline,newcolumn);
        if(resp[newline][newcolumn] !='0'){
//            printf("aqui - %d %d\n",newline,newcolumn);
            resp[line][column] = resp[newline][newcolumn];
        }
        else{
            bfs(newline,newcolumn);
            resp[line][column] = resp[newline][newcolumn];
        }
    }
    else{
        resp[line][column] = current;
        current = current+1;
    }
    
}


int main(){
    int i,j;
    scanf("%d",&n);
    int iterator;

    for(iterator =0; iterator < n; iterator++){
        
        current = 'a';
        scanf("%d %d",&linhas,&colunas);
        for(i=0;i<linhas;i++){
            for(j=0;j<colunas;j++){
                resp[i][j]='0';
                visited[i][j] = false;
            }
        }    
        for(i=0;i<linhas;i++){
            for(j=0;j<colunas;j++){
                scanf("%d",&mat[i][j]);
            }
        }
        
        for(i=0;i<linhas;i++){
            for(j=0;j<colunas;j++){
                if(visited[i][j]==false){
//                    printf("OK\n");
                    bfs(i,j);
//                    current=current+1;
                }
            }
        }
        
                
        printf("Case #%d:\n",iterator+1);
        for(i=0;i<linhas;i++){
            for(j=0;j<colunas-1;j++){
                printf("%c ",resp[i][j]);
            }
            printf("%c\n",resp[i][j]);
        }
        
    }


    return 0;
}
