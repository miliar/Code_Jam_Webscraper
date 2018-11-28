#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    int i,j,k,T;
    char norm[30], rese[30];
    FILE* fout = fopen("rese.out","w");
    FILE* fin = fopen("rese.in","r");
    
    for (i=0;i<=25;++i){
        norm[i] = 'a'+i;
    }
    
    rese[0] =  'y'     ; //a
    rese[1] =  'h'     ; //b
    rese[2] =  'e'     ; //c
    rese[3] =  's'     ; //d
    rese[4] = 'o'      ; //e
    rese[5] =  'c'     ; //f
    rese[6] =   'v'    ; //g
    rese[7] =    'x'   ; //h
    rese[8] =   'd'    ; //i
    rese[9] =  'u'     ; //j
    rese[10] =  'i'     ; //k
    rese[11] =  'g'     ; //l
    rese[12] =  'l'     ; //m
    rese[13] =  'b'     ; //n
    rese[14] =  'k'     ; //o
    rese[15] = 'r'      ; //p
    rese[16] =  'z'     ; //q
    rese[17] =   't'    ; //r
    rese[18] =  'n'     ; //s
    rese[19] =  'w'     ; //t
    rese[20] =  'j'     ; //u
    rese[21] =  'p'     ; //v
    rese[22] =  'f'     ; //w
    rese[23] =  'm'     ; //x
    rese[24] = 'a'      ; //y
    rese[25] =  'q'     ; //z
    
    char haha[3];
    fscanf(fin,"%d",&T);
    fgets(haha,12,fin);

    for (i=1;i<=T;++i){
        char str[200]={0};
        char after[200]={0};
        fgets(str,200,fin);
        //printf("\n\n%s\n\n halo \n",str);
        for (j=0;j<strlen(str);++j)
        {
            int temp = str[j]-'a';
            if  (temp >= 0 && temp <= 25)
            {
                after[j] = rese[temp];
            }
            else after[j] = str[j];
                        
        }
        
        after[j] = 0;
        fprintf(fout,"Case #%d: %s",i,after);
    }
    

}
    
