#include<iostream>

using namespace std;

int main(){
  int cas;
  cin>>cas;

  bool used[2000001];
  for(int ca=1; ca<=cas; ++ca){
    cout<<"Case #"<<ca<<": ";
    int a,b;
    cin>>a>>b;
    int ctn =0;
    for(int cur = a; cur<=b; cur++) {
      memset(used,0,sizeof(used));
      if (cur<10) continue;
      int temp =cur;
      int front=1;
      while(temp>=10) {
        front *= 10;
        temp /=10;
      }
      int back = 10;

      while(front > 1) {
        int flip = ((cur%back)*front)+(cur/back);
        if (flip>cur && flip<=b &&  !used[flip]) {
          used[flip] = true;
          ctn++;
        }
        //cout<<front<<" "<<back<<" "<<cur<<" "<<flip<<endl;
        front /=10;
        back*=10;
      }
    }
    cout<<ctn<<endl;
  }
}
