#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;
#define MP make_pair
vector <pair<int,int> > vp;
//event 5 starts from station a,6 starts from station b, 3 add one to station a,4 add one to station b
int mystoi(string s)
{ 
  istringstream is(s);
  int ret;
  is>>ret;
  return ret;
}

int main(){
	int t, na, nb, tt, res,resa,resb;
	int ca,cb;
	string st,su;
	cin>>t;
	for(int tc=1;tc<=t;tc++){
		cin>>tt;
		cin>>na>>nb;
		vp.clear();
		for(int i=0;i<na;i++){
			cin>>st>>su;
			res = mystoi(st.substr(0,2)+st.substr(3,2));
			vp.push_back(MP(res,5));
			res = mystoi(su.substr(0,2)+su.substr(3,2));
			vp.push_back(MP(res+tt,4));
		}
		for(int i=0;i<nb;i++){
			cin>>st>>su;
			res = mystoi(st.substr(0,2)+st.substr(3,2));
			vp.push_back(MP(res,6));
			res = mystoi(su.substr(0,2)+su.substr(3,2));
			vp.push_back(MP(res+tt,3));
		}
		res=0;ca=cb=0;resa=resb=0;
		sort(vp.begin(),vp.end());
		for(int i=0;i<vp.size();i++){
			if(vp[i].second==3) ca++;
			else if(vp[i].second==4) cb++;
			else if(vp[i].second==5){
				if(ca>0){ca--;}
				else resa++;
			}
			else {
				if(cb>0){cb--;}
				else resb++;
			}
		}
		cout<<"Case #"<<tc<<": "<<resa<<" "<<resb<<endl;
	}
	return 0;
}