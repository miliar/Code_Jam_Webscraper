#include <cstdio>
#include <cstdlib>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

int main(){
    char p[1000];
    int pos;
    map<pair<char,char>,char> troca;
    map<pair<char,char>,char> ap;
    pair<char,char> pc,pc2;
    int n1,n2,n3,m,i,j,k,t;
    char a,b,c;
    char pal[200];
    scanf("%d", &t);
    for( k =1; k <=t; k++){
        pos = 0;
        troca.clear();
        ap.clear();
        scanf("%d", &n1);
        for( i =0; i <n1; i++){
            scanf("%s", &pal);
            a = pal[0];
            b = pal[1];//scanf(" %c", &b);
            c = pal[2];//scanf(" %c", &c);
            pc.first = a;
            pc.second = b;
            troca[pc] = c;
            pc.first = b;
            pc.second = a;
            troca[pc] = c;     
            //printf("->%c%c%c<-\n",a,b,c);       
        }
        scanf("%d", &n2);
        for( i =0; i <n2; i++){
           // scanf(" %c", &a);
            //scanf(" %c", &b);
                        scanf("%s", &pal);
            a = pal[0];
            b = pal[1];//scanf(" %c", &b);
            pc.first = a;
            pc.second = b;
            ap[pc] = 'X';
            pc.first = b;
            pc.second = a;
            ap[pc] = 'X';
            
            //printf("             %c %c\n", a, b);       
        }
        scanf("%d", &n3);
//        scanf(" %c ", &a);
//        pc.first = a;
        scanf("%s", pal);
        int ok;
        for( i =0; i <n3; i++){
            ok = 1;
            a = pal[i];//            scanf(" %c", &a);
            pc.second = a;
            if( pos ){
            if( troca.find(pc) != troca.end()){
                ok =0;
                p[pos-1] = troca[pc];
                pc.first = troca[pc];
            } else {
                for( j = 0; j < pos; j++){
                    pc2.first = p[j];
                    pc2.second = a;
                    if( ap.find(pc2) != ap.end() ){
                        pos = 0;
                        ok =0;
                    }
                }
            }
            }
            if( ok ){
                p[pos++] = pc.second;
                pc.first = pc.second;
            }   
        }        
        
        
        printf("Case #%d: [", k, n3);
        if( pos ) printf("%c", p[0]);
        for( i =1; i < pos; i++){
            printf(", %c", p[i]);
        }
        printf("]\n");
    }
}
