#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(){
  int caseNum;
  cin >> caseNum;
  for(int tc=1; tc<=caseNum; tc++){
    int n;
    cin >> n;
    int posB = 1;
    int posO = 1;
    int timeB = 0;
    int timeO = 0;
    int time = 0;
    for(int i=0; i<n; i++){
      string str;int p;
      cin >> str >> p;
      if(str == "O"){
	int mov = abs(posO-p);
	mov = max(0,mov - (time - timeO));
	time += (mov + 1);
	timeO = time;
	posO = p;
      }
      else {
	int mov = abs(posB-p);
	mov = max(0,mov - (time - timeB));
	time += (mov + 1);
	timeB = time;
	posB = p;
      }
    }
    printf("Case #%d: %d\n",tc,time);
  }
  return 0;
}
