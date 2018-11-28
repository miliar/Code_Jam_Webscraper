#include<iostream>
#include<bitset>
#include<string>
using namespace std;

class A{
private:
  bool finish;
  bitset<4> map_x[4];
  bitset<4> map_o[4];
public:
  A(){
    finish=true;
    for(int i=0;i<4;i++){
      map_x[i].reset();
      map_o[i].reset();
    }
  }
  void input(){
    for(int i=0;i<4;i++){
      string tmp;
      while(cin>>tmp,tmp.size()==0);
      //cout<<"input "<<tmp<<endl;
      for(int j=0;j<4;j++){
        switch(tmp[j]){
	  case '.':
	    finish=false;
	    break;
	  case 'T':
	    map_x[i][j]=true;
	    map_o[i][j]=true;
	    break;
	  case 'O':
	    map_o[i][j]=true;
	    break;
	  case 'X':
	    map_x[i][j]=true;
	    break;
	}
      }
    }
  }

  bool x_won(){
    for(int i=0;i<4;i++){
      if(map_x[0][i]&&map_x[1][i]&&map_x[2][i]&&map_x[3][i]){
        return true;
      }
      if(map_x[i][0]&&map_x[i][1]&&map_x[i][2]&&map_x[i][3]){
        return true;
      }
    }
    if(map_x[0][0]&&map_x[1][1]&&map_x[2][2]&&map_x[3][3]){
      return true;
    }
    if(map_x[0][3]&&map_x[1][2]&&map_x[2][1]&&map_x[3][0]){
      return true;
    }
    return false;
  }

  bool o_won(){
    for(int i=0;i<4;i++){
      if(map_o[0][i]&&map_o[1][i]&&map_o[2][i]&&map_o[3][i]){
        return true;
      }
      if(map_o[i][0]&&map_o[i][1]&&map_o[i][2]&&map_o[i][3]){
        return true;
      }
    }
    if(map_o[0][0]&&map_o[1][1]&&map_o[2][2]&&map_o[3][3]){
      return true;
    }
    if(map_o[0][3]&&map_o[1][2]&&map_o[2][1]&&map_o[3][0]){
      return true;
    }
    return false;
  }

  string solve(){
    input();

    bool x=x_won(),o=o_won();
    if(x&&o){
      return "Draw";
    }else if(x){
      return "X won";
    }else if(o){
      return "O won";
    }else if(!finish){
      return "Game has not completed";
    }else{
      return "Draw";
    }
  }
};


int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    A a;
    cout<<"Case #"<<i+1<<": "<<a.solve()<<endl;;
  }
}
