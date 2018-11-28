 #include <iostream>
 #include <vector>
 #include <algorithm>
 #include <stdio.h>
 
 //using namespace std;
 FILE *f,*g;
 int N;
 char a[510];
 char b[]={"welcome to code jam"};
 int bprim[30],bbb;
 
 int i,j,k,p,lungime;
 int main() {
     f=fopen("C-small.in","r");
     g=fopen("C-small.out","w");
     fscanf(f,"%d ",&N);
 
 for(p=1;p<=N;p++)
    {bbb=0;
     i=0;
     while(bbb==0&&!feof(f)) 
                   {fscanf(f,"%c",&a[i]);
                    if(a[i]=='\n') bbb=1;
                    i++;
                    }  
               
     lungime=i-2;
    //int  lung2=strlen(b);
     for(i=0;i<strlen(b);i++) bprim[i]=0;
     bprim[19]=1;
     for(i=lungime;i>=0;i--) 
                           {
                            for(j=strlen(b)-1;j>=0;j--) //prcurg sirul b
                                                        {
                                                        if(a[i]==b[j])
                                                                {bprim[j]+=bprim[j+1];
                                                                bprim[j]=bprim[j]%10000;}
                                                                
                                                        }
                           }
 
      int maxim=0;
      for(i=0;i<19;i++) 
                          if(bprim[i]>maxim&&b[i]=='w') maxim=bprim[i];
                          
      maxim=maxim%10000;
       if (maxim<10) fprintf (g,"Case #%d: 000%d\n",p, maxim);
       else if (maxim<100) fprintf (g,"Case #%d: 00%d\n",p, maxim);
       else if (maxim<1000) fprintf (g,"Case #%d: 0%d\n",p, maxim);
       else fprintf (g,"Case #%d: %d\n",p, maxim);
       
         
     
       
       }  
  return 0;
 }
