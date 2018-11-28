#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main(int argc, char *argv[])
{vector<string>V(4); string S;
 int i,j,w,T,L,K,N,X;
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 getline(cin,S);
 stringstream SS(S);
 SS>>T;
 
 for(L=1;L<=T;L++)
 {for(K=0;K<4;K++)
  getline(cin,V[K]);
  
  w=0;
  for(N=X=i=0;i<4;i++)if(V[i][i]=='T')N++,X++; 
                      else if(V[i][i]=='X')X++;
                      else if(V[i][i]=='O')N++;
  
//  cout<<N<<' '<<X<<endl;
                      
  if(N<4 && X<4)
  for(N=X=i=0;i<4;i++)if(V[i][3-i]=='T')N++,X++; 
                      else if(V[i][3-i]=='X')X++;
                      else if(V[i][3-i]=='O')N++;
  
//  cout<<N<<' '<<X<<endl;
                      
  for(i=0;i<4 && N<4 && X<4;i++)
  {for(j=N=X=0;j<4;j++)
                      if(V[i][j]=='T')N++,X++; 
                      else if(V[i][j]=='X')X++;
                      else if(V[i][j]=='O')N++;
                      else w=1;
//  cout<<N<<' '<<X<<endl;
  }
  for(i=0;i<4 && N<4 && X<4;i++)
  {for(j=N=X=0;j<4;j++)
                      if(V[j][i]=='T')N++,X++; 
                      else if(V[j][i]=='X')X++;
                      else if(V[j][i]=='O')N++;
//  cout<<N<<' '<<X<<endl;
 }
  cout<<"Case #"<<L<<": ";
  if(X==4)cout<<"X won";
  else if(N==4)cout<<"O won";
  else if(w==0)cout<<"Draw";
  else cout<<"Game has not completed";
  cout<<endl;
  getline(cin,S);                    
  
 }
//    system("PAUSE");
    return EXIT_SUCCESS;
}
