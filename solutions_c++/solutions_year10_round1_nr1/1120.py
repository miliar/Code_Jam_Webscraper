
#include <stdio.h>
#include <iostream>
#include <ctype.h>

using namespace std;

int n,k;
char board[51][51];

void rota(){
    int aux=0;
    char c;
    for (int i=0; i<n; i++){
        aux=n-1;
        for (int j=n-1; j>=0; j--){
            if (board[i][j]!='.'){
                c=board[i][j];
                board[i][j]='.';
                board[i][aux]=c;
                aux--;
            }
        }
    }
}

char compruebaChar(char c){
    int cont;
    for (int i=0; i<n; i++){
        cont=0;
        for (int j=0; j<n; j++){
            if (board[i][j]==c){
                cont++;
                if (cont>=k)
                    return true;
            }
            else
                cont=0;
        }
    }

    for (int j=0; j<n; j++){
        cont=0;
        for (int i=0; i<n; i++)
            if (board[i][j]==c){
                cont++;
                if (cont>=k)
                    return true;
            }
            else
                cont=0;
    }

    for (int j=0; j<n-1; j++){
        cont=0;
        for (int i=0; (i+j)<n; i++){
            if (board[i][j+i]==c){
                cont++;
                if (cont>=k)
                    return true;
            }
            else
                cont=0;
        }
        cont=0;
        for (int i=0; (j-i)>=0; i++){
            if (board[i][j-i]==c){
                cont++;
                if (cont>=k)
                    return true;
            }
            else
                cont=0;
        }
    }

    for (int i=0; i<n-1; i++){
        cont=0;
        for (int j=0; (j+i)<n; j++){
            if (board[i+j][j]==c){
                 cont++;
                if (cont>=k)
                    return true;
            }
            else
                cont=0;
        }        
    }

    for (int j=0; j<n-1; j++){
        cont=0;
        for (int i=0; i<n; i++){
            if (board[n-1-i][j+i]==c){
                 cont++;
                if (cont>=k)
                    return true;
            }
            else
                cont=0;
        }
    }

    return false;

}

char comprueba(){
    bool red=false;
    bool blue=false;
    red=compruebaChar('R');
    blue=compruebaChar('B');
    if (red){
        if (blue) return 'O';
        else return 'R';
    }
    else{
        if (blue) return 'B';
        else return 0;
    }

}

void imprime(){
    cout<<endl;
    for (int i=0; i<n; i++){
            for (int j=0; j<n; j++)
                putchar(board[i][j]);
            putchar('\n');
        }
}

int main(){
    int casos;
    cin >>casos;
    char c;
    for(int ccasos=1; ccasos<=casos; ccasos++){
        cin>>n>>k;
        while ((c=getchar())!='\n');
        for (int i=0; i<n; i++)
            gets(board[i]);

        //transpuesta();
        //imprime();

        //espejo();
        //imprime();

        rota();
       // imprime();

        char c;
        if (c=comprueba()){
            if (c=='R')
                printf("Case #%d: Red\n",ccasos);
            else if (c=='B')
                printf("Case #%d: Blue\n",ccasos);
            else
                printf("Case #%d: Both\n",ccasos);
        }
        else
            printf("Case #%d: Neither\n",ccasos);

    }
    return 0;
}
