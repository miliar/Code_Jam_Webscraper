#include <iostream>
#define TASK "A"
#define Small "-small-attempt"
#define NUM "0"
#include <string>
#include <map>
#include <set>

using namespace std;

int test;
int n;
char c[10][10];
int answer;
bool hasEmpty;

int dx[8] = { 0,-1, 1, 0, 1,-1,-1, 1};
int dy[8] = {-1, 0, 0, 1,-1, 1,-1, 1};

bool checkwon(char x){
    for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
            if (i==0 || j==0 || i==3 || j==3){                
                for (int k=0;k<8;k++){
                    bool res = true;
                    for (int l=0;l<4;l++){
                        int nx = i+dx[k]*l;
                        int ny = j+dy[k]*l;
                        if (nx<0 || ny<0 || nx>=4 || ny>=4)
                        {                            
                            res = false;
                            break;                                  
                        }  
                        
                        if (c[nx][ny]!=x && c[nx][ny]!='T')
                        {
                            res = false;
                            break;                                  
                        }                          
                    }    
                    if (res)
                    {
                        //printf("%i,%i - %c - %i\n",i,j,x, k );
                        return true;                             
                    }
                }    
            }    
    return false;    
}

void readinput(){
    hasEmpty = false;
    for (int i=0;i<4;i++)
    {
        for (int j=0;j<4;j++){
            scanf("%c",&c[i][j]);   
            if (c[i][j]=='.') hasEmpty = true; 
        }   
        scanf("\n");
    }    
    scanf("\n");
}

void solve(){
    answer = 0;
    if (checkwon('X')) answer=1; else
    if (checkwon('O')) answer=2; else
    if (!hasEmpty) answer = 3;             
}

void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    if (answer == 0) printf("Game has not completed\n"); else
    if (answer == 1) printf("X won\n"); else
    if (answer == 2) printf("O won\n"); else
    printf("Draw\n");
}

int main(void){
    //freopen("input.txt","r",stdin);    
    //freopen(TASK""Small""NUM".in","r",stdin);
    freopen(TASK"-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%i\n",&test);
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
