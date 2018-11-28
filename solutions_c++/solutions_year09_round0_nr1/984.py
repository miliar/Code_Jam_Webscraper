#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
using namespace std;


bool present[20][26];
string input[5001];


int main(){

  int L,D,N;

  cin>>L>>D>>N;

  char c;
  int index ;

  for(int i=0; i<D; i++)
    cin>>input[i];

  for(int i=0; i<N; i++){

    memset(present,0,sizeof(present));
    index = 0;
    bool flag = false;

    while(index<L){
      cin>>c;

      if(c=='('){
	flag = true;
      }
      else if(c==')'){
	flag = false;
	index++;
      }
      else{
        present[index][(int)c-(int)'a'] = true;
	if(!flag)
	  index++;
      }
    }

    //for(int 

    int ans = 0;

    for(int k=0; k<D; k++){
      int j;
      for( j=0; j<L; j++){
	if(!present[j][(int)input[k][j]-(int)'a'])
	  break;
      }
      if(j==L)
	ans++;
    }

    cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }

  return 0;
}
    

