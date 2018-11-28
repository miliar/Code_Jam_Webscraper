#include <cstdio>

using namespace std;

int main(){
    int i,j,k,l,mo,mx,n,o,p,pxw,pow;
    char c;
    int pole[4][4];
    
    scanf("%d",&n);
    
    for(l=0;l<n;l++){
        k=0;
        pxw=0;
        pow=0;
        c=getchar();
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                c=getchar();
                while(c=='\n'){
                    c=getchar();
                }
                switch(c){
                    case '.':
                        pole[i][j]=0;
                        k++;                        
                        break;
                    case 'X':
                        pole[i][j]=1;                        
                        break;
                    case 'O':
                        pole[i][j]=2;                        
                        break;
                    case 'T':
                        pole[i][j]=3;                        
                        break;
                }
            }
        }
        for(i=0;i<4;i++){
            mx=0;
            mo=0;
            for(j=0;j<4;j++){
                if((pole[i][j]==1)||(pole[i][j]==3)){
                    mx++;
                }
                if((pole[i][j]==2)||(pole[i][j]==3)){
                    mo++;
                }
            }
            if(mo==4){
                pow=1;
                break;
            }
            if(mx==4){
                pxw=1;
                break;
            }
        }
        for(j=0;j<4;j++){
            mx=0;
            mo=0;
            for(i=0;i<4;i++){
                if((pole[i][j]==1)||(pole[i][j]==3)){
                    mx++;
                }
                if((pole[i][j]==2)||(pole[i][j]==3)){
                    mo++;
                }
            }
            if(mo==4){
                pow=1;
                break;
            }
            if(mx==4){
                pxw=1;
                break;
            }
        }
        
        mx=0;
        mo=0;
        for(i=0;i<4;i++){
            if((pole[i][i]==1)||(pole[i][i]==3)){
                mx++;
            }
            if((pole[i][i]==2)||(pole[i][i]==3)){
                mo++;
            }
        }
        if(mo==4){
            pow=1;
        }
        if(mx==4){
            pxw=1;
        }
        
        mx=0;
        mo=0;
        for(i=0;i<4;i++){
            if((pole[i][3-i]==1)||(pole[i][3-i]==3)){
                mx++;
            }
            if((pole[i][3-i]==2)||(pole[i][3-i]==3)){
                mo++;
            }
        }
        if(mo==4){
            pow=1;
        }
        if(mx==4){
            pxw=1;
        }
        
        if(pxw==1){
            printf("Case #%d: X won\n",l+1);
        }
        if(pow==1){
            printf("Case #%d: O won\n",l+1);
        }
        if((pxw==0)&&(pow==0)){
            if(k==0){
                printf("Case #%d: Draw\n",l+1);
            }else{
                printf("Case #%d: Game has not completed\n",l+1);
            }
        }
    }
    
    return 0;
}
