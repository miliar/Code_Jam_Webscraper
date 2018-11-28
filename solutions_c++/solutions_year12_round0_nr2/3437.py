#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
  ifstream ifs("B-large.in");
  ofstream ofs("outputBs");
  int i,j,t,n,s,p,ti[100],maxti,minti;
  ifs >> t;
  for(i=0; i<t;i++){
    ifs >> n >> s >> p;
    int ans=0;
    if(p >= 2){
      maxti=(p-1)*3+1;
      minti=(p-2)*3+2;
      for(j=0;j<n;j++){
	ifs >> ti[j];
	if(ti[j] >= maxti)
	  ans++;
	else if(s > 0 && ti[j] >= minti){
	  ans++;
	  s--;
	}
      }
    }
    else{
      maxti=p;
      minti=0;
      for(j=0;j<n;j++){
	ifs >> ti[j];
	if(ti[j] >= maxti)
	  ans++;
      }
    }
    ofs << "Case #" << i+1 << ": " << ans << endl; 
  }
  return 0;
}
