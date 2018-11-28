#include<iostream>
#include<vector>
using namespace std;

int NN;
int seen[500][500];
long long M[500][500];
int id=1;

vector<long long> X,Y;

long long solve(int maskX,int maskY){
   if(maskX==0) return 0;
   long long &ret=M[maskX][maskY];
   if(seen[maskX][maskY]==id) return ret;
   ret=1e18;
   seen[maskX][maskY]=id;
   for(int i=0;i<NN;i++){
   	if((maskX&(1<<i))){
	   for(int j=0;j<NN;j++){
	      if(maskY&(1<<j)){
	         ret<?=solve(maskX^(1<<i),maskY^(1<<j))+(X[i]*Y[j]);
	      }
	   }
	}
   }
   return ret;
}


int main(){
  int n;
  cin>>n;
  for(int i=0;i<n;i++){
    X.clear();
    Y.clear();
    int N;
    cin>>N;
    NN=N;
    for(int j=0;j<N;j++) {
      int x;
      cin>>x;
      X.push_back(x);
    }
    for(int j=0;j<N;j++) {
    	int y;
	cin>>y;
	Y.push_back(y);
    }
    cout<<"Case #"<<id<<": "<<solve((1<<N)-1,(1<<N)-1)<<endl;
    id++;
  }
}