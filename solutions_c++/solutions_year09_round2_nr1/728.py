#include <iostream>
#include <vector>
#include <sstream>
#include <iomanip>

void skipws(std::istream& is) {
  char c;
  for(;;) {
    if(!is.get(c)) {
      return;
    }
    if(!isspace(c)) {
      is.unget();
      return;
    }
  }
}


double
doit(std::istream& is,
     const std::vector<std::string>& features,
     double p){
  skipws(is);
  char c;
  if(!is.get(c)) {
    assert(0);
  }
  //std::cerr << c << std::endl;
  assert(c=='(');

  skipws(is);
  double w;
  is >> w;

  skipws(is);
  if(is.peek() == ')') {
    is.get(c);
    return p*w;
  }

  skipws(is);
  std::string feature;
  is >> feature;

  float p0 = doit(is, features, p*w);
  float p1 = doit(is, features, p*w);
  if(std::find(features.begin(),features.end(),feature) != features.end()) {
    p = p0;
  } else {
    p = p1;
  }
  
  skipws(is);
  if(!is.get(c)) {
    assert(0);
  }
  assert(c==')');
  return p;
}

int main() {
  int N;
  std::cin >> N;
  for(int i = 0 ; i< N; i++ ) {
    int L;
    std::cin >> L;
    skipws(std::cin);

    std::string treerep;
    for( int j = 0 ; j < L ; j++ ) {
      std::string line;
      std::getline(std::cin,line);
      //std::cerr << line << std::endl;
      treerep += " " + line;
    }
    //std::cerr << treerep;

    std::cout << "Case #" << (i+1) << ":" << std::endl;

    int number_of_animals;
    std::cin >> number_of_animals;
    for( int j = 0 ; j< number_of_animals; j++ ) {
      std::string animal;
      std::cin >> animal;
      int feature_count;
      std::cin >> feature_count;

      //std::cerr << animal << feature_count;
      std::vector<std::string> features;
      for( int k = 0 ; k < feature_count; k++ ) {
        std::string feature;
        std::cin >> feature;
        features.push_back(feature);
      }

      std::istringstream iss(treerep);
      std::cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
      std::cout << std::setw(8) << doit(iss, features, 1.0) << std::endl;
    }
  }

  return 0;
}
