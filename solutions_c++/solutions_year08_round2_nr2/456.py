#include <stdio.h>


int contor,NrCazuri,retin,ok,maresc;
long a,b,p,nr_seturi,i,nr;
char vector[100002];

int main()
 {FILE *f,*g;


  f=fopen("intrare.in","r");
  g=fopen("iesire.out","w");


  fscanf(f,"%d",&NrCazuri);
  for (contor=1;contor<=NrCazuri;contor++)
     {fscanf(f,"%ld %ld %ld",&a,&b,&p);
      nr_seturi=0;
      for (i=a;i<=b;i++)
         vector[i]='0';
      for (nr=p;nr<=b;nr++)
          {ok=0;
           for (i=2;i<=nr/2;i++)
             if (nr%i==0) {ok=1;i=nr;}
           if (ok==0) {retin=0;
                       for (i=a;i<=b;i++)
                             if (i%nr==0) {retin=i;i=b+1;}
                       if (retin!=0) {maresc=0;
                                      for (i=retin;i<=b;i=i+nr)
                                                {if (vector[i]=='1') maresc=1;
                                                 vector[i]='1';
                                                 }
                                      if (maresc==0) nr_seturi++;
                                      }
                       //if (retin==0) nr=b+1;
                       }
           }
      for (i=a;i<=b;i++)
          if (vector[i]=='0') nr_seturi++;
      fprintf(g,"Case #%d: %ld\n",contor,nr_seturi);
      }

   fclose(f);
   fclose(g);

   return 0;

   }
