#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
      int t,n,i,j,k;
      int cur,bPos,oPos;
      int bl[200];
      int orange[200];
      char seq[200];
      FILE *fin,*fout;
      fin=fopen("A-large.txt","r");
      fout=fopen("A-large-Out.txt","w");
      fscanf(fin,"%d",&t);
      
      for(int c=1;c<=t;c++){
            fscanf(fin,"%d",&n);
            int oc=0,bc=0;
            for(i=0;i<n;i++){
                  fscanf(fin,"%c",&seq[i]);
                  fscanf(fin,"%c",&seq[i]);
                  if(seq[i]=='O') fscanf(fin,"%d",&orange[oc++]);
                  else fscanf(fin,"%d",&bl[bc++]);      
            } 
            cur=0;oPos=bPos=1;
            j=0;k=0;
            int ans=0;
            int curMove=0;
            
            while(cur<n){
                  if(seq[cur]=='O'){
                        if(oPos>orange[j]) curMove=oPos-orange[j];
                        else curMove =orange[j]-oPos;
                        
                        oPos=orange[j]; j++;
                        curMove+=1;
                        
                        if(k<bc){
                              if(bPos>bl[k]){
                                    if(bPos-bl[k]<=curMove) bPos=bl[k];
                                    else bPos-=curMove;     
                              }
                              else{
                                    if(bl[k]-bPos<=curMove) bPos=bl[k];
                                    else bPos+=curMove;     
                              }     
                        }     
                  }    
                  else{
                        if(bPos>bl[k]) curMove=bPos-bl[k];
                        else curMove =bl[k]-bPos;
                        
                        bPos=bl[k]; k++;
                        curMove+=1;
                        
                        if(j<oc){
                              if(oPos>orange[j]){
                                    if(oPos-orange[j]<=curMove) oPos=orange[j];
                                    else oPos-=curMove;     
                              }
                              else{
                                    if(orange[j]-oPos<=curMove) oPos=orange[j];
                                    else oPos+=curMove;     
                              }     
                        }  
                  } 
                  ans+=curMove;
                  curMove=0;
                  cur++;
            } 
            fprintf(fout,"Case #%d: %d\n",c,ans);   
      }
      return 0;
}
