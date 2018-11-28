#include <iostream>

using namespace std;

int onext;
int bnext;
int n;
bool ob[100];

void oNext(){
  while(1){
    onext++;
    if(ob[onext]) return;
    if(onext>=n){
      return;
    }
  }
}
void bNext(){
  while(1){
    bnext++;
    if(!ob[bnext]) return;
    if(bnext>=n){
      return;
    }
  }
}

main(){
  int t;
  cin >> t;
  for(int tc=0;tc<t;tc++){
    cin >> n;
    int data[100];
    for(int i=0;i<n;i++){
      char c;
      cin >> c;
      cin >> data[i];
      if(c=='O'){
	ob[i]=true;
      }else{
	ob[i]=false;
      }
    }
    int opos=1, bpos=1;
    int cnt=0;
    onext=-1, bnext=-1;
    oNext();
    bNext();
    while(onext<n || bnext<n){
      cnt++;
      if(onext<bnext || bnext>=n){
	if(data[onext]==opos){
	  oNext();
	}else if(data[onext]<opos) opos--;
	else opos++;
	if(bnext<n){
	  if(data[bnext]>bpos) bpos++;
	  else if(data[bnext]<bpos) bpos--;
	}
      }else if(onext>bnext || onext>=n){
	if(data[bnext]==bpos){
	  bNext();
	}else if(data[bnext]<bpos) bpos--;
	else bpos++;
	if(onext<n){
	  if(data[onext]>opos) opos++;
	  else if(data[onext]<opos) opos--;
	}
      }
    }
    cout << "Case #" << tc+1 << ": " << cnt << endl;
  }
}
