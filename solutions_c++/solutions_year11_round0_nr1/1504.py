#include<stdio.h>
#include<stdlib.h>

int v[105];
char s[105];

int main(){
    int T, N;
    int i, g, h;
    int tempo;
    int t[3];
    int p[3];
    scanf("%d ", &T);
    for(g=0; g<T; g++){
        scanf("%d ", &N);
        for(h=0; h<N; h++){
            char a;
            int x;
            scanf("%c %d ", &a, &x);
            v[h]=x;
            if(a=='O') s[h]=1;
            else if(a=='B') s[h]=2;        
        }
        tempo = 0;
        t[1]=0, t[2]=0;
        p[1]=1, p[2]=1;
        for(i=0; i<N; i++){
            int m = abs(v[i]-p[s[i]]);
            //printf("i=%d, m =%d, s[i]=%d v[i]=%d t[1]=%d t[2]=%d tempo=%d\n", i, m, s[i], v[i], t[1], t[2], tempo);
            p[s[i]] = v[i];
            t[s[i]] = t[s[i]]+m+1;
            if(i>=1){
                if(s[i]!=s[i-1]){
                    int ai=0;
                    if(t[s[i]]>t[s[i-1]]){
                        ai=1;
                        tempo = tempo + t[s[i]] - t[s[i-1]];
                    }
                    else
                        tempo = tempo +1;
                    if(ai==1){
                        t[s[i]] = t[s[i]] - t[s[i-1]];
                    }   
                    else
                        t[s[i]] = 1;
                    t[s[i-1]]=0;
                }
                else{
                    tempo = tempo + m + 1; 
                }
            }
            else if(i==0){
                tempo = tempo + m + 1; 
            }
        }
        printf("Case #%d: %d\n", g+1, tempo); 
    }

return 0;
}
