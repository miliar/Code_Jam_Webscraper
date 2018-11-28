#include <stdio.h>
#include <stdlib.h>

int oige(int a1,int a2,int a3){
    if((a1>=0)&&(a2>=0)&&(a3>=0)){
       if((a1>=a2)&&(a1>=a3)&&(((a1-a2)<=2)||((a1-a3)<=2))) return a1;
       else if((a2>=a1)&&(a2>=a3)&&(((a2-a1)<=2)||((a2-a3)<=2))) return a2;
       else if((a3>=a1)&&(a3>=a2)&&(((a3-a1)<=2)||((a3-a2)<=2))) return a3;
       else return 0;
    }
    else return 0;
}

int suurim(int a1,int a2,int a3,int a4){
    if((a1>=a2)&&(a1>=a3)&&(a1>=a4)) return a1;
    else if((a2>=a1)&&(a2>=a3)&&(a2>=a4)) return a2;
    else if((a3>=a1)&&(a3>=a2)&&(a3>=a4)) return a3;
    else if((a4>=a1)&&(a4>=a2)&&(a4>=a3)) return a4;
}


int kontrolli(int summa,int kas){
   int s1,s2,s3,suurim1,suurim2,suurim3,suurim4;
   if(kas==1){
     s1=(summa+2)/3;
     s2=(summa-s1)/2;
     s3=(summa-s1-s2);
     suurim1=oige(s1,s2,s3);
     s1=(summa-2)/3;
     s2=(summa-s1)/2;
     s3=(summa-s1-s2);
     suurim2=oige(s1,s2,s3);
     s1=(summa+4)/3;
     s2=(summa-s1)/2;
     s3=(summa-s1-s2);     
     suurim3=oige(s1,s2,s3);
     s1=(summa-4)/3;
     s2=(summa-s1)/2;
     s3=(summa-s1-s2);
     suurim4=oige(s1,s2,s3);
     return suurim(suurim1,suurim2,suurim3,suurim4); 
   }
   else if(kas==0){ 
     s1=summa/3;
     s2=(summa-s1)/2;
     s3=(summa-s1-s2);
     if((s1>=s2)&&(s1>=s3)) return s1;
     else if((s2>=s1)&&(s2>=s3)) return s2;
     else if((s3>=s1)&&(s3>=s2)) return s3;
   } 
}

int sorteeri(const void * a, const void * b)
{
    int arv1=*(int*)a;
    int arv2=*(int*)b;
    return arv1-arv2;
}

int main(){
    int rida,imelik,mitu,peab,x;
    FILE* sisse;
    sisse=fopen("input.txt","r");
    FILE* valja;
    valja=fopen("output.txt","w");
    fscanf(sisse,"%d",&rida);
    for(int a=0;a<rida;a++){
       fscanf(sisse,"%d %d %d ",&mitu,&imelik,&peab);
       int jada[mitu];
       int vastus[mitu];
       for(int b=0;b<mitu;b++){
          fscanf(sisse,"%d ",&jada[b]);
       }       
       qsort(jada,mitu,sizeof(int),sorteeri);
       for(x=0;x<imelik;x++){
         vastus[x]=kontrolli(jada[x],1);
         if((vastus[x]==-1)||(vastus[x]<peab)){ 
            vastus[x]=kontrolli(jada[x],0);
            imelik++;
         }
       }
       for(;x<mitu;x++){
         vastus[x]=kontrolli(jada[x],0);
       }
       int tulemus=0;
       for(int e=0;e<mitu;e++){
         if(vastus[e]>=peab) tulemus++; 
       }
       fprintf(valja,"Case #%d: %d\n",a+1,tulemus);
    }
}
