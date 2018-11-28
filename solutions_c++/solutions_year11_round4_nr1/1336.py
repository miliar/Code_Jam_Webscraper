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

struct Path{
       
       bool operator<( const Path rhs)const{
            return (B<rhs.B);
            
            
            }
       
       
       int B, E, w;

       };


bool compare(const Path a, const Path b){   
     
     return a.w<b.w;
     
     }



int main(){
    int i, j, k, t, tt;
    char fileName[100];
    
    cout.precision(15);
    
    
    cout<<"enter file name: ";
    cin>>fileName;
    
    if(!testF(fileName)){
       cout<<"NO FILE"<<endl; system("pause"); return 0;                 
       }       
    
   	freopen( fileName, "r", stdin );  //open for read
    
	freopen( "outputL.txt", "w", stdout ); //open for write
    
    tt=ni();

    ft(tt){

               int X=ni(); //length
               int S=ni(); //walk speed
               int R=ni(); //run speed
               int T=ni(); //run time
               int N=ni(); //num walkways
               
               vector<Path> ways;
               ways.clear();
               
               double time=0;
               
               //time=double(X)/double(S);
               double dist;
               double rTime=0;
               double addT, addTR;
               
               fi(N){
                     Path p;
                     p.B=ni();
                     p.E=ni();
                     p.w=ni();
                     

                     ways.pb(p);
                     }
               
               sort(all(ways));
        
               fi(ways.size()){
                               if(i==0){
                                        dist=ways[i].B;
                                        addT=dist/double(S);
                                        addTR=dist/double(R);

                                        }
                               
                               else{
                                    dist=ways[i].B-ways[i-1].E;
                                    addT=double(dist)/double(S);
                                    addTR=double(dist)/double(R);

                                    }
                               
                               if(rTime>=T){
                                            time+=addT;
                                            }
                               else if(rTime+addTR<=T){
                                    time+=addTR;
                                    rTime+=addTR;
                                    }
                               else if(rTime+addTR>T){
                                    double d=double(R)*double(T-rTime);
                                    dist-=d;
                                    time+=T-rTime;
                                    time+=dist/double(S);
                                    rTime=T;
                                    }
                               
                               }
                               
               //after last walkway
                               
                                    dist=X-ways[ways.size()-1].E;
                                    addT=double(dist)/double(S);
                                    addTR=double(dist)/double(R);
                               
                               if(rTime>=T){
                                            time+=addT;
                                            }
                               else if(rTime+addTR<=T){
                                    time+=addTR;
                                    rTime+=addTR;
                                    }
                               else if(rTime+addTR>T){
                                    double d=double(R)*double(T-rTime);
                                    dist-=d;
                                    time+=T-rTime;
                                    time+=dist/double(S);
                                    rTime=T;
                                    }         
                               
                               
               
               sort(all(ways),compare);
               
               fi(ways.size()){
                               
                               dist=ways[i].E-ways[i].B;
                               addT=double(dist)/double(S+ways[i].w);
                               addTR=double(dist)/double(R+ways[i].w);
                               
                               if(rTime>=T){
                                            time+=addT;
                                            }
                               else if(rTime+addTR<=T){
                                    time+=addTR;
                                    rTime+=addTR;
                                    }
                               else if(rTime+addTR>T){
                                    double d=double(R+ways[i].w)*double(T-rTime);
                                    dist-=d;
                                    time+=T-rTime;
                                    time+=dist/double(S+ways[i].w);
                                    rTime=T;
                                    }
                               
                               }

               
               
               printf( "Case #%d: ", t+1 );
               cout<<time<<endl;
          
          }
    
    
    
    
    
    
    
 return 0;   
}
