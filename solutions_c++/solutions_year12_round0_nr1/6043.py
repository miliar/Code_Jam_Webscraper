#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;
int main() {

    FILE *fin = fopen("downloaded.in","r");
    FILE *fout = fopen("A-small.out","w");
    int T,i,j;
    char G[31][101];
    char S[31][101];
    char A[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char a;
    fscanf(fin,"%d",&T);
    
        a=fgetc(fin);    
    for(i=0;i<T;i++){
    
fprintf(fout,"Case #%d: ",i+1);
        for(j=0;j<101;j++)
        {
            //cout << "i,j are " << i << ' ' << j << '\n';
             G[i][j]=fgetc(fin);
            
            if(G[i][j]=='\n' || G[i][j]=='\r') {break;}
            
            if(G[i][j]==' ') {S[i][j]=' ';}
            else
            {
            S[i][j]=A[G[i][j]-97];
            
            }
            
            fprintf(fout,"%c",S[i][j]);
            //cout << "i is " << i << " j is " << j << " G[i][j] is" << G[i][j] ;    
        }
        fprintf(fout,"%c",'\n');
    }

    
}
