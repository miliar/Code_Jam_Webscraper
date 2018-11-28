#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>


using namespace std;

int n;
bool oppose[256][256];
char result[256][256];

template<class t>
ostream & operator << (ostream & tout,const vector<t> &s){
  tout<<'[';
  for (int i=0;i<s.size();i++)
    if (i+1 == s.size())
      tout<<s[i];
    else
      tout<<s[i]<<',';
  tout<<']';
  return(tout);
}


int main(){
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    for (int i=0;i<256;i++)
      for (int j=0;j<256;j++){
	oppose[i][j]=false;
	result[i][j]=0;
      }
    int x;
    cin>>x;
    for (int i=1;i<=x;i++){
      string temp;
      cin>>temp;
      result[temp[0]][temp[1]]=temp[2];
      result[temp[1]][temp[0]]=temp[2];
    }
    cin>>x;
    for (int i=1;i<=x;i++){
      string temp;
      cin>>temp;
      oppose[temp[0]][temp[1]]=true;
      oppose[temp[1]][temp[0]]=true;
    }

    int temp;
    cin>>temp;
    string st;
    cin>>st;
    vector<char> vc;
    for (int i=0;i<st.size();i++){
      vc.push_back(st[i]);
      bool bad=true;
      do{
	bad=false;
	if(vc.size() >= 2 && result[vc[vc.size()-1]][vc[vc.size()-2]]){
	  bad=true;
	  char temp=result[vc[vc.size()-1]][vc[vc.size()-2]];
	  vc.pop_back();
	  vc.pop_back();
	  vc.push_back(temp);
	}
      }while (bad);
//       cout<<i<<' '<<vc<<endl;
      for (int j=0;j+1<vc.size();j++)
	if (oppose[vc[vc.size()-1]][vc[j]])
	  vc.clear();
//       cout<<i<<' '<<vc<<endl;
    }
    cout<<"Case #"<<ccount<<": [";
    for (int i=0;i<vc.size();i++){
      cout<<vc[i];
      if (i+1 < vc.size())
	cout<<", ";
    }
    cout<<']'<<endl;
  }
}
