#include <iostream>
#include <iomanip>
using namespace std;

double WP(int N, char arr[100], int exc){
  double win=0, num=0;
  for (int r = 0; r < N; r++){
    if (r == exc) continue;
    if (arr[r] == '0') num++;
    if (arr[r] == '1') num++,win++;
  }
  return win/num;
}
double OWP(int N, char arr[100][100], int exc){
  double total = 0;
  double num = 0;
  for (int y = 0; y < N; y++){
    if (arr[exc][y] == '.') continue;
    if (y == exc) continue;
    double a = WP(N, arr[y], exc);
    //cout << a;
    total += a;
    num++;
  }
  return total/num;
}
double OOWP(int N, char arr[100][100], int exc){
  double total = 0;
  double num = 0;
  for (int y = 0; y < N; y++){
    if (arr[exc][y] == '.') continue;
    if (y == exc) continue;
    double a = OWP(N, arr, y);
    //cout << a;
    total += a;
    num++;
  }
  return total/num;
}
int main(){
  int T;
  cin >> T;
  for (int t = 0; t < T; t++){
    int N;
    char arr[100][100] = {0};
    cin >> N;
    for (int y = 0; y < N; y++) cin >> arr[y];
    cout << "Case #" << t+1 << ":" << endl;
    for (int y = 0; y < N; y++){
      double total = 0;
      total += WP(N, arr[y], -1)*0.25;
      total += OWP(N, arr, y)*0.5;
      total += OOWP(N, arr, y)*0.25;
      cout << setprecision(12) << total << endl;
    }
    /*cout << OWP(N, arr, 0) << endl;
    cout << OWP(N, arr, 1) << endl;
    cout << OWP(N, arr, 2) << endl;
    cout << OWP(N, arr, 3) << endl;
    cout << OOWP(N, arr, 0) << endl;*/
  }
  return 0;
}
