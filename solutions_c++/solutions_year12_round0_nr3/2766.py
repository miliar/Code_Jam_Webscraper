#include <stdio.h>

#define SIZE (2000001)

struct unit {
  int use[10];
  int hash;
};

static unit table[SIZE];

void MakeTable(int A, int B, int D) {
  for (int i=A; i!=B+1; ++i) {

    // make table
    for (int j=0; j!=10; ++j) {
      table[i].use[j] = 0;
    }

    // make use and number
    int val = i;
    //    printf("-%d-\n", val);
    while (1) {
      //      printf("%d, %d\n", val, val % 10);
      table[i].use[val % 10] ++;
      if (val / 10 >= 10) {
        val = (val - (val % 10)) / 10;
      } else {
        table[i].use[val / 10] ++;
        break;
      }
    }

    // make hash
    table[i].hash = 0;
    for (int j=0; j!=10; ++j) {
      table[i].hash += table[i].use[j]*j;
    }
    //        printf("hash %d\n", table[i].hash);
  }
}

int BitRotate(int V, int D) {
  //    printf("rot %d ",V);
  int Vmod = V % 10;
  V /= 10;
  for (int i=0; i!=D-1; i++) {
    Vmod *=10;
  }
  //    printf("%d\n", V + Vmod);
  return V + Vmod;
}

bool Check(int A, int B, int D) {
  //  printf("Check %d\n",B);
  int B_ = B;
  for (int i=0; i!=D; ++i) {
    B_ = BitRotate(B_, D);
    if (A == B_) {
      return true;
    }
  }
  return false;
}

int Solve(int A, int B, int D) {
  int count = 0;
  for (int i=A; i!=B+1; ++i) {
    for (int j=i+1; j!=B+1; ++j) {
      // check with hash
      if (i!= j) {
        if (table[i].hash == table[j].hash) {
          // check full count
          bool match = true;
          //        printf("%d-%d\n", i, j);
          for (int k=0; k!=10; ++k) {
            if (table[i].use[k] != table[j].use[k]) {
              match = false;
              break;
            }
          }
          if (match) {
            // OK
            if (Check(i, j, D)) {
              //            printf("%d-%d\n", i, j);
            count++;
            }
          }
        }
      }
    }
  }
  return count;
}

int GetDigit(int A) {
  int digit = 1;
  int div = 1;
  while (1) {
    if (A / div >= 10) {
      ++digit;
      div *= 10;
    } else {
      return digit;
    }
  }
}

int main() {
  // read
  int T;
  scanf("%d", &T);
  // loop
  int A, B;
  int i, j;
  for (i = 1; i <= T; ++i) {
    scanf("%d %d", &A, &B);
    printf("Case #%d: ", i);

    // none
    int D = GetDigit(A);
    if (D == 1) {
      printf("0\n");
    } else {
      MakeTable(A, B, D);
      printf("%d\n", Solve(A, B, D));
    }
  }
  return 0;
}
