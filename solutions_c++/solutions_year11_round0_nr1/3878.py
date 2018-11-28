#include <iostream>
#include <cmath>
using namespace std;

int main(){
  int T;
  cin>>T;
  for(int zz=1;zz<=T;zz++){
    int posO=1,posB=1,deltaO=0,deltaB=0,t=0;
    int N;
    cin>>N;
    for(int i=0;i<N;i++){
      char R;
      int P;
      cin>>R>>P;
      if(R=='O'){
	int dif=1;
	if(posO!=P)
	  dif+=(int)abs((double)posO-P);
	dif = max(dif-deltaO,1);
	deltaO=0;
	deltaB+=dif;
	posO=P;
	t+=dif;
      }
      else{
	int dif=1;
	if(posB!=P)
	  dif+=(int)abs((double)posB-P);
	dif = max(dif-deltaB,1);
	deltaB=0;
	deltaO+=dif;
	posB=P;
	t+=dif;
      }
    }
    cout<<"Case #"<<zz<<": "<<t<<endl;
    
  }
  return 0;
}
