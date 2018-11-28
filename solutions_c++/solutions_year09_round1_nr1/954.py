#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <conio.h>
#include <string>
#include <vector>

using namespace std;

char c[20];
FILE *out, *in;
    
int feliz(int k){
    vector<int> v2;
    vector<int>::iterator it;
    vector<int>::iterator it2;    
    int m,s;
    v2.clear();
    s=0;
    do{
        m=0;
        for (int i=0;c[i]!='\0';i++){
            m+=(c[i]-48)*(c[i]-48);
            }
        it=find(v2.begin(),v2.end(),m);
        if (it==v2.end())
           v2.push_back(m);    
           else
               s=-1;
        itoa(m,c,k);
        }while(s!=-1);
    if (c[0]=='1'&&c[1]=='\0')
       return 1;
       else 
              return 0;
    }



int main(void){
//    in=fopen("testa.in","r");
//    out=fopen("testa.out","w");    
  in=fopen("smalla.in","r");
  out=fopen("smalla.out","w");
//  in=fopen("largea.in","r");
//  out=fopen("largea.out","w");    
    int t,j,f,k;
    char car;   
    vector<int> v; 
    fscanf(in,"%d",&t);
    for (int i=0;i<t;i++){
         v.clear();
         do{
            fscanf(in,"%d",&j);
            v.push_back(j);
            fscanf(in,"%c",&car);
            }while (car==' '&&!feof(in));
         k=2;
         do{
             f=1;
             for (int l=0;l<v.size()&&f==1;l++){
                 itoa(k,c,v[l]);
            //     printf("%d %d %s\n",k,v[l],c);
                 if (feliz(v[l])==0)
                    f=0;           
              //   printf("%d %d %s\n",k,v[l],c);                    
                 }

             k++;
             }while(f!=1);       
         printf("Case #%d: %d\n",i+1,k-1);                    
         fprintf(out,"Case #%d: %d\n",i+1,k-1);     
         }    
    fclose(in);
    fclose(out);  
    printf("listo");  
    getch();
    }
