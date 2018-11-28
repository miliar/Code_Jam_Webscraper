#include <iostream>
#include <utility>
#include <vector>
using namespace std;

int num_ropes;
vector< pair<int, int> > ropes;

bool isCrossed(pair<int,int> a, pair<int, int> b){
return  (a.first -b.first)*(a.second - b.second)<0;
}

int main(){
  int tstcse;
  cin>>tstcse;
  for(int tst=1;tst<=tstcse;tst++){
  int num_crossed=0;
    ropes.clear();
    cin>>num_ropes;
    for(int i=0; i<num_ropes; i++){
      pair<int, int> tmp;
      cin>>tmp.first>>tmp.second;
      ropes.push_back(tmp);
    }
    for(int i=0; i<num_ropes; i++){
      for(int j=i+1; j<num_ropes; j++){
	if(isCrossed(ropes[i],ropes[j]))num_crossed++;
      }
    }
    cout<<"Case #"<<tst<<": "<<num_crossed<<endl;
  }

}
