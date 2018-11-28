#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

int n, m;
char s[100];
int res[10000];
char p[40][130];

string check(char x){
   if (x == '0') return "0000";
   if (x == '1') return "0001";
   if (x == '2') return "0010";
   if (x == '3') return "0011";
   if (x == '4') return "0100";
   if (x == '5') return "0101";
   if (x == '6') return "0110";
   if (x == '7') return "0111";
   if (x == '8') return "1000";
   if (x == '9') return "1001";
   if (x == 'A') return "1010";
   if (x == 'B') return "1011";
   if (x == 'C') return "1100";
   if (x == 'D') return "1101";
   if (x == 'E') return "1110";
   if (x == 'F') return "1111";
}

void init(){
    scanf("%d%d",&n, &m);
    for (int i = 0; i < n; ++i){
        scanf("%s",s);
        for (int j = 0; j < m / 4; ++j){
            string tmp = check(s[j]);
            int now = 0;
            for (int k = j * 4; k < (j + 1) * 4; ++k){
               p[i][k] = tmp[now++];
            }
        }
    }  
    //for (int i = 0; i < n; ++i){
    //    for (int j = 0; j < m; ++j) printf("%c",p[i][j]);
    //    puts("");
    //}
    
}

void run(){
    memset(res, 0, sizeof(res));
    int minn = min(n, m);
    int total = 0;
    
    while (true){
        bool f = false;
        for (int l = minn; l >= 1; --l){  
            for (int i = 0; i < n; ++i){
                if (f) break;
                for (int j = 0; j < m; ++j){
                    if (f) break;
                    if (p[i][j] == '*') continue;
                    {
                        bool flag = true;
                        char ch = p[i][j];
                        
                        for (int w = i; w < i + l; ++w){
                            if (flag == false) break;
                            for (int v = j; v < j + l; ++v)
                                if (p[w][v] == '*'){
                                   flag = false;
                                   break;
                                }
                                else if (p[w][v] != ch && (((w + v) % 2) == ((i + j) % 2))){
                                   flag = false;
                                   break;
                                }else if (p[w][v] == ch && (((w + v) % 2) != ((i + j) % 2))){
                                   flag = false;
                                   break;
                                }    
                        }
                        
                        if (flag){
                           if (res[l] == 0) total++;
                           res[l]++;
                           f = true;
                           for (int w = i; w < i + l; ++w)
                              for (int v = j; v < j + l; ++v) p[w][v] = '*';
                           break;
                        }
                        
                    }    
                }  
            }
        }
        if (f == false) break;
    }     
    printf("%d\n",total);
    for (int i = minn; i >= 1; --i) if (res[i] > 0) printf("%d %d\n",i, res[i]);
}

int main(){
    int t;
    freopen("C.in", "r",stdin);
    freopen("C.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 0; i < t; ++i){
        printf("Case #%d: ",i + 1);
        init();
        run();    
    }
    return 0;
}
