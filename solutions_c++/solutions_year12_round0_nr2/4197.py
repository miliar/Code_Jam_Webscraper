#include <iostream>

using namespace std;


int main ()
{
  int T,N,S,p;
  cin >> T;
  for(int i=1;i<=T;i++){
    int Yes=0,No=0,MayBe=0;
    cin >> N;
    cin >> S;
    cin >> p;
    int googlers[N];
    for (int j=0;j<N;j++) {
      cin >> googlers[j];
      if ( googlers[j] != 0 && p != 0) {
	if ( googlers[j] >= (3*p-2) ) Yes++;
	else if ( googlers[j] < (3*p-4) ) No++;
	else MayBe++;
      }
      if (p==0){ 
	Yes=N;
      }
    }
    int ans = Yes + min(MayBe,S);
    cout << "Case #"<<i<<": "<< ans << endl;
  }
  return 0;
}
