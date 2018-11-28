#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int tc = 1; tc <= t; tc++){
    int n;
    cin >> n;
    vector<string> tab;
    for(int i=0; i<n; i++){
      string tmp; cin >> tmp;
      tab.push_back(tmp);
    }
    vector< pair<int,int> > wp(n,make_pair(0,0));
    vector< double > wpv(n,0.0);
    vector< double >  owp(n,0.0);
    vector<double> oowp(n,0.0);
    for(int i=0; i<n; i++){
      int al = 0;
      int w = 0;
      for(int j=0; j<n; j++){
	if(tab[i][j] == '.')continue;
	al += 1;
	if(tab[i][j] == '1')w += 1;
      }
      wp[i] = make_pair(w,al);
      if(al != 0)wpv[i] = (double)w/(double)al;
    }
    for(int i=0; i<n; i++){
      double sum = 0.0;
      double num = 0.0;
      for(int j=0; j<n; j++){
	if(i == j)continue;
	if(tab[j][i] == '.')continue;
	num += 1.0;
	if(tab[j][i] == '1'){
	  int al = wp[j].second;
	  int w = wp[j].first;
	  if(al <= 1){
	    sum += 0.0;
	  }else {
	    sum += ( (double)(w-1)/(double)(al - 1) );
	  }
	}
	if(tab[j][i] == '0'){
	  int al = wp[j].second;
	  int w = wp[j].first;
	  if(al <= 1){
	    sum += 0.0;
	  }else {
	    sum += ( (double)(w)/(double)(al - 1) );
	  }
	}
      }
      owp[i] = sum/num;
    }
    for(int i=0; i<n; i++){
      double sum = 0.0;
      double num = 0.0;
      for(int j=0; j<n; j++){
	if(i == j)continue;
	if(tab[i][j] == '.')continue;
	sum += owp[j];
	num += 1.0;
      }
      oowp[i] = sum/num;
    }
    printf("Case #%d: \n",tc);
    for(int i=0; i<n; i++){
      printf("%.12lf\n",0.25*wpv[i]+0.5*owp[i]+0.25*oowp[i]);
    }
    
  }
  return 0;
}
