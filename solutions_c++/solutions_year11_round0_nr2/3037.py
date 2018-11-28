#include<iostream>
#include<vector>

using namespace std;
int main(){
  int t;
  cin >> t;
  for(int i=0;i<t;++i){
	int n;
	vector<string> comb;
	vector<string> opp;
	cin>>n;
	for(int k=0;k<n;++k){
	  string tmp; cin>>tmp;
	  comb.push_back(tmp);
	}
	cin>>n;
	for(int k=0;k<n;++k){
	  string tmp; cin>>tmp;
	  opp.push_back(tmp);
	}
	cin>>n;
	string input;
	cin>>input;

	string list;
	list += input[0];
	input = input.substr(1);

	while(!input.empty()){
	  char c = list[list.length()-1];
	  string co1,co2;
	  co1 += c; co1 += input[0];
	  co2 += input[0]; co2 += c;
	  //cout << co1 << co2 << endl;
	  bool cf=false;
	  for(int j=0;j<comb.size();++j){
		if(comb[j].substr(0,2)==co1 or comb[j].substr(0,2)==co2){
		  list[list.length()-1] = comb[j][2];
		  cf = true; break;
		}
	  }
	  bool opf = false;
	  if(!cf){
		for(int j=0;j<opp.size();++j){
		  if(input[0]==opp[j][0] and list.find(opp[j][1])!=string::npos){
			list = "";
			opf = true; break;
		  }
		  if(input[0]==opp[j][1] and list.find(opp[j][0])!=string::npos){
			list = "";
			opf = true; break;
		  }
		}
	  }
	  if(!cf and !opf) list += input[0];
	  input = input.substr(1);	 
	}
	
	cout << "Case #" << i+1 << ": [";
	for(int j=0;j<list.size();++j){
	  cout << list[j] << (j==list.size()-1?"":", ");
	}
	cout << "]" << endl;
  }
  return 0;
}

