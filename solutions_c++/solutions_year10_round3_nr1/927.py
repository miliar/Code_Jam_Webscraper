#include<iostream>
using namespace std;

int N;
int A[1000], B[1000];

int main(){

  int T;
  cin >> T;
  for(int t = 1; t <= T; t++){
    cin >> N;
    for(int i = 0; i < N; i++){
      cin >> A[i] >> B[i];      
    }
    int ans = 0;
    for(int i = 0; i < N; i++){
      for(int j = i+1; j < N; j++){
	if((A[i] > A[j] && B[i] < B[j]) ||
	   (A[i] < A[j] && B[i] > B[j])) ans++;
      }
    }
    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;
}
