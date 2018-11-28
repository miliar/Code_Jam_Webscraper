#define _USE_MATH_DEFINES 1
// include files
// c header
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cassert>
#include<cfloat>
#include<ctime>
#include<climits>

// for visual c++
#ifdef _MSC_VER
#define finite _finite
#define isnan _isnan
#endif

// c++ header
#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<sstream>
#include<map>
//#include<random>
#include<algorithm>
#include<numeric>

/*!
 * @brief vector converter to string
 * @param vec a vector
 * @param string quontized by ","
 */
template<typename T> std::string vec2str(std::vector< T > vec){
  std::stringstream os("");
  for(int i=0;i<vec.size();i++)
    os<<vec.at(i)<<",";
  return os.str().substr(0,os.str().length()-1);
};


using namespace std;

int main(int argc,char* argv[]){
  ifstream ifs(argv[1]);
  int C; ifs>>C;
  for(int i=0;i<C;i++){
	int N,S,p; ifs>>N; ifs>>S; ifs>>p;
	int check[N][2]; bool checkb[N][2];
	int ret=0;
	for(int j=0;j<N;j++){
	  int tmp[3]; ifs>>tmp[0];
	  if(tmp[0]==0 || tmp[0]==1){
		check[j][0]=tmp[0]; check[j][1]=-1;
		checkb[j][0]=(check[j][0]>=p);
		checkb[j][1]=false;
	  }else{
		tmp[1]=tmp[0]/3; tmp[2]=tmp[0]%3;
		if(tmp[2]==0)	check[j][0]=tmp[1];
		else check[j][0]=tmp[1]+1;
		checkb[j][0]=(check[j][0]>=p);
		if(tmp[2]==2) check[j][1]=tmp[1]+2;
		else check[j][1]=tmp[1]+1;
		if(check[j][1]>10){
		  check[j][1]=-1;
		  checkb[j][1]=false;
		}else checkb[j][1]=(check[j][1]>=p);
	  }
	  if(checkb[j][0]) ret++;
	  if(checkb[j][1] && !checkb[j][0] && S>0){
		ret++;
		S--;
	  }
	}
	printf("Case #%d: %d\n",i+1,ret);
  }
  ifs.close();
  return 0;
}


