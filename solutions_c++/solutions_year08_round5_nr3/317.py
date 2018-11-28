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

vector<int> masks;
int n, m;

bool isGood(int nowMask, int mmask){
	for(int j=1;j<m;++j){
		if((nowMask&(1<<(j-1)))&&(nowMask&(1<<j)))
			return false;
	}
	for(int j=0;j<m;++j)
		if(nowMask&(1<<j)&&(mmask&(1<<j)))
			return false;
	return true;
}
int countBits(int mask){
	int res =0;
	for(int j=0;j<m;++j)
		res+=(mask&(1<<j))>0;
	return res;
}
int getNewmask(int mask){
	int newmask = 0;
	for(int j=0;j<m;++j){
		if(mask&(1<<j)){
			if(j>0)
			newmask|=1<<(j-1);
			if(j<m-1)
			newmask|=1<<(j+1);
		}
	}
	return newmask;
}
int dp[16][2048];
int go(int index, int curmask){
	if(index == n)
		return 0;
	int nmask = masks[index];
	int resmask = nmask|curmask;

	int k = 1<<m;
	int &res = dp[index][curmask];
	if(res>=0)
		return res;
	res = 0;
	for(int i=0;i<k;++i){
		int c = 0;
		bool good = isGood(i,resmask);
		int bits = countBits(i);
		int newmask = getNewmask(i);
		if(good){
			res = max(res,bits+go(index+1,newmask));
		}
	}
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

			cin>>n;
			cin>>m;

			masks.clear();
			masks.resize(n);
			for(int i=0;i<n;++i){
				int mask = 0;
				for(int j=0;j<m;++j){
					char t;
					cin>>t;
					if(t!='.')
						mask+=1<<j;

				}
				masks[i]=mask;
			}
			reverse(masks.begin(),masks.end());
			memset(dp,-1,sizeof(dp));
			int res = go(0,0);
			cout<<"Case #"<<it+1<<": ";
			cout<<res;
			cout<<endl;
	   } 
	}
    // C:\Documents and Settings\Dmitry\My Documents\Visual Studio 2005\Projects\problem\problem\problem.cpp
