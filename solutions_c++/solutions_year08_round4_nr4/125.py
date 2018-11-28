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



    int main()
        {
			freopen("f:\\input.in", "r", stdin);
			freopen("f:\\output.txt", "w+", stdout);
		string s;
		cin>>s;
		int n;
		sscanf(s.c_str(),"%d",&n);

		for(int it=0;it<n;++it){
			cout << "Case #" << (it+1)<<": ";
			int res;
			int k;
			cin>>s;
			scanint(s,k);
			string g;
			cin>>s;
			g = s;
			vector<int> vi;
			for(int i=0;i<k;++i)
				vi.push_back(i);
			int minv = g.size();
			do{
				string s2;
				for(int i=0;i<g.size();++i){
					int ind = i%k;
					int u = i/k;
					s2+=g[u*k+vi[ind]];
				}
				int changes = 0;
				int c = 'A';
				for(int i=0;i<s2.size();++i){
					if(c!=s2[i]){
						changes++;
					}
					c=s2[i];
				}
				minv = min(minv,changes);

			} while(next_permutation(vi.begin(),vi.end()));
			res = minv;
			cout<<res;
			cout<<endl;
		}
        } 
    // C:\Documents and Settings\Dmitry\My Documents\Visual Studio 2005\Projects\problem\problem\problem.cpp
