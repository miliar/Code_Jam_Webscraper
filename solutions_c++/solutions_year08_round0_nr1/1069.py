#include <iostream>
#include <string>
#include <fstream>
#include <map>

#define foreach(it,c) for(typeof((c).begin()) it=(c).begin(); it != (c).end() ; it++ )
#define F(i,mi,ma) for(int i=mi;i<ma;i++)

#define vi vector< int >
#define vs vector< string >
#define bn begin()
#define en end()
#define sz size()
#define pb push_back

using namespace std;

int main()
{
    int N,S,Q;
    
    ifstream in("al.in");
    ofstream out("al.out");
    
    in>> N;
    F( i,0,N){

       in >> S;
       
       int k=0,ans=0;
       map<string,int> se;
       string t;
       getline(in,t);
       F( j,0,S){
          getline(in,t);
          se[t] = k++ ;
       }
       
       string fset,eset,rset;
       F( j,0,S){
          fset+="1";
          eset+="0";
       }
       rset=eset;
       in>>Q;
       getline(in,t);
       F( j,0,Q){
          getline(in,t);
          rset[ se[t] ]='1';
          if( rset == fset ){
              ans++;
              rset = eset;
              rset[ se[t] ] = '1' ;
          }
       }
       
       out << "Case #" << i+1 <<": " << ans <<endl;
   }
   out.close();
   in.close();
}

                
             
