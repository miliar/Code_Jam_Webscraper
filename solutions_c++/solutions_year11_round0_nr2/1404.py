#include<stdio.h>
#include<vector>

using namespace std;

int main(){
    int m[300];
    int i, j;    
    for(i=0; i<300; i++)
        m[i]=-1;

    m['Q']=0;
    m['W']=1;  
    m['E']=2;
    m['R']=3;
    m['A']=4;
    m['S']=5;
    m['D']=6;
    m['F']=7;
  
vector<char> x;

    char com[10][10];
    int del[10][10];

    int T, g, h;
    int C, D, N;
    //printf("1");
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        for(i=0; i<8; i++)
            for(j=0; j<8; j++){
                com[i][j]=0;
                del[i][j]=0;
            }
    //printf("2");
        scanf("%d ", &C);
        for(h=0; h<C; h++){
            char a, b, c;
            scanf("%c%c%c ", &a, &b, &c);
            com[m[a]][m[b]] = c; 
            com[m[b]][m[a]] = c;
        }

    //printf("3");
        scanf("%d ", &D);
        for(h=0; h<D; h++){
            char a, b;
            scanf("%c%c ", &a, &b);
            del[m[a]][m[b]] = 1;
            del[m[b]][m[a]] = 1; 
        }
    //printf("4");
        scanf("%d ", &N);
        x.clear();
        for(i=0; i<N; i++){
            //printf("i vale %d\n", i);
            char a;
            scanf("%c", &a);
            //printf("a vale %c\n", a);
            int mudei =0;
    
            if(x.empty()){
                x.push_back(a);
                continue;
            }

            char b = x.back();
    
            if(m[b]!=-1){
                if(com[m[a]][m[b]]!=0){
                    x.pop_back();
                    x.push_back(com[m[a]][m[b]]);
                    mudei=1;
                }
            }
            if(mudei==0){
                int k = x.size();
                for(j=0; j<k; j++){
                    if(del[m[a]][m[x[j]]] == 1){
                        x.clear();
                        mudei=1;
                        break;
                    } 
                }
            }
            if(mudei==0)
                x.push_back(a);
        }
        printf("Case #%d: [", g);
        int r = x.size();
        for(j=0; j<r; j++){
            printf("%c", x[j]);
            if(j!=r-1)
            printf(", ");
        }
        printf("]\n");
        scanf(" ");
    }
    return 0;
}
