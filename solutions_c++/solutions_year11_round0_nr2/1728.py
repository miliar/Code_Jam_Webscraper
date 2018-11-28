#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
      int t,c,d,n,i,j,k;
      int com[26][26];
      bool clear[26][26];
      char ch,ch1,ch2,ch3;
      FILE *fin,*fout;
      
      fin=fopen("B-large.txt","r");
      fout=fopen("B-large-out.txt","w");
      
      fscanf(fin,"%d",&t);
      for(int num=1;num<=t;num++){
            
            for(i=0;i<26;i++) for(j=0;j<26;j++) com[i][j]=-1;
            for(i=0;i<26;i++) for(j=0;j<26;j++) clear[i][j]=false;
            
            fscanf(fin,"%d",&c);
            for(i=0;i<c;i++){
                  fscanf(fin,"%c%c%c%c",&ch,&ch1,&ch2,&ch3);
                  com[ch1-65][ch2-65]=ch3-65;
                  com[ch2-65][ch1-65]=ch3-65;     
            }
            
            fscanf(fin,"%d",&d);
            for(i=0;i<d;i++){
                  fscanf(fin,"%c%c%c",&ch,&ch1,&ch2);
                  clear[ch1-65][ch2-65]=true; 
                  clear[ch2-65][ch1-65]=true;    
            }   
            fscanf(fin,"%d",&n);
            fscanf(fin,"%c",&ch);
            
            int ans[200];
            int len=0;
            
            for(i=0;i<n;i++){
                  fscanf(fin,"%c",&ch);
                  if(len==0) ans[len++]=ch-65;
                  
                  else if(com[ans[len-1]][ch-65]!=-1)
                        ans[len-1]=com[ans[len-1]][ch-65];      
                  
                  else ans[len++]=ch-65;
                  for(j=0;j<len-1;j++){
                        if(clear[ans[j]][ans[len-1]]==true){
                              len=0;
                              break;     
                        }     
                  }
            }   
            fprintf(fout,"Case #%d: [",num);
            for(i=0;i<len;i++){
                  ch=ans[i]+65;
                  if(i!=len-1) fprintf(fout,"%c, ",ch);
                  else     fprintf(fout,"%c",ch); 
            }
            fprintf(fout,"]\n");
      }
      
      return 0;     
}
