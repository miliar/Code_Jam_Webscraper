#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main() {

  std::fstream FS("output-B", std::ios::out);
  if( FS.fail() ) return 1;


  int t;
  cin>>t;

  for(int o=0; o<t; o++) {

    int r,k,n,p;
    cin>>r>>k>>n;
    vector<int> vec;
    for(int i=0; i<n; i++) {
      cin>>p;
      vec.push_back(p);
    }

    long res = 0;
    int pos = 0,tmp=0;
    int count=0;
    for(int i=0; i<r; i++) {
      count = 0;
      while(true) {
	if( tmp > k || count == vec.size()+1 ) {
	  tmp -= vec[ (pos==0)?vec.size()-1:pos-1];
	  pos = (pos-1+vec.size())%vec.size();
	  break;
	}

	tmp += vec[pos++];
	pos %= vec.size();
	count++;
      }

      //cout<<i<<" "<<tmp<<" "<<pos<<endl;
      res += tmp;
      tmp = 0;

    }

    FS<<"Case #"<<o+1<<": "<<res<<endl;
    //cout<<res<<endl;
  }
}
