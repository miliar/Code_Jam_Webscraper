// BEGIN CUT HERE
#include "stdafx.h"
// END CUT HERE
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>

using namespace std; 


vector<string> parse(string input, string search = " ",bool write_empty = false){
  vector<string> result;
  if (search.size() == 0){
    result.push_back(input);
    return result;
  }
  string temp = "";
  for(int i =0; i<input.length(); ++i){
    if(find(search.begin(),search.end(),input[i])!=search.end()){
      if (temp.size()!=0 || write_empty)
        result.push_back(temp);
      temp = "";
    } else {
      temp+=input[i];
    }
  }
  if(temp!="")
  result.push_back(temp);
  return result;
} 
#define sz 2001
 		int mod1 = 1000;
		int mod2 = 1000000;        

		void scanint(string &s, int& n){
			sscanf(s.c_str(),"%d",&n);
		}

set<pair<int,int> > bads;
int modulo = 10007;
int w,h;
int dp[124][124];
int go(int i, int j){
	if(i==0 && j==0)
		return 1;
	if(i<0 || j<0)
		return 0;
	int & res = dp[i][j];
	if(res>=0)
		return res;
	if(bads.count(make_pair(i,j))){
		return 0;
	}
	res = 0;
	res += go(i-2,j-1)%modulo;
	res += go(i-1,j-2)%modulo;
	return res;
}
    int main()
    {
			freopen("f:\\input.in", "r", stdin);
			freopen("f:\\output.txt", "w+", stdout);
		string s;
		cin>>s;
		int nn;
		sscanf(s.c_str(),"%d",&nn);


       for(int it=0;it<nn;++it)
       {

		   int r;
			cin>>w;
			cin>>h;
			cin>>r;
			memset(dp,-1,sizeof(dp));
			bads.clear();
			for(int i=0;i<r;++i){
				int t1,t2;
				cin>>t1;
				cin>>t2;
				bads.insert(make_pair(t1-1,t2-1));
			}
			int res = go(w-1,h-1)%modulo;
			cout<<"Case #"<<it+1<<": ";
			cout<<res;
			cout<<endl;
	   } 
	}
    // C:\Documents and Settings\Dmitry\My Documents\Visual Studio 2005\Projects\problem\problem\problem.cpp
