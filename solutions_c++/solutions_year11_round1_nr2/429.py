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


string alph;
vector<string> words;


bool comp(string a, string b){

int i,j;


     fi(26){
                    int at=-1,bt=-1;
                    
                    
                    fj(a.length()){
                           if(alph[i]==a[j])
                              at=1;
                           if(alph[i]==b[j])
                              bt=1;
                           }
                           
                    if(at!=bt){
                               return (at==1);
                               }
                           
                     
                    
                    }


     fi(words.size()){
                      if(words[i]==a)
                         return false;
                      if(words[i]==b)
                         return true;
                      
                      }



 }




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

               printf( "Case #%d:", t+1);

               int N=ni();
               int M=ni();
               
               int Ncopy=N;
               
               words.clear();
               
               fi(N){
                     words.pb(ns());
                     }
               
               vector<string> wordsCopy;
               wordsCopy=words;
               
               
               int lengths[11];
               int longest=0;
               _(lengths,0);
               
               fj(N){
                     lengths[ words[j].length() ]++;                           
                     }
                     
               int length=0;
                     
               fj(11){
                      if(lengths[j]>length){
                                            longest=j;
                                            length=lengths[j];
                                           }
                      }
               
               
               fi(M){
                     string best="blank";
                     int guesses=-1;
                     alph=ns();

                     //for every word
                     fj(N){
                           int num=0;

                           words=wordsCopy;                           
                           string testWord=words[j];
                     
                     
                           fk(words.size()){
                                 if( words[k].length()!=testWord.length() ){
                                    words.erase(words.begin()+k);                           
                                    k--;
                                    }
                                 }
                                 

                     
                           int letter=-1;
                           while(words.size()>1){
                                                 letter++;
                                                 char c=alph[letter];
                                                 bool in=false;

                                                 fk(words.size()){
                                                       for(int l=0;l<testWord.length();l++){
                                                               

                                                               if(words[k][l]==c)        
                                                                  in=true;

                                                               if( (words[k][l]==c && testWord[l]!=c) || (words[k][l]!=c && testWord[l]==c) ){
                                                                  words.erase(words.begin()+k);
                                                                   k--;
                                                                   break;
                                                                   }
                                                                   


                                                               }
                           
                                                       }
                                                 
                                                 fk(testWord.length()){
                                                                     if(testWord[k]==c)
                                                                         in=false;
                                                                     
                                                                     }
                                                 
                                                 
                                                 if( in )
                                                   num++;

                                                 
                                                 }

                     
                              if(num>guesses){
                                              guesses=num;
                                              best=testWord;
                                              
                                              
                                              }
                                                 
                           
                           
                           
                           }
                     
                     
                     
                     
                                        
                     cout<<' '<<best;

                     }
               
               cout<<"\n";
               

          
          }
    
    
    
    
    
    
    
 return 0;   
}
