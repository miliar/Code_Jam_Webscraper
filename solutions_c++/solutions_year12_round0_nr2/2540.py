#include<iostream>
#include<queue>
using namespace std;
#define N 100

int t,n,s,p;
int score[N];

int init(){
  cin >> t;
}

bool over_p(int x){
  int tmp;
  if(x%3==0 && x/3>=p)return true;
  for(int i=1 ; i<3 ; i++){
    tmp = x - i;
    if(tmp%3==0 && tmp/3+1>=p)return true;
  }
  return false;
}

bool surprising(int x){
  int temp;
  for(int i=2 ; i<4 ; i++){
    temp = x - i;
    if(temp<0)break;
    if(temp%3==0 && temp/3+2<=10 && temp/3+2>=p)return true;
  }
  return false;
}

int solve(){
  queue<int> q;
  int ret = 0;
  int cnt_s = 0;
  cin >> n >> s >> p;

  for(int i=0 ; i<n ; i++){
    int point,temp;
    bool flag = false;
    cin >> point;
    flag = over_p(point);
    if(flag)ret++;
    if(!flag){
      flag = surprising(point);
      if(flag)cnt_s++;
    }
    //if(flag)cout << point << endl;
  }

  ret+=min(cnt_s,s);
  return ret;
}

int main(){
  init();
  for(int i=0 ; i<t ; i++){
    cout << "Case #" << i+1 << ": " << solve() << endl;
  }
  return 0;
}
