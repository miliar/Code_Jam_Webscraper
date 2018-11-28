#include <iostream>
#include <fstream>
#include <cassert>
#include <unordered_set>
using namespace std;

char buf[512], buf2[512], buf3[512];
int get(int num, int B) {
  itoa(num, buf, 10);
  strcpy(buf2, buf);
  strcat(buf2, buf);
  //cout << "BUF: " << buf << "  BUF2: " << buf2 << endl;
  int n = strlen(buf);
  int count = 0;
  unordered_set<int> used;
  for (int i = 1; i < n; i++) {
    strncpy(buf3, buf2+i, n);
    buf3[n] = '\0';
    //cout << "BUF3 = " << buf3 << endl;
    if (buf3[0] == '0') continue;
    int num2 = atoi(buf3);
    if (num2 <= num || num2 > B) continue;
    if (used.find(num2) != used.end()) continue;
    used.insert(num2);
    count++;
    //cout << "(" << num << ", " << num2 << ")\n";
  }
  return count;
}

int main() {
  ifstream cin("data.txt");
  int N, A, B;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> A >> B;
    int count = 0;
    for (int j = A; j <= B; j++) {
      count += get(j, B);
    }
    cout << "Case #" << (i+1) << ": " << count << endl;
  }

}