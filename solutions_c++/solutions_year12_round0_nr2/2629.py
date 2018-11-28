#include <iostream>

using namespace std;

//
// If  t%3 == 0 then either
//   
//   t = x + (x+1) + (x+2) = 3(x+1)  (surprising)     max = t/3 + 1
//   t = x + x + x         = 3x      (not surprising) max = t/3
//
// Special cases
// 
//   t = 30 is always 10 + 10 + 10   (not surprising)
//   t = 0  is always 0  + 0  + 0    (not surprising)


//
// If t%3 == 1 then
//
//   t = x + x + (x-2) = 3(x-1) + 1  (surpising)      max = t/3 + 1
//   t = x + x + (x+1) = 3x + 1      (not surprising) max = t/3 + 1
//
// Special cases
//
//   t = 1 is always 0 + 0 + 1       (not surprising)
//   

//
// If t%3 == 2 then
//
//   t = x + x + (x+2) = 3x + 2      (surprising)      max = t/3 + 2
//   t = x + x + (x-1) = 3(x-1) + 2  (not surprising)  max = t/3 + 1
//
// Special cases
// 
//   t = 29 is always 10 + 10 + 9    (not surprising)
//   

// Hence, each total t has a maximum surprising and maximum
// non-surprising triple, unless t is in {0,1,29,30}.

// We need exactly S surprising scores t
//
// First, we eliminate all t in {0,1,29,30} (counting max >= p)
// 
// For all t with minmax >= p
//   minmax >= p implies max >= p, so count t (++C)
//   S := max(S-1, 0)
//   --N
//
// For all t with maxmax < p
//   maxmax < p implies max < p, so don't count t
//   S := max(S-1, 0)
//   --N
//
// For all the t that are left
//   it must hold that both
//     minmax <  p (the not surprising case)
//     maxmax >= p (the surprising case)
//   so we can choose any S of them to fulfill surprisingness, and the
//   rest will give max >= p
//     
// Hence, count = C + N - S
//

// NOTE: 0 <= p <= 10

int minmax(int t) {
  if (t%3 == 0)
    return t/3;
  else
    return (t/3) + 1;
}

int maxmax(int t) {
  if (t%3 == 2)
    return (t/3) + 2;
  else
    return (t/3) + 1;
}

int main() {
  int num_tests;
  cin >> num_tests;
  for (int test = 1; test <= num_tests; ++test) {
    int N, S, p;
    cin >> N >> S >> p;

    int c = 0;
    int n = N;
    
    for (int i = 0; i < N; ++i) {
      int t;
      cin >> t;

      // edge cases when t is never surprising
      if (t == 0 || t == 1) {
        if (p == t)
          ++c;
        continue;
      }
      if (t == 29 || t == 30) {
        ++c;
        continue;
      }

      // all other t can be surprising and non-surprising
      if ((minmax(t) < p) && (maxmax(t) >= p)) {
        if (S > 0) {
          ++c;
          --S;
        }
      }
      if (minmax(t) >= p) {
        ++c;
      }
    }

    cout << "Case #" << test << ": " << c << '\n';
  }
  return 0;
}
