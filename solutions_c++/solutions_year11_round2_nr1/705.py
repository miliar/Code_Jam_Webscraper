#include <iostream>
#define TASK "A"
#define Small "-small-attempt"
#define NUM "0"
#include <string>
#include <map>
#include <set>

using namespace std;

#define N 200

int test;

int n;
char a[N][N];
double coef[N][3];


void readinput(){
    scanf("%i\n",&n);
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            scanf("%c",&a[i][j]);        
        }   
        scanf("\n"); 
    }   
}

void solve(){
    //WP
    for (int i=0;i<n;i++){
        int all = 0;
        int win = 0;
        coef[i][0]=0;
        for (int j=0;j<n;j++){
            if (a[i][j]!='.') all++;
            if (a[i][j]=='1') win++;    
        }    
        if (all>0){
            coef[i][0]=(win+0.0)/all;    
        }
    }
    //OWP
    for (int i=0;i<n;i++){
        coef[i][1]=0;
        int cc = 0;
        for (int j=0;j<n;j++)
            if (i!=j && a[i][j]!='.'){
                cc++;
                int all = 0;
                int win = 0;
                for (int k = 0;k<n;k++){
                    if (k!=i){
                        if (a[j][k]!='.') all++;
                        if (a[j][k]=='1') win++;        
                    }
                }
                double add = 0;
                if (all>0){
                    add = (win+0.0)/all;
                }
                coef[i][1]+=add;                            
            }    
        coef[i][1]/=cc;
    }
    //OOWP
    for (int i=0;i<n;i++){
        coef[i][2]=0;
        int cc = 0;
        for (int j = 0;j<n;j++){
            if (a[i][j]!='.'){
                cc++;
                coef[i][2]+=coef[j][1];
            }    
        }    
        coef[i][2]/=cc;
    }
}

void writeoutput(int t){
    printf("Case #%i:",t+1);            
    printf("\n");
    for (int i=0;i<n;i++){
        printf("%.6lf\n",0.25*coef[i][0]+0.5*coef[i][1]+0.25*coef[i][2]);    
    }
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
