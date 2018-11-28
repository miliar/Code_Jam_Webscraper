// Michael Lawrence, mikeklawrence@gmail.com
// 2012-04-14
//
// Google Code Jam 2012 Qualification Round Problem B - Dancing with the
// Googlers
//
//
// Problem
// 
// You're watching a show where Googlers (employees of Google) dance, and then
// each dancer is given a triplet of scores by three judges. Each triplet of
// scores consists of three integer scores from 0 to 10 inclusive. The judges
// have very similar standards, so it's surprising if a triplet of scores
// contains two scores that are 2 apart. No triplet of scores contains scores
// that are more than 2 apart.
// 
// For example: (8, 8, 8) and (7, 8, 7) are not surprising. (6, 7, 8) and (6, 8,
// 8) are surprising. (7, 6, 9) will never happen.
// 
// The total points for a Googler is the sum of the three scores in that
// Googler's triplet of scores. The best result for a Googler is the maximum of
// the three scores in that Googler's triplet of scores. Given the total points
// for each Googler, as well as the number of surprising triplets of scores,
// what is the maximum number of Googlers that could have had a best result of
// at least p?
// 
// For example, suppose there were 6 Googlers, and they had the following total
// points: 29, 20, 8, 18, 18, 21. You remember that there were 2 surprising
// triplets of scores, and you want to know how many Googlers could have gotten
// a best result of 8 or better.
// 
// With those total points, and knowing that two of the triplets were
// surprising, the triplets of scores could have been:
// 
// 10 9 10
// 6 6 8 (*)
// 2 3 3
// 6 6 6
// 6 6 6
// 6 7 8 (*)
//
// The cases marked with a (*) are the surprising cases. This gives us 3
// Googlers who got at least one score of 8 or better. There's no series of
// triplets of scores that would give us a higher number than 3, so the answer
// is 3.
//
// Input
// 
// The first line of the input gives the number of test cases, T. T test cases
// follow. Each test case consists of a single line containing integers
// separated by single spaces. The first integer will be N, the number of
// Googlers, and the second integer will be S, the number of surprising triplets
// of scores. The third integer will be p, as described above. Next will be N
// integers ti: the total points of the Googlers.
// 
// Output
// 
// For each test case, output one line containing "Case #x: y", where x is the
// case number (starting from 1) and y is the maximum number of Googlers who
// could have had a best result of greater than or equal to p.
// 
// Limits
// 
// 1 ≤ T ≤ 100.
// 0 ≤ S ≤ N.
// 0 ≤ p ≤ 10.
// 0 ≤ ti ≤ 30.
// At least S of the ti values will be between 2 and 28, inclusive.
// Small dataset
// 
// 1 ≤ N ≤ 3.
// Large dataset
// 
// 1 ≤ N ≤ 100.
// Sample
// 
// 
// Input 
// 4
// 3 1 5 15 13 11
// 3 0 8 23 22 21
// 2 1 1 8 0
// 6 2 8 29 20 8 18 18 21
//  	
// Output 
//  
// Case #1: 3
// Case #2: 2
// Case #3: 1
// Case #4: 3
// 
// Solution:
//
// For each total t, there are 3 cases based on t mod 3
// t = 0 mod 3
//   t could be either the non-surprising scoreset ns(t) = t/3, t/3, t/3, or (only if t
//   > 0) the surprising scoreset s(t) = t/3 + 1, t/3, t/3 - 1
// t = 1 mod 3
//   t could be either the non-surprising scoreset ns(t) = t/3 + 1, t/3, t/3, or
//   (only if t > 1) the surprinsing scoreset s(t) = t/3 + 1, t/3 + 1, t/3 - 1
// t = 2 mod 3
//   t could be either the non-surprising scoreset ns(t) = t/3 + 1, t/3 + 1, t/3, or the
//   surpising scoreset s(t) = t/3 + 2, t/3, t/3
//
// It is true in each cases that the max value in s(t) scoreset is larger than
// the max value in ns(t). That means if a ns(t) has a value >= p then s(t) will
// as well.
//
// The goal is to maximize the number of googlers who scored >= p, subject to
// the constraint there are no more than S surprising scores. We count all
// surprising scores towards this S, which are such that s(t) >= p but ns(t) <
// p. We automatically count all scores such that both s(t) and ns(t) >= p

#include <iostream>

using namespace std;

// Computes the non-surprising score set for a total t, and returns the highest
// of the 3 scores in it.
int highestNonSurprisingScore(int t) {
  if (t % 3 == 0) {
    return t/3;
  } else {  // The cases for n = 1 mod 3 and n = 2 mod 3 are the same
    return t/3 + 1;
  }
}

// Computes the surprising score set for a total t, and returns the highest
// of the 3 scores in it.  Returns -1 if there is no surprising score set for t.
int highestSurprisingScore(int t) {
  if (t % 3 == 0) {
    if (t > 0) {
      return t/3 + 1;
    } else {
      return -1;
    }
  } else if (t % 3 == 1) {
    if (t > 1) {
      return t/3 + 1;
    } else {
      return -1;
    }
  } else {
    return t/3 + 2;
  }
}

// Runs this bitch!
int main(int argc, const char* argv[]) {
  int n_cases;
  cin >> n_cases;

  for (int i = 0; i < n_cases; ++i) {
    int N;
    cin >> N;

    int S;
    cin >> S;

    int p;
    cin >> p;

    int t;
    int total = 0;

    for (int j = 0; j < N; ++j) {
      cin >> t;
      int highest_surprising_score = highestSurprisingScore(t);
      int highest_nonsurprising_score = highestNonSurprisingScore(t);

      if (highest_surprising_score >= p && S > 0) {
        total++;
        if (highest_nonsurprising_score < p) {
          S--;
        }
      } else if (highest_nonsurprising_score >= p) {
        total++;
      }
    }

    cout << "Case #" << i+1 << ": " << total << endl;
  }
  return 0;
}
