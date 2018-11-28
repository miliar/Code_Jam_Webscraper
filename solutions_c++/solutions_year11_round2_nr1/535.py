#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(){
  int T,tt=1;
  cin>>T;
  while(T--){
    int N;
    cin>>N;
    vector<string> V(N);
    string tmp;
    for (int i=0;i<N;i++){
      cin>>tmp;
      V[i]=tmp;
    }
    vector<double> score(N,0);
    vector<double> WP(N,0);
    vector<int> matches(N,0);
    vector<double> OWP(N,0);
    vector<int> OWPm(N,0);
    for (int i=0;i<N;i++){
      int w=0,l=0;
      for (int j=0;j<N;j++){
	if (V[i][j]=='1')
	  w++;
	if (V[i][j]=='0')
	  l++;
      }
      score[i]+=((0.25*w)/(w+l));
      WP[i] = score[i];
      matches[i]=w+l;
    }
    for (int i=0;i<N;i++){
      double sum=0;
      int is=0;
      for (int j=0;j<N;j++){
	if (V[i][j]!='.'){
	  if (matches[j]==1)
	    continue;
	  sum+=(4*WP[j]*matches[j]-('1'-V[i][j]))/(matches[j]-1);
	  is++;
	}
      }
      OWP[i]=(sum*0.5)/is;
      OWPm[i]=is;
      score[i]+=OWP[i];
    }
    for (int i=0;i<N;i++){
      double sum=0;
      int is=0;
      for (int j=0;j<N;j++){
	if (V[i][j]!='.'){
	  sum+=OWP[j];
	  is++;
	}
      }
      score[i]+=(sum*0.5)/is;
    }    
    cout<<"Case #"<<tt++<<":"<<endl;
    for (int i=0;i<N;i++){
      cout<<score[i]<<endl;
    }
  }
}
      

      
