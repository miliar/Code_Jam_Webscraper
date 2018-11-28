#include<string>
#include<iostream>
#include<vector>

using namespace std;

char buf[2000];

int main(){
  vector<string> SE;
  int N;
  cin>>N;
  int n=0;
  while(n++<N){
    int S,Q;
    cin>>S;
    cin.getline(buf,2000);
    SE.resize(S);
    for (int i=0;i<S;i++){
      cin.getline(buf,2000);
      SE[i] = string(buf);
    }
    cin>>Q;
    cin.getline(buf,2000);
    vector<int> tag(SE.size(),0);
    int total=0;
    int chosen=0;
    int last = 0;
    string tmp;
    for (int i=0;i<Q;i++){
      cin.getline(buf,2000);
      tmp = string(buf);
      for (int j=0;j<S;j++){
	if (SE[j]==tmp){
	  if (tag[j]==0){
	    tag[j]=1;
	    chosen++;
	    last = j;
	  }
	}
      }
      if (chosen == S){
	total++;
	chosen = 1;
	for (int j=0;j<S;j++){
	  if (last==j) continue;
	  tag[j]=0;
	}
      }
    }
    cout<<"Case #"<<n<<": "<<total<<endl;
  }
}
