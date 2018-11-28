#include "data.h"

Data::Data(string filename){
                file=fopen(filename.c_str(),"r");
                resultFile=fopen("result.txt","w");
                
                unknow=NULL;dict=NULL;
                int i;
                int unknowRowLen;
                //L dlugosc slowa
                //D ilosc slow
                //N ilosc niepewnych slow
                fscanf(file,"%d %d %d",&l,&d,&n);
                printf("%d %d %d",l,d,n);
                dict=new char*[d];
                //najpierw  slowa
                for(i=0;i<d;i++){
                    *(dict+i)=new char[n];
                    fscanf(file,"%s",*(dict+i));
                    //printf("%s\n",*(dict+i));
                }
                //teraz nieznane slowa
                unknow=new char*[n];
                unknowRowLen=20000;//l*l+2*l;
                for(i=0;i<n;i++){
                   *(unknow+i)=new char[unknowRowLen];                     
                   fscanf(file,"%s",*(unknow+i));
                   //printf("%s\n",*(unknow+i));
                }         
}
//obliczam
string Data::Calculate(void){
   int i,j,k,m,pos,wordsFound;
   short status;
   char tmp,tmp2;
   bool letterFound=false;
   string result; 
   
   for(i=0;i<n;i++){//po nieznanych slowach
   wordsFound=0;
      for(j=0;j<d;j++){//po slowniku
         k=0; pos=0;status=0;
         tmp=*(*(unknow+i)+k);
         while(tmp!=0){ 
             if(tmp=='('){
                m=1;letterFound=false;
                while((tmp2=*(*(unknow+i)+k+m))!=')'){
                   if(tmp2==*(*(dict+j)+pos)){
                      letterFound=true; 
                   }
                   m++;                         
                }
                if(letterFound)status++;
                pos++;k+=m+1;          
             }else{
                if(tmp==*(*(dict+j)+pos))status++;
                pos++;k++;  
             }                   
                   
             tmp=*(*(unknow+i)+k);             
         } 
         if(status==l)wordsFound++;        
      }              
     result+=fprintf(resultFile,"Case #%d: %d\n",i+1,wordsFound);     
   }
   return result;
   
       
}
Data::~Data(){
              if(unknow!=NULL&&dict!=NULL){
              int i;
              for(i=0;i<d;i++)delete []*(dict+i);
              delete []dict;   
              for(i=0;i<n;i++)delete []*(unknow+i);
              delete []unknow;
              }
              fclose(file);
              fclose(resultFile);               
              }
