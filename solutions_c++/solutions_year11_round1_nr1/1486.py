#include <iostream>
#include <string>

//#define A 10000
//#define B 10000

using namespace std;

long long a[512*4][512],b[512];

int main(){
  int case_num, M, N,pd,pg, i, j, k;
  cin >> case_num;
  string ans;
  for(i=0;i<case_num;i++){
    cin >> N >> pd >> pg;
    int d,d_tmp,wd;
    if((pg==0 && pd > 0)||(pg==100 && pd!=100)){
      ans = "Broken";
    }else{
      ans = "Broken";
      for(d=1;d<N+1;d++){
	if((pd*d)%100==0){
	  wd=(pd*d)%100;
	  d_tmp=d;
	  ans = "Possible";
	}
      }
    }

    cout << "Case #" <<  i+1 << ": " << ans <<endl;
  }
  
  return 0;
}
