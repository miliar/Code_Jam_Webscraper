#include <stdio.h>
int main()
{
    int t,T,d,nx,no,nt,i,j,f;
        char tik[4][4],w;
        scanf("%d",&T);
        for(t=1;t<=T;t++)
        {       
                f=0;
                d=0;
                for(i=0;i<4;i++)
                        scanf("%s",tik[i]);
                for(i=0;i<4;i++){       
                        nx=no=nt=0;
                        for(j=0;j<4;j++){
                                switch(tik[i][j]){
                                        case '.': d++; break;
                                        case 'T' : nt++; break;
                                        case 'X': nx++;break;
                                        case 'O': no++; break;
                                }
                        }
                        if(nx+nt==4) {printf("Case #%d: X won\n",t); f=1; break;}
                        if(no+nt==4) {printf("Case #%d: O won\n",t); f=1; break;}
                }
                if(f==0){
                        for(i=0;i<4;i++){       
                                nx=no=nt=0;
                                for(j=0;j<4;j++){
                                        switch(tik[j][i]){
                                                case '.': d++; break;
                                                case 'T' : nt++; break;
                                                case 'X': nx++;break;
                                                case 'O': no++; break;
                                        }
                                }
                                if(nx+nt==4) {printf("Case #%d: X won\n",t); f=1; break;}
                                if(no+nt==4) {printf("Case #%d: O won\n",t); f=1; break;}
                        }
                }
                if(f==0){
                        nx=no=nt=0;
                        for(i=0;i<4;i++){       
                                switch(tik[i][i]){
                                        case '.': d++; break;
                                        case 'T' : nt++; break;
                                        case 'X': nx++;break;
                                        case 'O': no++; break;
                                }
                        }       
                        if(nx+nt==4) {printf("Case #%d: X won\n",t); f=1;}
                        else if(no+nt==4) {printf("Case #%d: O won\n",t); f=1;}
                }
                if(f==0){
                        nx=no=nt=0;
                        for(i=0;i<4;i++){       
                                switch(tik[i][3-i]){
                                        case '.': d++; break;
                                        case 'T' : nt++; break;
                                        case 'X': nx++;break;
                                        case 'O': no++; break;
                                }
                        }       
                        if(nx+nt==4) {printf("Case #%d: X won\n",t); f=1;}
                        else if (no+nt==4) {printf("Case #%d: O won\n",t); f=1;}
                }
                if(f==0){
                        if(d==0) printf("Case #%d: Draw\n",t);
                        else printf("Case #%d: Game has not completed\n",t);
                }       
                
        }
        return 0;
}