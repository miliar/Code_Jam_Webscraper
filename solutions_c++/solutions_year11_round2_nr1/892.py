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

char a[101][101];
double wp[101];
double owp[101];
double oowp[101];



int main(){
    int i, j, k, t, tt;
    char fileName[100];
    
    
    cout<<"enter file name: ";
    cin>>fileName;
    
    if(!testF(fileName)){
       cout<<"NO FILE"<<endl; system("pause"); return 0;                 
       }       
    
   	freopen( fileName, "r", stdin );  //open for read
    
	freopen( "outputL.txt", "w", stdout ); //open for write
    
    tt=ni();

    ft(tt){

               cout.precision(10);

               int N=ni();
               _(a,-100);
               _(wp,-100);
               _(owp,-100);
               _(oowp,-100);
               fi(N){
                     fj(N){
                           a[i][j]=nc();
                           }     
                     }
               
               
               //WP               
               fi(N){
                     double win=0;
                     double tot=0;
                     fj(N){
                           if(a[i][j]=='1'){
                                         win+=1;
                                         tot+=1;
                                         }
                           if(a[i][j]=='0'){
                                         tot+=1;
                                         }
                           
                           }
                     wp[i]=win/tot;
                     }
               
               //OWP
               fi(N){
                     double sum=0;
                     double num=0;
                     fj(N){
                           if(a[i][j]=='.'){
                                           continue;
                                         }
                           num++;
                           double win=0;
                           double tot=0;
                           fk(N){
                                 if(a[j][k]=='1' && k!=i ){
                                                win+=1;
                                                tot+=1;
                                                }
                                 if(a[j][k]=='0' && k!=i ){
                                                tot+=1;
                                                }
                                 }
                           sum+=win/tot;
                           }
                           
                     owp[i]=sum/num;
                     }
               
               
               //OOWP
               fi(N){
                     double sum=0;
                     double num=0;
                     
                     fj(N){
                           if(a[i][j]=='.')
                               continue;
                           sum+=owp[j];
                           num+=1;
                           }
                     
                     oowp[i]=sum/num;
                     
                     }
               
               printf( "Case #%d:\n", t+1 );
               fi(N){
                     cout<< 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]<<endl;

                     }

          }
    
    
    
    
    
    
    
 return 0;   
}
