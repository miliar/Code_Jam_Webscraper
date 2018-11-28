 
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

typedef vector<int> intv;
typedef vector<float> floatv;
typedef vector<double> doublev;


/**
 * Cast an S type object to an R type object.
 * Should work for most data/types and strings
**/
template<typename R, typename S> 
R cast(const S& s) {

	stringstream ss;
	ss << s;
	R result;
	ss >> result;
	return result;
}

// summing functor
template<typename T>
struct summer_t {
  T sum;
  summer_t(): sum(0) {}
  void operator() ( const T& t) { sum += t; }
};

/**
 * Sum contents of array/set/whatever
 **/
template<typename T,typename V>
T sum(const V& v) {
  summer_t<T> summer;
  return for_each(v.begin(),v.end(),summer).sum;
}



int process(intv&,intv&);

int main (int argc, char * const argv[]) {


ifstream in("test.in");
ofstream out("test.out");

int t,cur_case=1;
in >> t; // number cases


while(cur_case<=t) {
 cout << "Test: " << cur_case << endl;
 int n,tmp;
 in >> n; // vector size
 int cur=n;
 intv v1,v2;
 while (cur--) {   
  in >> tmp;
  v1.push_back(tmp);
 }
 cur=n;
 while(cur--) {
  in >> tmp;
  v2.push_back(tmp);
 }
 int result=process(v1,v2);
 out << "Case #" << cur_case++ << ": " << result << endl;
}


}

int scalar(intv& v1, intv& v2) {
 int s=v1.size();
 int sum=0;
 while (--s >= 0) {
  sum += v1[s] * v2[s];
 }
 return sum;
}

int process(intv& v1,intv& v2) {
 sort(v1.begin(),v1.end());
 int lowest= 1 << 30;
 do {
  int sum=scalar(v1,v2);
  //cout << sum << endl;
  if (sum<lowest) lowest=sum;
 } while ( next_permutation( v1.begin(), v1.end() ) );
 
 return lowest;

}