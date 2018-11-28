#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <string>
#include <vector>

using namespace std;

int n,w,h,r1,r2,r3,r4;
    int m[101][101];
    char m2[101][101];
    
void reemplaza(char a,char b){
        for (int j=0;j<h;j++){
            for (int i=0;i<w;i++){
                if (m2[j][i]==a)
                   m2[j][i]=b;
                }
            }
     }
     
void muestra(){
        for (int j=0;j<h;j++){
            for (int i=0;i<w;i++){
                printf("%c ",m2[j][i]);
                }
            printf ("\n");
            }    
     printf ("\n");   
     getch();       
     }

int main(void){
    

    char t='a';
    FILE *out, *in;
    in=fopen("c://2.in","r");
    out=fopen("2.out","w");
//    scanf("%d\n",&n);
   fscanf(in,"%d\n",&n);

    for (int k=0;k<n;k++){
        t='a';
//        scanf("%d %d\n",&h,&w);
        fscanf(in,"%d %d\n",&h,&w);        
        for (int j=0;j<h;j++){
            for (int i=0;i<w;i++){
//                scanf("%d",&m[j][i]);
                  fscanf(in,"%d",&m[j][i]);
                m2[j][i]='0';
                }
            }
        printf("Case #%d:\n",k+1);      
        fprintf(out,"Case #%d:\n",k+1);      
        for (int j=0;j<h;j++){
            for (int i=0;i<w;i++){
                if (m2[j][i]=='0'){
                   m2[j][i]=t;     
                   t++;
                   }
                r1=20000;
                r2=20000;
                r3=20000;
                r4=20000;                
                if (i+1<w) r3=m[j][i+1];
                if (i-1>=0) r2=m[j][i-1];                               
                if (j+1<h) r4=m[j+1][i];
                if (j-1>=0) r1=m[j-1][i];
                
                if (m[j-1][i]<m[j][i]&&r1<=r2&&r1<=r3&&r1<=r4) {
                if (m2[j-1][i]=='0'){
                   m2[j-1][i]=m2[j][i];  
                   }      
                   else{
                        if (m2[j][i]<m2[j-1][i]){
                           reemplaza(m2[j-1][i],m2[j][i]);
                           }
                           else{
                                reemplaza(m2[j][i],m2[j-1][i]);                                
                                }
                        }       
                }
                else if (m[j][i-1]<m[j][i]&&r2<=r1&&r2<=r3&&r2<=r4) {
                if (m2[j][i-1]=='0'){
                   m2[j][i-1]=m2[j][i];  
                   }      
                   else{
                        if (m2[j][i]<m2[j][i-1]){
                           reemplaza(m2[j][i-1],m2[j][i]);
                           }
                           else{
                                reemplaza(m2[j][i],m2[j][i-1]);                                
                                }
                        }       
                }
                else if (m[j][i+1]<m[j][i]&&r3<=r2&&r3<=r1&&r3<=r4){
                if (m2[j][i+1]=='0'){
                   m2[j][i+1]=m2[j][i];  
                   }      
                   else{
                        if (m2[j][i]<m2[j][i+1]){
                           reemplaza(m2[j][i+1],m2[j][i]);
                           }
                           else{
                                reemplaza(m2[j][i],m2[j][i+1]);                                
                                }
                        }       
                }
                else if (m[j+1][i]<m[j][i]&&r4<=r2&&r4<=r3&&r4<=r1){
                if (m2[j+1][i]=='0'){
                   m2[j+1][i]=m2[j][i];  
                   }      
                   else{
                        if (m2[j][i]<m2[j+1][i]){
                           reemplaza(m2[j+1][i],m2[j][i]);
                           }
                           else{
                                reemplaza(m2[j][i],m2[j+1][i]);                                
                                }
                        }       
                }                                                             
                //muestra();
                }
            }

        t='a';
        reemplaza (m2[0][0],t);
        for (int j=0;j<h;j++){
        for (int i=0;i<w;i++){
                if (m2[j][i]>t||m2[j][i]<'a'||m2[j][i]>'z'){
                   t++;
                   reemplaza (m2[j][i],t);
                   }                
                }
            }
        
        for (int j=0;j<h;j++){
            for (int i=0;i<w;i++){
                printf("%c ",m2[j][i]);
                fprintf(out,"%c ",m2[j][i]);
                }
            printf ("\n");
            fprintf (out,"\n");
            }
        }
    getch();
    }
