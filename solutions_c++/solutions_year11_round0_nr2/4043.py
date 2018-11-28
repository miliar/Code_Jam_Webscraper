 #include <stdio.h>
 #include <conio.h>
 #include <string.h>

 int fct(char *t,char c)
 {

     int ok=0;
     for(char *p=t;*p;p++)
     if(*p==c){*p='*';ok=1;}
     return ok;
 }
 int main()
 {
     FILE *in =fopen("B-small.in","r");
     FILE *out=fopen("B-small.out","w");
     
     int nombrecas;
     
     fscanf(in,"%d\n",&nombrecas);
     int i;
     for(int i=0;i<nombrecas;i++)
     {
             int x;
             char a=0,b=0,c=0;
             char o=32,p=32;
             char l;
             char tab[150]="";
             int taille=0;
             
             fscanf(in,"%d",&x);
             if(x==1)
             fscanf(in," %c%c%c",&a,&b,&c);
             
             fscanf(in," %d",&x);
             if(x==1)
             fscanf(in," %c%c",&o,&p);
             
             fscanf(in," %d",&x);
             if(x>0)
             {
             fscanf(in," %c",&l);
                tab[taille++]=l;tab[taille]=0;
             }
             
             for(int ff=1;ff<x;ff++)
             {
                fscanf(in," %c",&l);
                if(l==a&&tab[taille-1]==b||l==b&&tab[taille-1]==a)tab[taille-1]=c;
                else 
                {
                if(l==o&&fct(tab,p) || l==p&&fct(tab,o))
                
                l='*';
                
                
                
  
                          
    
                tab[taille++]=l;tab[taille]=0;
    
                }
                
             }

             strcpy(tab,strrev(tab));
             char *t;
             for( t=tab;*t&&*t!='*';t++);
             *t=0;
             strcpy(tab,strrev(tab));
             fprintf(out,"Case #%d: [",i+1);
             if(*tab)
             {
                             fprintf(out,"%c",*tab);     
             for( t=tab+1;*t;t++)
             
             fprintf(out,", %c",*t);
             
             }
            if(nombrecas-i==1) fprintf(out,"]");
            else
            fprintf(out,"]\n");
             


                         
             
             
                     
                          
             
             
     }
     

     
     
   
     
     
     
     return 0;
 }
