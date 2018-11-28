#include <iostream>
#include <cstdio>
#include <list>
#include <vector>
#include <cstdlib>

using namespace std;
int t,na,nb;

typedef struct foo{
        int st;
        int end;
        bool ep;        
        bool ab;
        }foo;
        
int compare (const void * a, const void * b)
{
    return ( ((foo *)a)->end - ((foo *)b)->end );
}
foo *table;

void read_input(){
     string a,b;     
     int con;
     for(int i=0; i<na+nb; i++){
             cin >> a >> b;
             con = ((a[0]-'0')*10) + (a[1]-'0');        
             con *= 60;
             con += ((a[3]-'0')*10) + (a[4]-'0');
             table[i].ep = false;             
             table[i].st = con;
             con = ((b[0]-'0')*10) + (b[1]-'0');   
             con *= 60;     
             con += ((b[3]-'0')*10) + (b[4]-'0');             
             table[i].end = con;             
             if(i < na){
                  table[i].ab = true;
             }else{
                   table[i].ab = false;
             }
             //cout << tablea[i].st << " || " << tablea[i].end <<endl;    
     }   
}
void print_input(){
     for(int i=0; i<na+nb; i++){
             cout << table[i].st << " || " << table[i].end << " -> "<< table[i].ab <<" ep: " << table[i].ep << endl;    
     }     
}
void searchb(int u,int end);
void searcha(int u,int end){
     int min,mini,k=0;
     for(int i=0; i<na+nb; i++){
         if(table[i].ab && !table[i].ep && table[i].st-t >= end){
                      if(k==0){
                               mini = i;
                               min =  table[i].st-end;  
                               k++;
                         }else{
                               if((table[i].st-end) < min){
                                      mini = i;
                                      min = table[i].st-end;                          
                               }
                         }       
         }
     }
     if(k==1){
    table[mini].ep = true;
    searchb(mini,table[mini].end);
    }
    return;
}
void searchb(int u,int end){
     int min,mini,k=0;
     for(int i=0; i<na+nb; i++){
         if(!table[i].ab && !table[i].ep && table[i].st-t >= end){                         
                         if(k==0){
                               mini = i;
                               min =  table[i].st-end;  
                               k++;
                         }else{
                               if((table[i].st-end) < min){
                                      mini = i;
                                      min = table[i].st-end;                          
                               }
                         }                
         }            
     }     
     if(k==1){
     table[mini].ep = true;
     searcha(mini,table[mini].end);
    }
    return;
}
void process(int k){
     int tna=0,tnb=0;
     for(int i=0; i<na+nb; i++){
             if(!table[i].ep){
                  if(table[i].ab){
                                  searchb(i,table[i].end);                
                  }else{
                                  searcha(i,table[i].end);                        
                  }            
             }        
     }
     for(int i=0; i<na+nb; i++){
             if(!table[i].ep){
                              if(table[i].ab){
                                              tna++;                
                              }else{
                                              tnb++;
                              }                 
             }        
     }
     cout << "Case #" << k << ": "<< tna << " " << tnb <<endl;
}
int main(){
    int k;
    cin >> k;  
    table = (foo *)malloc(200*sizeof(foo));
    for(int i=0; i<k; i++){
            cin >> t;        
            cin >> na >> nb;            
            read_input();
            qsort(table, na+nb, sizeof(foo), compare);                                  
            process(i+1);
            //print_input();
            //cout << "========"<<endl;
    }
    return 0;    
}
