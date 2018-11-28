#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;++t){
	int teams;
	cin>>teams;

	vector<string> w(teams);
	for(int i=0;i<teams;++i)
	  cin>>w[i];

	vector<double> p(teams);
	vector<double> wins(teams);
	vector<double> wp(teams);
	vector<double> owp(teams);
	vector<double> owps(teams);
	vector<double> oowp(teams);

	for(int team=0;team<teams;++team){
	  int won = 0;
	  int plays = 0;
	  for(int i=0;i<teams;++i){
		if(w[team][i] == '1'){
		  ++won;
		  ++plays;
		}
		if(w[team][i] == '0'){
		  ++plays;
		}

		p[team] = plays;
		wins[team] = won;
		if(plays)wp[team] = (double)won / (double)plays;
		else wp[team] = 0;
	  }
	}

	for(int team=0;team<teams;++team){
	  int plays = 0;
	  double sum = 0.0;
	  for(int i=0;i<teams;++i){
		if(w[team][i] == '0'){
		  ++plays;
		  if(p[i]>1)
		  sum += (wins[i]-1) / (p[i]-1);
		  //cout<<wins[i]<<" "<<p[i]<<endl;
		}
		if(w[team][i] == '1'){
		  ++plays;
		  if(p[i]>1)
		  sum += wins[i] / (p[i]-1);
		  //cout<<wins[i]<<" "<<p[i]<<endl;
		}

		//owps[team] = sum;

		if(plays)owp[team] = sum / plays;
		else owp[team] = 0;
	  }
	  owps[team] = sum;
	}

	for(int team=0;team<teams;++team){
	  int plays = 0;
	  double sum = 0.0;
	  for(int i=0;i<teams;++i){
		if(w[team][i] != '.'){
		  ++plays;
		  //cout<<(owps[i]-owp[team]) / (p[i]-1)<<endl;
		  //if(p[i]>1)
			sum += owp[i];////(owps[i]-owp[team]) / (p[i]-1);
		  //cout<<wins[i]<<" "<<p[i]<<endl;
		}

		if(plays)oowp[team] = sum / plays;
		else oowp[team] = 0;
	  }
	}
					   

	cout<<"Case #"<<t<<":"<<endl;
	for(int i=0;i<teams;++i){
	  
	  cout<<(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i])<<endl;
	}
  }
}
