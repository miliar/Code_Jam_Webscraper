#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

int
main(){

  char buf[500];
  string w = "elcome to code jam";

  cin.getline(buf, sizeof(buf) / sizeof(buf[0]));
  int n = atoi(buf);

  for(int i = 0; i < n; i++){
    cin.getline(buf, sizeof(buf) / sizeof(buf[0]));

    //debug    
    //    cout<<buf<<endl;

    unsigned long long v[500];
    for(int j = 0; j < 500; j ++) v[j] = 0;

    int ws = strlen(buf);
    //debug
    //    cout<<"len= "<<ws<<endl;

    for(int j = 0; j < ws; j++) if(buf[j] == 'w') v[j] = 1;

    for(int j = 0; j < w.size(); j++){

      for(int k = ws - 1; k >= 0; k--){

	v[k] = 0;

	if(buf[k] != w[j]) continue;
	int sum = 0;

	for(int l = k - 1; l >= 0; l--){
	  sum += v[l];
	}

	v[k] = sum;

      }

      //      debug
      //            cout<<w[j]<<": ";
      //            for(int k = 0; k < ws; k++){
      //      	cout<<v[k]<<" ";
      //            }
      //            cout<<endl;
      
    }

    unsigned long long ans = 0;
    for(int j = 0; j < ws; j++){
      ans += v[j];
    }

    stringstream ss;
    ss<<ans;
    string a = ss.str();
    reverse(a.begin(), a.end());
    if(a.size() < 4){
      while(a.size() != 4) a += '0';
    }

    cout<<"Case #"<<i+1<<": "<<a[3]<<a[2]<<a[1]<<a[0]<<endl;

  }
}
