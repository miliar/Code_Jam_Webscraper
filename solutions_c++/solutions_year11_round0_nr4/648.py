#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin >> T;
  int case_num = 1;
  while(T>0)
  {
    int N;
    cin >> N;
    vector<int> v(N);
    for(int i=0;i<N;i++) cin >> v[i];
    vector<int> model = v;
    sort(model.begin(), model.end());
    //for(int i=0;i<N;i++) cout << v[i] << "|"; cout << endl; //debug
    //for(int i=0;i<N;i++) cout << model[i] << "|"; cout << endl; //debug
    int times = 0;
    for(int i=0;i<N;i++) if(v[i] != model[i]) times++;
    cout << "Case #" << case_num << ": " << times << endl; 

    T--; case_num++;
  }

  return 0;
}
