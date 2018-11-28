#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
int power(int, int);
void display_list (vector <int> list);
int calculate (vector <int> factors);
int main (int argc, char *argv[]) {

  int T, L, P, C ;

  cin >> T;

  // for each test case
  for (int t=1; t<=T; t++) {
    int no_of_test = 0;
    cin >> L >> P >> C;
    //cout << L << " "<< P << " " << C << endl;
    vector <int> factors;
    int index = 1;
    long long pow1 = pow(C, index);
    long long factor = L*pow1;
    index++;
    while (factor < P) {
      factors.push_back(factor);
      pow1  = pow(C, index); 
      factor = L*pow1;
      index++;
    }
    //  display_list (factors);

    // calculate the no of tests to be done
    int tests  = calculate (factors) ;
    cout << "Case #" << t << ": "<< tests << endl;
  }

  return 0;
}

int power(int a, int b)
{
  int c=a;
  for (int n=b; n>1; n--) c*=a;
  return c;
}

void display_list (vector <int> list) {
  for (int i=0; i < list.size(); i++) {
    cout << list[i] << " ";
  }
  cout << endl;
}

int calculate (vector <int> factors) {
  if (factors.size() > 2 ) {
    int mid = factors.size()/2;
    vector <int> list1;
    vector <int> list2;
    for (int i=0; i<mid; i++) {
      list1.push_back(factors[i]);
    }
    for (int i=mid+1; i<factors.size(); i++) {
      list2.push_back(factors[i]);
    }

    int test1 = calculate (list1);
    int test2 = calculate (list2);

    if (test1 < test2) {
      return test2+1;
    } else {
      return test1+1;
    }
  } else {
    return factors.size();
  }
}
