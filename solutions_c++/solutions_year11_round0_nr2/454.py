#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void com_check(int com[][30], int elist[], int nxt){
     int i,j,k;
     int temp;
            
     temp = elist[elist[0]];

     if (com[temp][nxt]>0) elist[elist[0]]=com[temp][nxt];

     else if (com[temp][nxt]==0){
          elist[0]++;
          elist[elist[0]]=nxt;
     }
    
}

void opp_check(int opp[][30],int elist[]){
     int i,j,k;
     int n,temp;
     n = elist[0];
     temp = elist[n];
     /*
     for (i=n-1;i>=1;--i){
         if  (opp[elist[i]][temp]==1){
             elist[0]=i-1;
             for(j=i;j<=n;++j){
                               elist[j]=0;
             }
             break;
         }
     }
     */
     for (i=n-1;i>=1;--i){
         if  (opp[elist[i]][temp]==1){
             for (j=0;j<=n;++j) elist[j]=0;
             break;
         }
     }
         
     
        
}
                                     


void update_elist(int com[][30], int opp[][30], int elist[], int nxt){
     int i,j,k;
     
     if (elist[0]==0){
                      elist[0]=1;
                      elist[1]=nxt;
     }
     
     else if (elist[0]>0){
               
                     com_check(com,elist,nxt);
                     opp_check(opp,elist);
     }
}
                     


int main(){
    int i,j,k,temp[300]={0};
    int com[30][30]={0}, opp[30][30]={0},elist[300]={0},ivk[300]={0};
    int t,c,d,n;
    char tempch[300]={0};
    FILE* fin=fopen("B-large.in","r");
    FILE* fout=fopen("B-large.out","w");
    
    
    fscanf(fin,"%d",&t);
    for (i=1;i<=t;++i){
        for (j=0;j<=29;++j){
            for (k=0;k<=29;++k){
                com[j][k]=0;
                opp[j][k]=0;
            }
        }
        for (j=0;j<=299;++j){
            elist[j]=0;
            ivk[j]=0;
        }
        
        fscanf(fin,"%d",&c);
        for (j=1;j<=c;++j){
            fscanf(fin,"%s",tempch);
            temp[0]=tempch[0]-'A'+1;
            temp[1]=tempch[1]-'A'+1;
            temp[2]=tempch[2]-'A'+1;
            com[temp[0]][temp[1]]=temp[2];
            com[temp[1]][temp[0]]=temp[2];
        }
        fscanf(fin,"%d",&d);
        for (j=1;j<=d;++j){
            fscanf(fin,"%s",tempch);
            temp[0]=tempch[0]-'A'+1;
            temp[1]=tempch[1]-'A'+1;
            opp[temp[0]][temp[1]]=1;
            opp[temp[1]][temp[0]]=1;
        }
        fscanf(fin,"%d",&n);
        ivk[0]=n;
        fscanf(fin,"%s",tempch);
        for (j=1;j<=n;++j) ivk[j]=tempch[j-1]-'A'+1;
        
        for (j=0;j<=200;++j) elist[j]=0;
     
        for (j=1;j<=n;++j){
                
            update_elist(com, opp, elist, ivk[j]);
        }
    
        fprintf(fout,"Case #%d: [",i);
        for (j=1;j<=elist[0]-1;++j) fprintf(fout,"%c, ",elist[j]+'A'-1);
        if (elist[0]>0) fprintf(fout,"%c",elist[elist[0]]+'A'-1);
        fprintf(fout,"]\n");
        
    }
    
    return 0;
}
