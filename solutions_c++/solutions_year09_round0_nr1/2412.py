#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node node;

struct node{
    char elem[50];
    int nelem;
};
char strvalues[5000][20];

node palavra[20];

int l,d,n;
int cont;

void buildTree(char *avalia){
    //printf("oi");
    int index =0;    
    int i,j=0;
    int len = strlen(avalia);
    //printf("%s\n\n\n",avalia);
    for(i=0;i<len;i++){
        palavra[index].nelem = 0;
        if(avalia[i] == '('){
            i++;
            j=0;
            while(avalia[i]!=')'){
                palavra[index].elem[j] = avalia[i];
                palavra[index].nelem++;
                j++;
                i++;
            }
            index++;
        }
        else{
            palavra[index].elem[0] = avalia[i];
            palavra[index].nelem = 1;
            index++;
        }
    }
}



void checkBelong(){
    int i,j,p;
    bool flag;
    int index;
      // printf("oi");
    bool ok;
    for(p=0;p<d;p++){
        flag = false;
        for(i=0;i<l;i++){
            ok = false;
            for(j=0;j<palavra[i].nelem;j++){
                if(strvalues[p][i] == palavra[i].elem[j]) ok = true;
            }
            if(ok==false) flag = true;
        }
        if(flag == false){
            cont++;
       //     printf("\n--- --- --- %s\n",strvalues[p]);
        }
    }    
}



int main(){
//    char avalia[500];
    char aux[15];
    scanf("%d %d %d",&l,&d,&n);

    int i,j;


    for(i=0;i<d;i++){
        scanf("%s",&strvalues[i][0]);
    }
    
    /*for(i=0;i<d;i++){
        printf("%s\n",strvalues[i]);
    }*/
   // qsort (strvalues, d, 15, (int(*)(const void*,const void*)) strcmp);
 /*   printf("\n\n\n");
    for(i=0;i<d;i++){
        printf("%s\n",strvalues[i]);
    }
    */
    for(i=0;i<n;i++){
        char avalia[1000];
        for(int m=0;m<20;m++){
            palavra[m].nelem = 0;
            for(int o=0;o<25;o++){
                palavra[m].elem[o] = '0';
            }
        }
        
        scanf("%s",avalia);        
        buildTree(avalia);
        
        cont = 0;
        
        checkBelong();
        

        //printf("\n\n\n");
      //  printf("%s",avalia);
        
        /*for(int j=0;j < l;j++){
            for(int k=0;k< palavra[j].nelem;k++){
                printf("%d %c  ",k,palavra[j].elem[k]);              
            }
            printf("\n");
        }*/
        printf("Case #%d: %d\n",i+1,cont);
        
        
      
        
    }
    
   // scanf("%d",&l);
    
    return 0;
}
