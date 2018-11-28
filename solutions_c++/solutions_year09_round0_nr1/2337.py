#include <iostream>

using namespace std;


char words[5010][16];

int main() {
  int L,D,N;
  cin>>L;
  cin>>D;
  cin>>N;

  for(int i=0;i<D;i++) {
    cin>>words[i];
  }
  
  for(int i=0;i<N;i++) {

    bool table[16][28];
    
    for(int j=0;j<16;j++) {
      for(int k=0;k<28;k++) {
	table[j][k]=false;
      }
    }

    for(int tokens=0;tokens<L;tokens++) {
      char temp;
      cin>>temp;
      if(temp!='(') {
	table[tokens][temp-'a']=true;
      }
      else {
	cin>>temp;
	while(temp!=')') {
	  table[tokens][temp-'a']=true;
	  cin>>temp;
	}
      }
    }
    
    int answer=0;
    for(int wi=0;wi<D;wi++) {
      int tokens;
      for(tokens=0;tokens<L;tokens++) {
	if(table[tokens][words[wi][tokens]-'a']==false) {
	  break;
	}
      }
      if(tokens==L) {
	answer++;
      }
    }
    cout<<"Case #"<<(i+1)<<": "<<answer<<endl;
  }
  return 0;
}

  
