#include <iostream>
#include <vector>

using namespace std;


void gen_and_calc_partition(vector< unsigned int >& bitArray,
                            const vector< unsigned int >& num,
                            unsigned int pos, unsigned int& MAX);


int main() {
  //read in the number of test cases
  unsigned int T;
  cin >> T;

  for (unsigned int i = 0; i < T; ++i) {
    //read in the number of candies
    unsigned int N;
    cin >> N;

    //read in the candies
    vector< unsigned int > num(N, 0);
    for (unsigned int j = 0; j < N; ++j)
      cin >> num[j];

    vector< unsigned int > bitArray(N, 0);

    unsigned int MAX = 0;
    gen_and_calc_partition(bitArray, num, 0, MAX);

    //display answer
    cout <<"Case #"<<i+1<<": ";

    if (MAX == 0)
      cout <<"NO";
    else
      cout <<MAX;

    cout <<"\n";
  }

  return 0;
}


void gen_and_calc_partition(vector< unsigned int >& bitArray, 
			    const vector< unsigned int >& num, 
			    unsigned int pos, unsigned int& MAX) {
  if (pos == num.size()) {
    //generate the two partitions
    vector< unsigned int > set1, set2;
    for (unsigned int i = 0; i < pos; i++) {
      if (bitArray[i] == 1)
	set1.push_back(num[i]);
      else
	set2.push_back(num[i]);
    }

    //don't continue if either set is empty or full
    if (set1.empty() || set2.empty() || set1.size() == pos || set2.size() == pos)
      return;

    unsigned int xsum1 = 0, xsum2 = 0, sum1 = 0, sum2 = 0;
    for (unsigned int i = 0; i < set1.size(); ++i) { 
      xsum1 ^= set1[i];
      sum1 += set1[i];
    }

    for (unsigned int i = 0; i < set2.size(); ++i) {
      xsum2 ^= set2[i];
      sum2 += set2[i];
    }

    //don't continue if the two xor sums are not equal
    if (xsum1 != xsum2)
      return;

    //determine the max
    if (sum1 > MAX)
      MAX = sum1;
    
    if (sum2 > MAX)
      MAX = sum2;

    return;
  }
  
  for (unsigned int i = 0; i <= 1; i++) {
    bitArray[pos] = i;
    gen_and_calc_partition(bitArray, num, pos+1, MAX);
  }
}
