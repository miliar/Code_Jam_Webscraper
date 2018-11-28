#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

#define TAM 1024

char mat[TAM][TAM];

int main(){
    int t;
    int nt;
    FILE *fin = fopen("A-large.in","r");
    FILE *fout = fopen("A.out","w");
    int n,m;
    fscanf(fin,"%d",&nt);
    for(int t = 1 ; t <= nt ; t++){
        fscanf(fin,"%d %d",&n,&m);
        for(int i = 0 ; i < n ; i ++)
            fscanf(fin," %s",mat[i]);
        int ans = 1;
        for(int i = 0 ; i < n - 1 ; i++){
            for(int j = 0 ; j < m - 1; j++){
                if(mat[i][j] == '#'){
                    if(mat[i+1][j] == '#' && mat[i][j+1] == '#' && mat[i][j] == '#'){
                            mat[i][j] = mat[i+1][j+1] = '/';
                            mat[i+1][j] = mat[i][j+1] = '\\';
                    }
                    else ans = 0;
                }
            }
        }
        for(int i = 0 ; i < n  ; i++)
            for(int j = 0 ; j < m; j++)
                if(mat[i][j] == '#') ans = 0;
    fprintf(fout,"Case #%d:\n",t);
        if(ans == 0) fprintf(fout,"Impossible\n");
        else{
           for(int i = 0 ; i < n ; i++)
                fprintf(fout,"%s\n",mat[i]);
        }
    }

    return 0;

}
