#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
      int t,n;
      int smallest,price,total;
      int i,j;
      int ones[30];
      FILE *fin,*fout;
      fin=fopen("C-large.in","r");
      fout=fopen("C-large-out.txt","w");
      
      fscanf(fin,"%d",&t);
      
      int jMax=0;
      for(int c=1;c<=t;c++){
            fscanf(fin,"%d",&n);
            for(i=0;i<30;i++) ones[i]=0;
            smallest=100000000;
            total=0;
            for(i=0;i<n;i++){
                  fscanf(fin,"%d",&price);
                  if(price<smallest) smallest=price;
                  total+=price;
                  
                  j=0;
                  while(price>0){
                        if(price%2==1) ones[j]++;
                        price/=2;
                        j++;     
                  }
                  if(j>jMax) jMax=j;
            }        
            bool poss=true;   
            for(i=0;i<jMax;i++){
                  if(ones[i]%2==1){
                        poss=false;
                        break;     
                  }     
            }
            if(poss)
                  fprintf(fout,"Case #%d: %d\n",c,total-smallest);     
            
            else
                  fprintf(fout,"Case #%d: NO\n",c);     
                    
      }     
      
      return 0;
}
