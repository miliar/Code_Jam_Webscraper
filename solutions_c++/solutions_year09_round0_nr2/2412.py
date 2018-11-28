#include <iostream>
#include <vector>

using namespace std;

typedef struct{
   int i, j;
}pos;

int h,w,basin;

pos escorre(int i, int j, vector< vector <int> > & mapa){
     int idest,jdest;
     int menor=100000;
     if(i+1<h){
        if(mapa[i+1][j]<=menor){
           idest=i+1;
           jdest=j;
           menor=mapa[i+1][j];
        }
     }
     if(j+1<w){
        if(mapa[i][j+1]<=menor){
           idest=i;
           jdest=j+1;
           menor=mapa[i][j+1];
        }
     }
     if(j-1>-1){
        if(mapa[i][j-1]<=menor){
           idest=i;
           jdest=j-1;
           menor=mapa[i][j-1];
        }
     }
     if(i-1>-1){
        if(mapa[i-1][j]<=menor){
           idest=i-1;
           jdest=j;
           menor=mapa[i-1][j];
        }
     } 
     pos posicao;
     if(menor<mapa[i][j]){
        posicao.i=idest;
        posicao.j=jdest;
     }else{
        posicao.i=-1;
        posicao.j=-1;
     }
     return posicao;   
}

void backtrack(int i, int j, vector< vector <int> > & mapa, vector< vector <char> > & resultado){
     resultado[i][j]=('a'+basin);
     pos posicao=escorre(i,j,mapa);
     if(posicao.i!=-1 && resultado[posicao.i][posicao.j]=='!')
        backtrack(posicao.i,posicao.j,mapa,resultado);
     if((i+1<h) && (resultado[i+1][j]=='!')){
        posicao=escorre(i+1,j,mapa);
        if(posicao.i==i && posicao.j==j)
           backtrack(i+1,j,mapa,resultado);
     }
     if((j+1<w) && (resultado[i][j+1]=='!')){
        posicao=escorre(i,j+1,mapa);
        if(posicao.i==i && posicao.j==j)
           backtrack(i,j+1,mapa,resultado);
     }
     if((j-1>-1) && (resultado[i][j-1]=='!')){
        posicao=escorre(i,j-1,mapa);
        if(posicao.i==i && posicao.j==j)
           backtrack(i,j-1,mapa,resultado);
     }
     if((i-1>-1) && (resultado[i-1][j]=='!')){
        posicao=escorre(i-1,j,mapa);
        if(posicao.i==i && posicao.j==j)
           backtrack(i-1,j,mapa,resultado);
     }
}

int main(){
    int t;
    cin>>t;
    for(int cont=0; cont<t; cont++){       
       cin>>h>>w;
       vector< vector <int> > mapa(h,vector<int>(w));
       vector< vector <char> > resultado(h,vector<char>(w,'!'));
       for(int i=0; i<h; i++)
          for(int j=0; j<w; j++)
             cin>>mapa[i][j];
       basin=0;       
       for(int i=0; i<h; i++){
          for(int j=0; j<w; j++){
             if(resultado[i][j]=='!'){                                     
                backtrack(i,j,mapa,resultado);
                basin++;
             }
          }
       }
       /*cout<<i<<" -- "<<j<<" dest "<<idest<<" -- "<<jdest<<endl;
       for(int l=0; l<h; l++){
          for(int m=0; m<w; m++)
             cout<<resultado[l][m]<<" ";
          cout<<endl;
       }*/         
       cout<<"Case #"<<cont+1<<":"<<endl;
       for(int i=0; i<h; i++){
          for(int j=0; j<w; j++){
             if(j!=0)
                cout<<" ";
             cout<<resultado[i][j];
          }
          cout<<endl;
       }
    }
    return 0;
}
