#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>

#define fo(a,b,c) for( a = ( b ); a < ( c ); a++ )
#define fr(a,b) fo( a, 0, ( b ) )
#define fk(a) fr( k, ( a ) )
#define ft(a) fr( t, ( a ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )


using namespace std;

int ni() { int a; scanf( "%d", &a ); return a; } //get int
int nc() { char a; cin>>a; return a; } //get char
double nf() { double a; scanf( "%lf", &a ); return a; }  //get double
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }  //get string
long long nll() { long long a; scanf( "%lld", &a ); return a; } //get long long

bool testF(char str[]){ifstream inf; bool a; inf.open(str); a=inf.good(); inf.close(); return a; }

template <class T>
T** make2d(int n, int m) { T** a; int i,j; a=new T* [n]; fi(n){a[i]=new T [m]; fj(m){a[i][j]=0;} } return a; } 

char a[53][53];


int main(){
    int i, j, k, t, tt;
    char fileName[100];
    
    
    cout<<"enter file name: ";
    cin>>fileName;
    
    if(!testF(fileName)){
       cout<<"NO FILE"<<endl; system("pause"); return 0;                 
       }       
    
   	freopen( fileName, "r", stdin );  //open for read
    
	freopen( "outputLarge.txt", "w", stdout ); //open for write
    
    tt=ni();

    ft(tt){

               int R=ni();
               int C=ni();
               
               _(a,0);
               bool possible=true;
               
               fi(R){
                     fj(C){
                           a[i][j]=nc();
                           }
                     }
               
               
               fi(R){
                     fj(C){
                           if(a[i][j]=='#'){
                                            if(a[i+1][j]!='#' || a[i][j+1]!='#' || a[i+1][j+1]!='#' ){
                                                  possible=false;
                                                  break;
                                                  }
                                            else{
                                                 a[i][j]='/';
                                                 a[i][j+1]=92;
                                                 a[i+1][j]=92;
                                                 a[i+1][j+1]='/';
                                                 }
  
                                            }
 
                           }
 
                      if(!possible)
                         break;
 
                     }
               
               printf( "Case #%d: \n", t+1 );
               if(!possible){
                             cout<<"Impossible"<<endl;
                             continue;
                             }
               fi(R){
                     fj(C){
                           cout<<a[i][j];
                
                          }
                      cout<<endl;
                     }
               
          
          }
    
    
    
    
    
    
    
 return 0;   
}
