#include<iostream>

using namespace std;

int main(){
  int Q;
  ios::sync_with_stdio(false);
  cin >> Q;
  for(int q=1;q<=Q;q++){
    int N,M,Arr;
    cin >>N>>M>>Arr;
    bool pos = true,fnd=false;
    if(N*M<Arr)pos=false;
    int x0=0,x1=0,x2=0;
    int y0=0,y1=0,y2=0;
    if(pos){
      for(int i=1;i<=N && !fnd;i++){
	for(int j=1;j<=M && !fnd;j++){
	  for(int ni=1;ni<=N;ni++){
	    int tmp = ni*j-Arr;
	    if(abs(tmp)%i==0 && abs(tmp/i)<=M && abs(tmp/i-j)<=M){
	      fnd = true;
	      int nj = tmp/i;
	      if(tmp<0){
		x1 = i;
		x2 = ni;
		y1 = j-nj;
		y0 -= nj;
		y2 = 0;
	      }else{
		x1 = i;
		x2 = ni;
		y1 = j;
		y2 = nj;
	      }
	      break;
	    }
	  }
	}
      }
    }
    if(x2==0 && x1 == 0 && y2 == 0 && y1 == 0)pos=false;
    cout<<"Case #"<<q<<": ";
    if(pos)cout<<x0<<" "<<y0<<" "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
    else cout<<"IMPOSSIBLE"<<endl;
  }
  return 0;
}
