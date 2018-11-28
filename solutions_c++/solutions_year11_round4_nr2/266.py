#include<stdio.h>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>
#include<sstream>
#include<string>
#include<iostream>
using namespace std;


int m[15][15];
int R, C, D;



int testa(int a){
    int i, k, x, y;
    for(i=0; i+a-1<R; i++)
        for(k=0; k+a-1<C; k++){
            int somax=0, somay=0, soma=0;
            int parx=0, pary=0, par=0;
            for(x=i; x<=i+a-1; x++)
                for(y=k; y<=k+a-1; y++){
                    if((x==i) && (y==k)) continue;
                    if((x==i+a-1) && (y==k)) continue;
                    if((x==i+a-1) && (y==k+a-1)) continue;
                    if((x==i) && (y==k+a-1)) continue;
                    somax += m[x][y]*x;
                    somay += m[x][y]*y;
                    soma += m[x][y];
                    parx += x;
                    pary += y;
                    par += 1;
                }          
            if((somax*par == parx * soma) &&(somay*par == pary * soma))
                return 1;
        }
    return 0;
}

int main(){
    int T, g, i, k;
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%d %d %d ", &R, &C, &D);
        for(i=0; i<R; i++){
            string s;
            cin >> s;
            for(k=0; k<C; k++){
                m[i][k] = s[k]-'0';  
            }
        }
        int vv;
        int resp=0;
        for(int r=10; r>=3; r--){
            vv = testa(r);
            if(vv==1){
                resp = r;
                 break;
            }
        }
        printf("Case #%d: ", g);
        if(resp>0)
            printf("%d\n", resp);
        else 
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
