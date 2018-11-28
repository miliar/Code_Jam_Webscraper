#include <stdio.h>
#include <conio.h>
#include <string.h>

FILE *fo;
FILE *fp;
int count = 0;
int chk;


int isHappy(int num,int base){
    int temp = num;
    int colect = 0;
    int remainder = 0;
    if(num < base*base*base)
    chk = 1;
    if(chk)
    count++;
    while(num >= base){
        remainder = num%base;
        // printf("\nr = %d   , n = %d   ,  collect = %d\n",remainder,num,colect);
        num = num/base;
        colect += remainder*remainder;
      //  printf("\nr = %d   , n = %d   ,  collect = %d\n",remainder,num,colect);
    }
    colect += num*num;
    if(colect == 1) return 1;
    if(count > base*base*base) return 0;
    return isHappy(colect,base);
}

int main(){
    int T,num,table[11];
    char temp;
    fo = fopen("A-small-attempt3.in","r"); 
    fp = fopen("A-small-attempt3.out","w"); 
    fscanf(fo,"%d",&T);
    fscanf(fo,"%c",&temp);
    for(int z = 1 ; z <= T; z++){
              for(int i=0;i<=10;i++)
              table[i] = 0;
              temp = ' ';
            while(temp != '\n'){
                    fscanf(fo,"%c",&temp);
                    if(temp >= '0' && temp <= '9'){
                            if(temp == '1' || temp == '0')
                            table[10] = 1;
                            else
                            table[temp-48] = 1;
                    }
            }
            
            for(int j = 2;1;j++){
            int check = 1;
                    for(int i = 2; i <=10 && check;i++){
                            if(table[i]){
                                      count = 0;   
                                      chk = 0;
                                      check = isHappy(j,i);
                              }
                    }
                    if(check == 1){
                             num = j;
                             break;
                    }
            }
            fprintf(fp,"Case #%d: %d\n",z,num);        
    }
fclose(fo);
fclose(fp);
//while(1);
return 0;
}
