// Sergio Botero - sergiobuj@gmail.com
// Status:
#include <vector>
#include <map>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>

using namespace std;
#define all(x) x.begin(),x.end()
#define D(x) cout <<__LINE__<<"  "<<#x<<"  is  "<< x << endl
#define D_v(x) for(int __i=0;__i<x.size();cerr<<x[__i++]<<" ")
#define D_m(m,rows,cols) for(int __i=0;__i<rows;cout<<endl,++__i) for(int __j=0;__j<cols;) cout <<m[__i][__j++]<<"  "
#define SWAP(a,b)({(a)^=(b);(b)^=(a);(a)^=(b);})

int main (){

  int N, No;
  scanf("%d", &N);
  No = N;
  while(N--){
    printf("Case #%d: [", No-N);
    map < pair<char, char>, char> com;
    map <char, char> opp;
    string in;
    
    int coms = 0;
    scanf("%d ", &coms);
    for(int i = 0; i < coms; ++i){
      char A,B,C;
      scanf("%c%c%c", &A,&B,&C);
      com[ make_pair(A,B)] = C;
      com[ make_pair(B,A)] = C;
    }
    
    int ops;
    scanf("%d ", &ops);
    for(int i = 0; i < ops; ++i){
      char A,B;
      scanf("%c%c", &A,&B);
      opp[A] = B;
      opp[B] = A;
    }
    
    int ws;
    scanf("%d ", &ws);
    if(ws > 0) getline(cin, in);

    vector<char> ans;
    ans.push_back(in[0]);
    for(int i = 1; i < ws; ++i){
      //      printf( "1--->" ); D_v(ans); printf( "<---1\n" );      
      char aux = com[make_pair(ans[ans.size()-1], in[i])];
      if( aux ){ ans[ ans.size()-1  ] = aux;
      }else{
        ans.push_back(in[i]);
        
        for(int j = 0; j < ans.size() ; ++j)
          if( opp[ ans[j] ] == in[i]){
            j = 0 ;
            while(j < ans.size()) ans[j++] = 0;
            break;
          }
        
      }
      //  printf( "2--->" );D_v(ans);printf( "<---2\n" );
    }
    int first = 1;
    for(int it = 0; it < ans.size(); ++it)
      if( ans[it] != 0) (first)? printf("%c", ans[it]), first=0 : printf(", %c", ans[it]);
    printf("]\n");    
    
  }
  return 0;
}
