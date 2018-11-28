#include <iostream>
#include <fstream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

const int MAX_T = 100;
const int MAX_H = 100;
const int MAX_W = 100;
int array[MAX_H][MAX_W];

struct point{
       public :
       int x; int y;
       int color;
       point( int _x, int _y,int a){
              x = _x;
              y = _y;
              color = a;
              };
       
       void setColor( int a ){
            color = a;
            }
       };

bool isSink( int j , int k , int h , int w ){
     if ( j != 0 && array[j][k] > array[j-1][k] ) return false; 
     if ( j != h - 1 && array[j][k] > array[j+1][k] ) return false; 
     if ( k != 0 && array[j][k] > array[j][k-1] ) return false; 
     if ( k != w - 1 && array[j][k] > array[j][k+1] ) return false; 
     return true;
     }

bool isFlowTo( int i1, int j1, int i2, int j2, int h, int w ){
     if ( i1!= 0 && array[i1-1][j1]< array[i2][j2] ) return false;
     if ( i1!= h - 1 && array[i1+1][j1]< array[i2][j2] ) return false;
     if ( j1!= 0 && array[i1][j1-1]< array[i2][j2] ) return false;
     if ( j1!= w - 1 && array[i1][j1+1]< array[i2][j2] ) return false;
     if ( i1 == i2 + 1 ) return true;
     if ( i1 == i2 - 1 ){
          if ( j1!= 0 && array[i1][j1-1] == array[i2][j2] ) return false;
          if ( j1!= w - 1 && array[i1][j1+1] == array[i2][j2] ) return false;
          if ( i1!= 0 && array[i1-1][j1] == array[i2][j2] ) return false;
          }
     if ( j1 == j2 + 1 ){
          if ( i1!= 0 && array[i1-1][j1] == array[i2][j2] ) return false;
        }
     if ( j1 == j2 - 1 ){
          if ( i1!= 0 && array[i1-1][j1] == array[i2][j2] ) return false;
          if ( j1!= 0 && array[i1][j1-1] == array[i2][j2] ) return false;
        }
          
     return true;
     }  
     
int main(){
    ifstream fin("B-large.in",ios::in);
    ofstream fout("B_large.out", ios::out);
    int t;
    fin>>t;
    //cout<<t<<endl;
    
    for ( int i = 0 ; i < t ; i ++ ){
        int h = 0 , w = 0;
        fin>> h >>w;
        for ( int j = 0 ; j < h ; j++ )
            for ( int k = 0 ; k < w ; k++ ) fin >> array[j][k];
            
        int tempoArray[MAX_H][MAX_W];
        
        for ( int j = 0 ; j < h ; j++ )
            for ( int k = 0 ; k < w ; k++ ) {
                tempoArray[j][k] = 0;
            }
        
        int count = 0;
        vector<point> v;
        for ( int j = 0 ; j < h ; j++ )
            for ( int k = 0 ; k < w ; k++ ){
                if ( isSink(j,k,h,w) ) {
                     //cout<<j<<" "<<k<<endl;
                     count++;
                     tempoArray[j][k] = count;
                     v.push_back(point(j,k,count));
                }
            }
        //system("pause");
        vector<point> tempV;
        while ( v.size() != 0 ){
              tempV = v;
              v.clear();
              
              for ( int i = 0 ; i < tempV.size() ; i++ ){
                  point q = tempV[i];
                  int x = q.x;
                  int y = q.y;
                  int c = q.color;
                  if ( x!= 0 && isFlowTo( x - 1 , y , x, y , h , w ) && tempoArray[x-1][y] == 0 ) {
                       v.push_back( point(x-1,y,c) );
                       tempoArray[x-1][y] = c;
                       }
                  if ( x!= h - 1 && isFlowTo( x + 1 , y , x, y , h , w )&& tempoArray[x+1][y] == 0  ) {
                       v.push_back( point(x+1,y,c) );
                       tempoArray[x+1][y] = c;
                       }
                  if ( y!= 0 && isFlowTo( x , y - 1 , x, y , h , w ) && tempoArray[x][y-1] == 0 ) {
                       v.push_back( point(x,y-1,c) );
                       tempoArray[x][y-1] = c;
                       }
                  if ( y!= w - 1 && isFlowTo( x , y + 1 , x, y , h , w ) && tempoArray[x][y+1] == 0) {
                       v.push_back( point(x,y+1,c) );
                       tempoArray[x][y+1] = c;
                       }
              }
        }
        //cout<<count<<endl;
        /*for ( int i = 0 ; i < h ; i ++){
            cout<<endl;
            for ( int j = 0 ; j < w ; j ++ )   cout<<tempoArray[i][j]<<" ";
            }*/
        char map[30];
        for ( int i = 0 ; i < 30 ; i ++ ) map[i] = 'M';
        
        
        char c = 'a';
        for ( int i = 0 ; i < h ; i ++)
            for ( int j = 0 ; j < w ; j ++ )  {
                if ( map[tempoArray[i][j]] == 'M'){
                     map[tempoArray[i][j]] = c;
                     c++;
                   }
            }
        char result[MAX_H][MAX_W];
        for ( int i = 0 ; i < h ; i ++)
            for ( int j = 0 ; j < w ; j ++ ) result[i][j] = map[tempoArray[i][j]];
        
        for ( int i = 0 ; i < h ; i ++){
            cout<<endl;
            for ( int j = 0 ; j < w ; j ++ )   cout<<result[i][j]<<" ";
            }  
        fout<<"Case #"<<i+1<<": "<<endl;
        for ( int j = 0 ; j < h ; j ++){
            for ( int k = 0 ; k < w ; k ++ )   fout<<result[j][k]<<" ";
            fout<<endl;
            }    
       // system("pause");*/
    }
    system("pause");
}
