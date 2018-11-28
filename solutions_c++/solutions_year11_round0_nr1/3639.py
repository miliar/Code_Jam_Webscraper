#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

main(){
  int T,N;
  int t1,t2,P;
  int c1,c2;
  int m;
  char R;
  ifstream ifs("A-large");
  ofstream ofs("ans-a");
  ifs>>T;
  for(int i=1;i<=T;++i){
    ifs>>N;
    t1=t2=0;
    c1=c2=1;
    for(int j=0;j<N;++j){
      ifs>>R>>P;
      if(R=='O'){
	if((c1-P)>0) m = c1-P;
	else m = P-c1;
	if((m+t1)>t2) t1 = m+t1+1;
	else t1=t2+1;
	c1=P;
      }
      if(R=='B'){
	if((c2-P)>0) m = c2-P;
	else m = P-c2;
	if((m+t2)>t1) t2 = m+t2+1;
	else t2=t1+1;
	c2=P;
      }
    }
    if(t1>t2)
      ofs<<"Case #"<<i<<": "<<t1<<endl;
    else
      ofs<<"Case #"<<i<<": "<<t2<<endl;
  }
  ifs.close();
  ofs.close();
}
