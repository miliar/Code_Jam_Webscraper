#include<iostream>
#include<vector>
#include<map>

using namespace std;
int main(){
  int t;
  cin >> t;
  for(int i=0;i<t;++i){
	int n;
	cin >> n;
	vector<pair<char,int> > vp;
	vector<int> o,b;
	for(int k=0;k<n;++k){
	  char c; int m;
	  cin >> c >> m;
	  vp.push_back(make_pair(c,m));
	  if(c=='O') o.push_back(m);
	  else b.push_back(m);
	}
	vector<bool> comp(vp.size(),false);
	int cnt = 0, oo = 0, bb = 0, ox = 1, bx = 1;
	for(int k=0;k<vp.size();){

	  if(o.empty() || o[oo]==ox){
		//cout<<"O:ok ";
		if(vp[k].first=='O'){
		  oo++;
		  comp[k] = true;
		}
	  }else if(o[oo]>ox){
		//cout<<"O:++ ";
		ox++;
	  }else{
		//cout<<"O:--";
		ox--;
	  }

	  if(b.empty() || b[bb]==bx){
		//cout<<"B:ok "<<endl;
		if(vp[k].first=='B'){
		  bb++;
		  comp[k] = true;
		}
	  }else if(b[bb]>bx){
		//cout<<"B:++ "<<endl;
		bx++;
	  }else{
		//cout<<"B:--"<<endl;
		bx--;
	  }
	  
	  cnt++;
	  if(comp[k]) k++;
	}

	cout << "Case #" << i+1 << ": " << cnt << endl;
  }
  return 0;
}

