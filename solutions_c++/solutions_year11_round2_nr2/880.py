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


int P[201]; //point
int V[201]; //num

double solve(int a, int b);

int C,D;


int main(){
    int i, j, k, t, tt;
    char fileName[100];
    
    
    cout<<"enter file name: ";
    cin>>fileName;
    
    if(!testF(fileName)){
       cout<<"NO FILE"<<endl; system("pause"); return 0;                 
       }       
    
   	freopen( fileName, "r", stdin );  //open for read
    
	freopen( "output.txt", "w", stdout ); //open for write
    
    tt=ni();

    ft(tt){
    
               C=ni();
               D=ni();
               
               int tot=0;
               
               fi(C){
                     P[i]=ni();
                     V[i]=ni();
                     
                     tot+=V[i];
                     
                     }
               
               double time=0;
               
               if(D==0 || C==0 || tot <= 1){
                        printf( "Case #%d: %lf\n", t+1, 0.0 );
                        continue;
                        }
               
               fi(C){
                     for(j=i;j<C;j++){
                                       time=max(double(time),solve(i,j));        
                                      }
                     
                     
                     }
               
               
               printf( "Case #%d: %lf\n", t+1, time );
          
          }
    
    

    
    
    
    
 return 0;   
}


double solve(int a, int b){  //range of array, number left in array
    double time=0;
    double dist=0;
    
    int sum=0;
    for(int i=a; i<=b; i++)
    {
     sum+=V[i];       
     }
    
    if(sum <= 1)
       return 0;
    
    sum-=2;
    
    dist=sum*D+D;
    
    dist-= (P[b]-P[a]);
    
    time=dist/2;
    
    return time;
    

    }



