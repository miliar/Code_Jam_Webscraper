#include<iostream>
using namespace std;

int main(){
  int t;
  cin>>t;
  char bd[4][4];
  for(int z=1;z<=t;z++){
    for(int i=0;i<4;i++){
      cin>>bd[i];
    }
    cout<<"Case #"<<z<<": ";
    int c;
    bool wn=false;
    for(int i=0;i<4;i++){
      c=0;
      for(int j=0;j<4;j++){
	if(bd[i][j]=='O' || bd[i][j]=='T')
	  c++;
      }
      if(c==4)
	wn=true;
    }
    for(int i=0;i<4;i++){
      c=0;
      for(int j=0;j<4;j++){
	if(bd[j][i]=='O' || bd[j][i]=='T')
	  c++;
      }
      if(c==4)
	wn=true;
    }
    c=0;
    for(int i=0;i<4;i++){
      if(bd[i][i]=='O' || bd[i][i]=='T')
	  c++;
      if(c==4)
	wn=true;
    }
    c=0;
    for(int i=0;i<4;i++){
      if(bd[3-i][i]=='O' || bd[3-i][i]=='T')
	  c++;
      if(c==4)
	wn=true;
    }
    if(wn){
      cout<<"O won"<<endl;
      continue;
    }
    for(int i=0;i<4;i++){
      c=0;
      for(int j=0;j<4;j++){
	if(bd[i][j]=='X' || bd[i][j]=='T')
	  c++;
      }
      if(c==4)
	wn=true;
    }
    for(int i=0;i<4;i++){
      c=0;
      for(int j=0;j<4;j++){
	if(bd[j][i]=='X' || bd[j][i]=='T')
	  c++;
      }
      if(c==4)
	wn=true;
    }
    c=0;
    for(int i=0;i<4;i++){
      if(bd[i][i]=='X' || bd[i][i]=='T')
	  c++;
      if(c==4)
	wn=true;
    }
    c=0;
    for(int i=0;i<4;i++){
      if(bd[3-i][i]=='X' || bd[3-i][i]=='T')
	  c++;
      if(c==4)
	wn=true;
    }
    if(wn){
      cout<<"X won"<<endl;
      continue;
    }
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	if(bd[i][j]=='.')
	  wn=true;
      }
    }
    if(!wn){
      cout<<"Draw"<<endl;
      continue;
    }
    cout<<"Game has not completed"<<endl;
  }
  return 0;
}
