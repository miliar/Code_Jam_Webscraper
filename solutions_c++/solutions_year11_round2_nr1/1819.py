//Run file as cat input.in | ./a.out >out.txt

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main()
{
  int T,i,j,swap,k,min, minindex,N;
  double  temp;
  string s;
  vector<double> w;
  vector<double> ow;
  vector<double> oow;
  vector<double> rpi;
  vector< vector<int> > g;
  vector<int> games;
  cin >> T;
  for(i=0;i<T;i++){    
    cout << "Case #" <<i+1 <<":"<< endl;
    cin >> N;
   g.resize(N);
    for(j=0;j<N;j++){
      cin >>s;  
      w.push_back(0);
      games.push_back(0);
      for(k=0;k<N;k++){
	if(s[k] != '.'){
	  games[j] = games[j]+1;	  
	  g[j].push_back(1);
	  if(s[k]=='1'){
	  w[j] = w[j]+1.0;
	  g[j][k]=2;
	  }
	}
	else{
	  g[j].push_back(0);
	}
      }
      w[j] = w[j]/games[j];     
    }
    for(j=0;j<N;j++){
      ow.push_back(0);
      for(k=0;k<N;k++){
	if(g[j][k]>0){
	  temp=0;
	  if(g[j][k]==1){
	    temp = 1.0;
	  }
	  temp = (w[k]*games[k]-temp)/(games[k]-1);
	  ow[j] = ow[j]+temp;
	}
      }
      ow[j] = ow[j]/games[j]; 
    }    
    for(j=0;j<N;j++){
      oow.push_back(0);
      for(k=0;k<N;k++){
	if(g[j][k]>0){
	  oow[j] = oow[j]+ow[k];
	}
      }
      oow[j] = oow[j]/games[j];  
      temp = 0.25*w[j]+0.5*ow[j]+0.25*oow[j];
      rpi.push_back(temp);
      cout << rpi[j]<< endl;
    }
     w.clear();
     ow.clear();
     oow.clear();
     rpi.clear();
     games.clear();
     s.clear();
     for(j=0;j<N;j++){
       g[j].clear();
     }
     g.clear();
  }



return 0;
}