#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define DIGILEN 22

int main(){
    int i, j;
    int cases;
    char input[DIGILEN], output[DIGILEN];
    int num[10];
    int now, small;
    
    //input T
    scanf("%d", &cases);
    
    for(i=0; i<cases; i++){
        //input a case
        scanf("%s", input);
        memcpy(output, input, strlen(input));
        output[strlen(input)]='\0';

        //big to small 511
        for(j=strlen(input)-2; j>-1; j--){
            now=input[j];
            small=input[j+1];
            if(j==strlen(input)-2 && now<small){//case 2 digi && in order
                output[j]=input[j+1]; //de order
                output[j+1]=input[j];
                break;                
            }else if(j<strlen(input)-2 && now<small){
                //printf("j %d input[j] %d\n", j, input[j]);
                //know 1 to 9            
                for(int x=0; x<10;x++){
                    num[x]=0;
                }  
                for(int k=j; k<strlen(input); k++){
                    //printf("k %d in %d di %d\n", k, input[k], input[k]-'0');
                    num[input[k]-'0']++;
                }
                for(int x=0; x<10;x++){
                    //printf("d%d=%d ", x, num[x]);
                }                
                //printf("\n===digit===\n");
                for(int k=now-'0'+1; k<10; k++){
                    if(num[k]!=0){//just bigger
                        int runi=j+1;
                        output[j]=k+'0';
                        num[k]--;
                        //printf("k %d numk %d\n", k, num[k]);
                        //in-order
                        for(int x=0; x<10;x++){//??
                            while(num[x]>0){
                                output[runi]=x+'0';
                                //printf("runi %d output[runi] %d x %d num[x] %d\n", runi, output[runi]-'0', x, num[x]);
                                runi++;                                
                                num[x]--;
                            }
                        }
                        break;            
                    }
                }
                break;
            }
        }
        if(j==-1){//de order
                for(int x=0; x<10;x++){//be zero
                    num[x]=0;
                }  
                for(int k=0; k<strlen(input); k++){
                    //printf("k %d in %d di %d\n", k, input[k], input[k]-'0');
                    num[input[k]-'0']++;
                }
                for(int x=0; x<10;x++){
                    //printf("d%d=%d ", x, num[x]);
                }   
                for(int k=1; k<10; k++){
                    if(num[k]!=0){//smallest
                        int runi=2;
                        output[0]=k+'0';
                        output[1]='0';
                        num[k]--;
                        //in-order
                        for(int x=0; x<10;x++){
                            while(num[x]>0){
                                output[runi]=x+'0';
                                runi++;                                
                                num[x]--;
                            }
                        }
                        output[strlen(input)+1]='\0';
                    }
                }
        }
        //output
        printf("Case #%d: %s\n", i+1, output);
    }

    return 0;
}
