#include<stdio.h>
char arr[255];
int size=0;
char peek(){
     if(size>0)     return arr[size-1];
     else return -1;
}
void push(char c){
     arr[size]=c;
     size++;
}
char pop(){
     if(size>0){
                size--;
                return arr[size];
     }
}
void clear(){
     size=0;
}
int find(char c){
    int i;
    for(i=0;i<size;i++){
                        if(arr[i]==c)return 1;
    }
    return 0;
}

int main(){
    int T;
    int i,j,k,length,combine,oppose;
    char temp;
    char test[110];
    char str[100];
    char combineList[36][4];
    char opposeList[28][3];
    scanf("%d",&T);
    
    for(i=0;i<T;i++){
                     size=0;
                     
                     scanf("%d",&combine);
                    // printf("%d",combine);
                     for(j=0;j<combine;j++){
                         scanf("%s ",combineList[j]);
                         //printf("%s",combineList[j]);
                     }
                      scanf("%d",&oppose);
                                        //   printf("%d",oppose);
                     for(j=0;j<oppose;j++){
                         scanf("%s ",opposeList[j]);
                          //printf("%s",opposeList[j]);
                     }
                     scanf("%d",&length);
                     scanf("%s",str);//gets(str);
                     // printf("%s",str);
                     push(str[0]);
                     for(j=1;j<length;j++){
                            temp=peek();
                            if(temp==-1){
                                         push(str[j]);
                                         continue;
                            }
                            for(k=0;k<combine;k++){
                                 if((combineList[k][0]==temp && combineList[k][1]==str[j])||(combineList[k][1]==temp && combineList[k][0]==str[j])){
                                                           pop();
                                                           push(combineList[k][2]);
                                                           
                                                           break;
                                 }
                            }
                            if(k<combine)continue;
                            for(k=0;k<oppose;k++){
                                                  if((opposeList[k][0]==str[j] && find(opposeList[k][1])) ||(opposeList[k][1]==str[j] && find(opposeList[k][0]))){
                                                                           clear();
                                                                           break;
                                                  }
                            }
                            if(k<oppose)continue;
                            push(str[j]);       
                     }
                     printf("Case #%d: [",i+1);
                     for(j=0;j<size;j++){
                                         printf("%c",arr[j]);
                                         if(j<size-1)printf(", ");
                     }
                     printf("]\n");
                     
    }
    
}
