#include<iostream>
#include<fstream>
using namespace std;
#define MAX 101
#define tren 1
#define trai 2
#define duoi 3
#define phai 4
ifstream fin("B-large.in");
ofstream fout("WATER.OUT");

char loang(char A[MAX][MAX],int C[MAX][MAX],int h,int w,int d,int c,char letter){
   int chieu=0;
   int Min=C[d][c];
   //tren
   if(d-1>=1&&Min>C[d-1][c]){
      Min=C[d-1][c];
      chieu=tren;
   }
   //trai
   if(c-1>=1&&Min>C[d][c-1]){
      Min=C[d][c-1];
      chieu=trai;
   }
   //phai
   if(c+1<=w&&Min>C[d][c+1]){
      Min=C[d][c+1];
      chieu=phai;
   }
   //duoi
   if(d+1<=h&&Min>C[d+1][c]){
      Min=C[d+1][c];
      chieu=duoi;
   }
   
   if(!chieu)
      A[d][c]=letter;
   else
       switch(chieu){
          case tren:
               if(A[d-1][c]!='*')
                   A[d][c]=A[d-1][c];
               else
                   A[d][c]=loang(A,C,h,w,d-1,c,letter);
               break;
          case trai:
               if(A[d][c-1]!='*')
                   A[d][c]=A[d][c-1];
               else
                   A[d][c]=loang(A,C,h,w,d,c-1,letter);
               break;
          case phai:
               if(A[d][c+1]!='*')
                   A[d][c]=A[d][c+1];
               else
                   A[d][c]=loang(A,C,h,w,d,c+1,letter);
               break;
          default:    //duoi
               if(A[d+1][c]!='*')
                   A[d][c]=A[d+1][c];
               else
                   A[d][c]=loang(A,C,h,w,d+1,c,letter);
       }
   return A[d][c];
}
void proccess(int t){
   int C[MAX][MAX];
   char A[MAX][MAX];
   int h,w;  
   
   int i,j;
   char c='a';
   fin>>h>>w;
   for(i=1;i<=h;i++)
       for(j=1;j<=w;j++)
           fin>>C[i][j];
   for(i=1;i<=h;i++)
       fill(A[i]+1,A[i]+w+1,'*');
   for(i=1;i<=h;i++)
       for(j=1;j<=w;j++)
           if(A[i][j]=='*')
               if(loang(A,C,h,w,i,j,c)==c)
                  ++c;
   fout<<"Case #"<<t<<":\n";
   for(i=1;i<=h;i++){
       for(j=1;j<=w;j++)
           fout<<A[i][j]<<" ";
       fout<<endl;
   }  
}
int main(){
   int T;
   fin>>T;
   for(int t=1;t<=T;t++)
       proccess(t);
   //system("pause");
   return 0;
}
