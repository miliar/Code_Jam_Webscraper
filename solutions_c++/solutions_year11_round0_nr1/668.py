#include<stdio.h>
#include<stdlib.h>
int A[1005][2];
int ABS(int a){
    if(a > 0)return a;
    else return -1*a;
}
int main (){
    int T,n,x,y,tmp,nowa,nowb,ans,ca=0,i,j,pos;
    char ch;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        x=0;y=0;
        for(i=0;i<n;i++){
            scanf("%*c%c%d",&ch,&A[i][0]);
            if(ch == 'O'){A[i][1] = 0;}
            if(ch == 'B'){A[i][1] = 1;}
        }
        nowa = 1;
        nowb = 1;
        ans = 0;
        for(i=0;i < n;i++){
            //printf("nowa %d nowb %d ans %d\n",nowa,nowb,ans);
            if(A[i][1] == 0){
                ans += ABS(nowa - A[i][0])+1;
                
                pos = -1;
                for(j=i;j<n;j++){
                    if(A[j][1] == 1){pos = j;break;}
                }
                if(pos != -1){
                    if(A[pos][0] > nowb){
                        if(ABS(A[pos][0] - nowb) <= ABS(nowa - A[i][0])+1)
                            nowb = A[pos][0];
                        else{
                            nowb += ABS(nowa - A[i][0])+1;
                        }
                    }else{
                        if(ABS(A[pos][0] - nowb) <= ABS(nowa - A[i][0])+1)
                            nowb = A[pos][0];
                        else{
                            nowb -= ABS(nowa - A[i][0])+1;
                        }
                    }
                }
                nowa = A[i][0];
            }else{
                ans += ABS(nowb - A[i][0])+1;
                
                pos = -1;
                for(j=i;j<n;j++){
                    if(A[j][1] == 0){pos = j;break;}
                }
           //     printf("pos %d\n",pos);
                if(pos != -1){
                    if(A[pos][0] > nowa){
                        if(ABS(A[pos][0] - nowa) <= ABS(nowb - A[i][0])+1)
                            nowa = A[pos][0];
                        else{
                            nowa += ABS(nowb - A[i][0])+1;
                        }
                    }else{
                        if(ABS(A[pos][0] - nowa) <= ABS(nowb - A[i][0])+1)
                            nowa = A[pos][0];
                        else{
                            nowa -= ABS(nowb - A[i][0])+1;
                        }                    
                    }
                }
                nowb = A[i][0];                
            }
        }
        ca++;
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}

/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
