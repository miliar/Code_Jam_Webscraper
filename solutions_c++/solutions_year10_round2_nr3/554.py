#include <iostream>

using namespace std;


int checkOK(int s[],int size){
  /*
  //cout << size << " " << endl;
  for(int i = 0;i < size;i++){
    cout << s[i] << ",";
  }
  //cout <<  ;
  */
  
  int n = size + 1;
  while(n != 1){
    //cout << "now:" << n << endl;
    for(int i = 0;i < size;i++){
      if(s[i] == n){
	n = i+1;
	break;
      }
      if(s[i] > n){
	//cout << "NO" << endl;
	return 0;
      }
    }
  }
  //cout << "OK" << endl;
  return 1;
}

int create(bool contain[],int n,int now){
  if(now == n){
    int count = 0;
    int s[n+1];

    int j = 0;
    for(int i = 0;i < n;i++){
      if(contain[i])
	s[j++] = i;
    }
    return checkOK(s,j);
  }

  bool contain1[n+1];
  bool contain2[n+1];
  for(int i = 0;i < n;i++){
    contain1[i] = contain[i];
    contain2[i] = contain[i];
  }
  contain1[now] = true;
  contain2[now] = false;
  
  return (create(contain1,n,now+1) + create(contain2,n,now+1)) % 100003;
}

main(){
  int T;
  cin >> T;

  int count = 0;
  int results[26];

  for(int n = 2; n<=25;n++){
    bool contain[n+1];
    
    for(int i = 0;i <= n;i++){
      contain[i] = false;
    }
    contain[0] = false;
    contain[1] = false;

    int result = create(contain,n,2);

    results[n] = result;
  }
  
  
  for(int t = 0;t < T;t++){
    int n;
    cin >> n;
    //n = t+2;
    //cout << "n:" << n << endl;
    cout << "Case #" << (t+1) << ": " << results[n] << endl;
  }
  return 0;
}
