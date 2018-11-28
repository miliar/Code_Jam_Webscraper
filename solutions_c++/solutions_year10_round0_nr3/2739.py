#include <iostream>
using namespace std;

int main()
{
  int t, T;
  cin >> T;
  for(t = 1; t <= T; t++){
    int R, k, N, i;
    int *size;
    bool *visit;
    cin >> R >> k >> N;
    size = new int[N];
    visit = new bool[N];
    for(i = 0; i < N; i++){
      cin >> size[i];
      visit[i] = 0;
    }
    // find the loop
    int ptr = 0;
    int income1, income2, income;
    income1 = income2 = 0;
    int len1, len2;
    len1 = len2 = 0;
    while(visit[ptr] == 0){
      visit[ptr] = 1;
      int count = 0;
      int car = 0;
      while(car + size[ptr] <= k &&
	    count < N){
	car += size[ptr++];
	count++;
	if(ptr == N){
	  ptr = 0;
	}
      }
      income1 += car;
      len1++;
    }
    int loop = ptr;
    ptr = 0;
    while(ptr != loop){
      int count = 0;
      int car = 0;
      while(car + size[ptr] <= k &&
	    count < N){
	car += size[ptr++];
	count++;
	if(ptr == N){
	  ptr = 0;
	}
      }
      income2 += car;
      len2++;
    }
    income1 -= income2;
    len1 -= len2;
    income = income2 + (R - len2) / len1 * income1;
    ptr = loop;
    for(i = 0; i < (R - len2) % len1; i++){
      int count = 0;
      int car = 0;
      while(car + size[ptr] <= k &&
	    count < N){
	car += size[ptr++];
	count++;
	if(ptr == N){
	  ptr = 0;
	}
      }
      income += car;
    }
    cout << "Case #" << t << ": " << income << endl;
    delete [] size;
  }
  return 0;
}
