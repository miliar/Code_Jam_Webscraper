#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

struct data {
  char color;
  int k;
};

int main(){
  int t, n;

  cin >> t;

  for(int i = 0; i < t; i++){
    cin >> n;
    vector<data> V, ORANGE, BLUE;
    for(int j = 0; j < n; j++){
      data d;
      cin >> d.color >> d.k;
      V.push_back(d);
      if(d.color == 'O')
	ORANGE.push_back(d);
      else
	BLUE.push_back(d);
    }


    int ocurrent, bcurrent, current, time = 0, op, bp;
    ocurrent = bcurrent = current = 0;
    op = bp = 1;

    while(current < V.size()){
      bool oflg, bflg;
      oflg = bflg = 0;

      if(ocurrent < ORANGE.size() && ORANGE[ocurrent].k != op){
	if(ORANGE[ocurrent].k > op)
	  op++;
	else
	  op--;
	oflg = 1;
      }

      if(bcurrent < BLUE.size() && BLUE[bcurrent].k != bp){
	if(BLUE[bcurrent].k > bp)
	  bp++;
	else
	  bp--;
	bflg = 1;
      }

      if(V[current].color == 'O'){
	if(!oflg && V[current].k == op){
	  current++;
	  ocurrent++;
	}
      }else{
	if(!bflg && V[current].k == bp){
	  current++;
	  bcurrent++;
	}
      }
      time++;
    }
    cout << "Case #" << i + 1 << ": " << time << endl;
  }
}
