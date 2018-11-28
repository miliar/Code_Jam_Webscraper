#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
char mat[50][50];
int n, K;
void rotate();
int check();
void swap(char &a,char &b);
int main(char **argv,int argc)
{
   
   int lineNum;
   cin >> lineNum;
   for (int z=0;z<lineNum;++z)
   {
       cin >> n >> K;
       for (int i=0;i<n;++i)
       {  
          for (int j=0;j<n;++j)
          {
              cin >> mat[i][j];
          }
       }
       rotate();
       int ans=check();
       if (ans==0) cout <<     "Case #" << z+1 << ": " << "Neither" << endl;
       else if (ans==1) cout <<     "Case #" << z+1 << ": " << "Red" << endl;
       else if (ans==2) cout <<   "Case #" << z+1 << ": " << "Blue" << endl;
       else if (ans==3) cout <<   "Case #" << z+1 << ": " << "Both" << endl;

   }
//   system("pause");
   return 0;
}
void rotate()
{
     for (int i=0;i<n;++i)
     {
         int k=n-1;
         for (int j=n-1;j>=0;--j)
         {
             if (mat[i][j]=='.') 
             {
                  k=j;
                  for (int z=k-1;z>=0;--z)
                  {
                      
                     if (mat[i][z]!='.')
                     {
                        if (mat[i][k]=='.')
                           swap(mat[i][k],mat[i][z]);
                     }                   
                 }
             }
         }
     }
}
void swap(char &a,char &b)
{
     char c;
     c=a;
     a=b;
     b=c;
}
int check()
{
     bool red=false,blue=false;
     for (int i=0;i<n;++i)
     {
         for (int j=0;j<n;++j)
         {
             if (mat[i][j]=='R') {
             if (!red){
                 for (int k=0;k<K;++k)
                 {
                     if (j+k<n) {
                        if (mat[i][j]!=mat[i][j+k]) {red=false; break;}
                        else red=true;
                     }
                     else {red=false; break;}
                 }
             }
             if (!red){
                 for (int k=0;k<K;++k)
                 {
                     if (i+k<n) {
                        if (mat[i][j]!=mat[i+k][j]) {red=false; break;}
                        else red=true;
                     }
                     else {red=false; break;}
                 }
             }
             if (!red){
                 for (int k=0;k<K;++k)
                 {
                     if (j+k<n&&i+k<n) {
                        if (mat[i][j]!=mat[i+k][j+k]) {red=false; break;}
                        else red=true;
                     }
                     else {red=false; break;}
                 }
             }
             if (!red){
                 for (int k=0;k<K;++k)
                 {
                     if (i+k<n&&j-k>=0) {
                        if (mat[i][j]!=mat[i+k][j-k]) {red=false; break;}
                        else red=true;
                     }
                     else {red=false; break;}
                 }
             }
             }
             if (mat[i][j]=='B') {
             if (!blue){
                 for (int k=0;k<K;++k)
                 {
                     if (j+k<n) {
                        if (mat[i][j]!=mat[i][j+k]) {blue=false; break;}
                        else blue=true;
                     }
                     else {blue=false; break;}
                 }
             }
             if (!blue){
                 for (int k=0;k<K;++k)
                 {
                     if (i+k<n) {
                        if (mat[i][j]!=mat[i+k][j]) {blue=false; break;}
                        else blue=true;
                     }
                     else {blue=false; break;}
                 }
             }
             if (!blue){
                 for (int k=0;k<K;++k)
                 {
                     if (j+k<n&&i+k<n) {
                        if (mat[i][j]!=mat[i+k][j+k]) {blue=false; break;}
                        else blue=true;
                     }
                     else {blue=false; break;}
                 }
             }
             if (!blue){
                 for (int k=0;k<K;++k)
                 {
                     if (i+k<n&&j-k>=0) {
                        if (mat[i][j]!=mat[i+k][j-k]) {blue=false; break;}
                        else blue=true;
                     }
                     else {blue=false; break;}
                 }
             }
             }
             if (red==true&&blue==true) return 3;
         }
     }
     
     if (red==true&&blue==false) return 1;
     else if (red==false&&blue==true) return 2;
     return 0;
}
