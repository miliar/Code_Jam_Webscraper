#include <iostream>
#include <fstream>
#include <vector>


int main(){

  std::ifstream fp_in("C-small-attempt0.in");
  std::ofstream fp_out("C-small.out");
  int T;
  fp_in>>T;
  int R, k, N;
  std::vector<int> group;
  int tmp;

  int profit, count = 1;

  while (fp_in>>R>>k>>N){
    group.clear();
    //std::cout<<" r k n  "<<R<<" "<<k<<" "<<N<<std::endl;
    for (int i = 0 ;i!=N; ++i){
      fp_in>>tmp;
      group.push_back(tmp);
    }
    
    tmp = 0;
    for (std::vector<int>::iterator iter = group.begin(); iter!=group.end(); ++iter){
      //std::cout<<*iter<<" ";
      tmp += *iter;
    }

    if (tmp<=k) profit = R*tmp;
    else {
      profit  = 0;
      std::vector<int>::iterator iter= group.begin();
      for (int j = 1; j<=R; ++j){
	tmp = *iter;
	while (tmp<=k){
	  iter++;
	  if (iter!=group.end()) tmp+=(*iter);
	  else {
	    iter = group.begin();
	    tmp+=(*iter);
	  }
	}
	tmp-=(*iter);
	profit += tmp;
      }
    }
    fp_out<<"Case #"<<count<<": "<<profit<<std::endl;      
    count++;
    //std::cout<<std::endl;
  }
  fp_in.close();
  fp_out.close();
}
