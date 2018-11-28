#include <stdio.h>
#include <list>
using namespace std;

int t,h,w;
int field[105][105];
char ans[105][105];
enum di {
    North,
    West,
    East,
    South
};    
void clearAns(){
    int i,j;
    for(i=0;i<105;i++)
        for(j=0;j<105;j++)
           ans[i][j]=0;
}      
void printAns(){
    int i,j;
    for(i=0;i<h;i++){
        for(j=0;j<w;j++)
            printf("%c ", ans[i][j]);
        printf("\n");
    }      
}     
int main(){
    int i,j,k,ii,jj;
    char letter='a';
    list <int> qc; //Column
    list <int> qr; //Row
  
    scanf("%d", &t);    
    for(k=0;k<t;k++){
        scanf("%d %d", &h, &w);
        
        clearAns();
        letter='a';
        
        //Get the field
        for(i=0;i<h;i++){
            for(j=0;j<w;j++)
                scanf("%d", &field[i][j]);
        }    
        //Start from top left
        i=0; j=0;
        while(i<h&&j<w){
            qc.push_back(j);
            qr.push_back(i);
            while(!qr.empty()){
                i=qr.front();
                j=qc.front();
                qr.pop_front();
                qc.pop_front();
                ans[i][j]=letter;
                
                //printf("pop %d %d\n",i,j);
                //printAns();
                
                //North
                if(i-1>=0 && field[i-1][j]!=field[i][j] && ans[i-1][j]==0){
                    ii=i-1; jj=j;
                    
                    //(i,j) is sink
                    if(field[i][j]<field[ii][jj]                   && //(i,j) is South
                       (!(jj-1>=0) || field[i][j]<field[ii][jj-1]) && //South < West
                       (!(jj+1<w)  || field[i][j]<field[ii][jj+1]) && //South < East
                       (!(ii-1>=0) || field[i][j]<field[ii-1][jj]))   //South < North
                    {
                        qr.push_back(ii);
                        qc.push_back(jj);
                        //printf("North, sink\n");
                    }    
                    
                    //(i,j) is source
                    if(field[ii][jj]<field[i][j]                   && //(ii,jj) < (i,j), is North
                       (!(j-1>=0) || field[ii][jj]<=field[i][j-1]) && //North <= West
                       (!(j+1<w)  || field[ii][jj]<=field[i][j+1]) && //North <= East
                       (!(i+1<h)  || field[ii][jj]<=field[i+1][j]))   //North <= South
                    {
                        qr.push_back(ii);
                        qc.push_back(jj);
                        //printf("North, src\n");
                    }  
                }    
                //West
                if(j-1>=0 && field[i][j-1]!=field[i][j] && ans[i][j-1]==0){
                    ii=i; jj=j-1;
                    
                    //(i,j) is sink
                    if(field[i][j]<field[ii][jj]                   && //(i,j) is  East
                       (!(jj-1>=0) || field[i][j]<field[ii][jj-1]) && //East < West
                       (!(ii-1>=0) || field[i][j]<field[ii-1][jj]) && //East < North
                       (!(ii+1<h)  || field[i][j]<=field[ii+1][jj]))  //East <= South
                    {
                        qr.push_back(ii);
                        qc.push_back(jj);
                        //printf("West, sink\n");
                    }  
                    
                    //(i,j) is source
                    if(field[ii][jj]<field[i][j]                  && //(ii,jj) < (i,j), is West
                       (!(j+1<w)  || field[ii][jj]<=field[i][j+1]) && //West <= East
                       (!(i+1<h)  || field[ii][jj]<=field[i+1][j]) && //West <= South
                       (!(i-1>=0) || field[ii][jj]<field[i-1][j]))   //West < North
                    {
                        qr.push_back(ii);
                        qc.push_back(jj);
                        //printf("West, src\n");
                    }                 
                }    
                //East
                if(j+1<w && field[i][j+1]!=field[i][j] && ans[i][j+1]==0){
                    ii=i; jj=j+1;
                    
                    //(i,j) is sink
                    if(field[i][j]<field[ii][jj]                    && //(i,j) is  West
                       (!(ii+1<h)  || field[i][j]<=field[ii+1][jj]) && //West <= South
                       (!(ii-1>=0) || field[i][j]<field[ii-1][jj])  && //West < North
                       (!(jj+1<w)  || field[i][j]<=field[ii][jj+1]))   //West <= East
                    {
                        qr.push_back(ii);
                        qc.push_back(jj);
                        //printf("East, sink\n");
                    }  
                    
                    //(i,j) is source
                    if(field[ii][jj]<field[i][j]                   && //(ii,jj) < (i,j), is East
                       (!(j-1>=0)  || field[ii][jj]<field[i][j-1])  && //East < West
                       (!(i+1<h)  || field[ii][jj]<=field[i+1][j]) && //East <= South
                       (!(i-1>=0) || field[ii][jj]<field[i-1][j]))    //East < North
                    {
                        qr.push_back(ii);
                        qc.push_back(jj);
                        //printf("East, src\n");
                    }                 
                }
                //South
                if(i+1<h && field[i+1][j]!=field[i][j] && ans[i+1][j]==0){
                    ii=i+1; jj=j;
                    
                    //(i,j) is sink
                    if(field[i][j]<field[ii][jj]&&                     //(i,j) is North
                       (!(jj-1>=0) || field[i][j]<=field[ii][jj-1]) && //North <= West
                       (!(jj+1<w)  || field[i][j]<=field[ii][jj+1]) && //North <= East
                       (!(ii+1<h)  || field[i][j]<=field[ii+1][jj]))   //North <= South
                    {
                        qr.push_back(ii);
                        qc.push_back(jj);
                        //printf("South, sink\n");
                    }  
                    
                    //(i,j) is source
                    if(field[ii][jj]<field[i][j] &&                  //(ii,jj) < (i,j), is South
                       (!(j-1>=0)|| field[ii][jj]<field[i][j-1]) &&  //South < West
                       (!(j+1<w) || field[ii][jj]<field[i][j+1]) &&  //South < East
                       (!(i-1>=0) || field[ii][jj]<field[i-1][j]))    //South < North
                    {
                        qr.push_back(ii);
                        qc.push_back(jj);
                        //printf("South, src\n");
                    }  
                }
            }   
            letter++;
            for(i=0;i<h;i++){
                for(j=0;j<w&&ans[i][j]!=0;j++);
                if(j<w&&ans[i][j]==0)
                    break;
            }       
        }    
        printf("Case #%d:\n", k+1);
        printAns();
    }    
    
    //scanf("%d", &i);
    return 0;
}    
