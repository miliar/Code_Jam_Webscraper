// Michael Lawrence, mikeklawrence@gmail.com
// 2012-04-14
//
// Google Code Jam 2012 Qualification Round Problem C - Recycled Numbers
//
//
// Problem
// 
// Do you ever become frustrated with television because you keep seeing the
// same things, recycled over and over again? Well I personally don't care about
// television, but I do sometimes feel that way about numbers.
// 
// Let's say a pair of distinct positive integers (n, m) is recycled if you can
// obtain m by moving some digits from the back of n to the front without
// changing their order. For example, (12345, 34512) is a recycled pair since
// you can obtain 34512 by moving 345 from the end of 12345 to the front. Note
// that n and m must have the same number of digits in order to be a recycled
// pair. Neither n nor m can have leading zeros.
// 
// Given integers A and B with the same number of digits and no leading zeros,
// how many distinct recycled pairs (n, m) are there with A ≤ n < m ≤ B?
// 
// Input
// 
// The first line of the input gives the number of test cases, T. T test cases
// follow. Each test case consists of a single line containing the integers A
// and B.
// 
// Output
// 
// For each test case, output one line containing "Case #x: y", where x is the
// case number (starting from 1), and y is the number of recycled pairs (n, m)
// with A ≤ n < m ≤ B.
// 
// Limits
// 
// 1 ≤ T ≤ 50.
// A and B have the same number of digits.
// 
// Small dataset
// 
// 1 ≤ A ≤ B ≤ 1000.
// 
// Large dataset
// 
// 1 ≤ A ≤ B ≤ 2000000.
// 
// Sample
// 
// 
// Input 
// 4
// 1 9
// 10 40
// 100 500
// 1111 2222
//  	
// Output 
// Case #1: 0
// Case #2: 3
// Case #3: 156
// Case #4: 287
// 
// Solution:
//
// Iterate from n = A to N = B-1
// For each n, compute the (<= 6) permutations made by cycling 0 < k < digits(n)
// digits of n from the back to the front.
// For each permutation p, check that n < p <= B holds.

#include <cstring>
#include <cstdlib>
#include <iostream>
#include <set>

using namespace std;

int main(int argc, const char* argv[]) {
  int n_cases;
  cin >> n_cases;

  for (int i = 0; i < n_cases; ++i) {
    int A;
    cin >> A;
    int B;
    cin >> B;

    int total = 0;

    char n_str[8];
    char recycled[8];

    // Tracks the m's already seen for this n (so that they aren't counted
    // twice)
    set<int> alreadySeen;

    for (int n = A; n < B; n++) {
      sprintf(n_str, "%d", n);
      alreadySeen.clear();

      int digits = strlen(n_str);
      recycled[digits] = 0;

      // j represents the number of recycled chars
      for (int j = 1; j < digits; j++) {
        if (n_str[digits-j] != '0') {  // Otherwise m will have a leading 0
          strncpy(recycled, &n_str[digits-j], j);
          strncpy(&recycled[j], n_str, digits-j);
          int m = static_cast<int>(strtol(recycled, NULL, 10));

          if (n < m && m <= B && alreadySeen.find(m) == alreadySeen.end()) {
            alreadySeen.insert(m);
            total++;
          }
        }
      }
    }

    cout << "Case #" << i+1 << ": " << total << endl;
  }
  return 0;
}
