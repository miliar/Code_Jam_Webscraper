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

char* itoa(int num,char *numchar){
  std::ostringstream os(""); os<<num;
  memcpy(numchar,os.str().c_str(),sizeof(char)*os.str().length());
  return numchar;
}

using namespace std;

int main(int argc,char* argv[]){
  ifstream ifs(argv[1]);
  int C; ifs>>C;
  for(int i=0;i<C;i++){
	int ret=0;
	int tmp[2]; ifs>>tmp[0]; ifs>>tmp[1];
	for(int j=tmp[0];j<tmp[1];j++){
	  stringstream os(""); os<<j;
	  string jstr=os.str();
	  vector<string> vec;
	  //cout<<j<<endl;
	  for(int k=1;k<jstr.length();k++){
		vec.push_back(jstr.substr(k)+jstr.substr(0,k));
		//cout<<vec[vec.size()-1]<<endl;
	  }
	  //cout<<endl;
	  for(vector<string>::iterator it=vec.begin();it!=vec.end();it++){
		istringstream iss((*it)); int tmpit; iss>>tmpit;
		if(tmpit>j && tmpit<=tmp[1]) ret++;
	  }
	}
	printf("Case #%d: %d\n",i+1,ret);
  }
  ifs.close();
  return 0;
}


