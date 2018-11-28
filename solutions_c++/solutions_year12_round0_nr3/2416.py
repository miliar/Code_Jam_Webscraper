#include <cstdio>
#include <set>

using std::set;

int CountDigits(int val) {
  int c = 0;
  while (val != 0) {
    val /= 10;
    ++c;
  }
  return c;
}

bool Check(int left, int right, int val) {
  return (val >= left && val <= right);
} 

int main() {
 FILE *inf = fopen("i.in", "r");
 FILE *of = fopen("o.out", "w");
 int num_tests;
 fscanf(inf, "%d", &num_tests);
  for (int t = 1; t <= num_tests; ++t) {
    int A, B;
    fscanf(inf, "%d %d", &A, &B);
    int n = CountDigits(A);
    int res = 0;

    for (int a = A; a <= B; ++a) {
        set<int> s;
        int temp = a;
        for (int i = 1; i < n; ++i) {
          int temp2 = temp / 10;
          temp %= 10;
          for (int j = 1; j < n; ++j) temp *= 10;
          temp += temp2;
          if (Check(a + 1, B, temp)) s.insert(temp);
        }
        res += s.size();
     }

     fprintf(of, "Case #%d: %d\n", t, res);
   }
  fclose(inf);
  fclose(of);
  printf("DONE!\n");
  return 0;
}