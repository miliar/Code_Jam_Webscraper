#include<cstdio>
#include<cstring>

using namespace std;

typedef char Raw[4];

Raw Mat[4];

bool check(char);
int pro(int );

int main(){
    int  n;
    char c;
    //freopen("IN","r",stdin);
    freopen("OUT","w",stdout);

    scanf("%d",&n);
    getchar();

    for(int k=1;k!=n+1;k++){
        memset(Mat,0,sizeof(Mat));
        for(int i=0;i!=4;i++){
            for(int j=0;j!=4;j++)
                scanf("%c",&Mat[i][j]);
            getchar();
        }
        getchar();
        pro(k);
    }
}

bool check(char c){
    bool p;
    for(int i=0;i!=4;i++){
        p    = true;
        for(int j=0;j!=4;j++){
            if(!(Mat[i][j]==c || Mat[i][j]=='T')){
                p = false;
                break;
            }
        }
        if(p)
            return true;
    }
    

    for(int j=0;j!=4;j++){
         p = true;
        for(int i=0;i!=4;i++){
            if(!(Mat[i][j]==c || Mat[i][j]=='T')){

                p = false;
                break;
            }
        }
            if(p)
                return true;
    }
    
    p = true;
    for(int i=0;i!=4;i++)
        if(!(Mat[i][i]==c || Mat[i][i]=='T')){
            p = false;
            break;
        }
    if(p)
        return true;
    p = true;
    for(int i=0;i!=4;i++)
        if(!(Mat[i][3-i]==c || Mat[i][3-i]=='T')){
            p = false;
            break;
        }
    if(p)
        return true;
    return false;
}

int pro(int k){
    
    if(check('O')){
        printf("Case #%d: %c won\n",k,'O');
        return 0;
    }
    else
        if(check('X')){
            printf("Case #%d: %c won\n",k,'X');
            return 0;
        }
            
    for(int i=0;i!=4;i++)
        for(int j=0;j!=4;j++)
            if(Mat[i][j]=='.'){
                printf("Case #%d: Game has not completed\n",k);
                return 0;
            }
    printf("Case #%d: Draw\n",k);
    return 0;
}

        
        
           
        
            
                

            
                

                
