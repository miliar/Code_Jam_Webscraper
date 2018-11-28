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



int main(){
    int i, j, k, t, tt;
    char fileName[100];
    

    cout<<"enter file name: ";
    cin>>fileName;
    
    if(!testF(fileName)){
       cout<<"NO FILE"<<endl; system("pause"); return 0;                 
       }       
    
   	freopen( fileName, "r", stdin );  //open for read

	freopen( "outputSmall.txt", "w", stdout ); //open for write
    
    tt=ni();

    ft(tt){

               int N=ni();
               int L=ni();
               int H=ni();
               vector<int> notes;
               notes.clear();
               
               fi(N){
                     notes.pb(ni());
                     }
               
               bool work;
               int ans=0;
               
               //brute force
               for(i=L;i<=H;i++){
                                 work=true;
                                 fj(N){
                                       if( i % notes[j] != 0 && notes[j] % i != 0 ){
                                           work=false;
                                           break;
                                           }
    
                                       }
                                 if(work){
                                          ans=i;
                                          break;
                                          }
                                 
                                 
                                 }

               printf( "Case #%d: ", t+1 );
               
               if(work){
                        cout<<ans<<endl;
                        }
               else
                   cout<<"NO"<<endl;
               

          
          }
    
    
    
    
    
    
    
 return 0;   
}
