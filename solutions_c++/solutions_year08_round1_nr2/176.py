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
         

    // BEGIN CUT HERE 
	long long getv(vector<int> &v1, vector<int> &v2){
		long long res = 0;
		for(int i=0;i<v1.size();++i)
			res+=(long long)v1[i]*v2[i];
		return res;
	}
	int f(vector<pair<int,bool> > &v1,vector<pair<int,bool> > &v2){
		return v1.size()<v2.size();
	}
    int main()
        {
			freopen("f:\\input.in", "r", stdin);
			freopen("f:\\output.txt", "w+", stdout);
		string s;
		cin>>s;
		int n;
		sscanf(s.c_str(),"%d",&n);
		vector<int> v1, v2;
		for(int it=0;it<n;++it){
			cout << "Case #" << (it+1)<<": ";
			cin>>s;
			int fl;
			sscanf(s.c_str(),"%d",&fl);
			int sk;
			cin>>s;
			sscanf(s.c_str(),"%d",&sk);
			
			vector<vector<pair<int,bool> > > vp;
			vp.resize(sk);
			for(int i=0;i<vp.size();++i){
				cin>>s;
				int tmp;
				sscanf(s.c_str(),"%d",&tmp);
				vector<pair<int,bool> > &vv=vp[i];
				vv.resize(tmp);
				for(int j=0;j<tmp;++j){
					cin>>s;
					sscanf(s.c_str(),"%d",&vv[j].first);
					cin>>s;
					sscanf(s.c_str(),"%d",&vv[j].second);
				}
			}
			vector<int> res(fl,0);

			bool sggood = true;
			while(true){
				sort(vp.begin(),vp.end(),f);
				bool glgood = true;
				bool glimp = false;
				for(int i=0;i<vp.size();++i){
					vector<pair<int,bool> > &v = vp[i];
					bool good = false; //1 - good, 2 - need to fix 1, 3 - need to fix 0 - impossible
					int ind1tof = -1;
					for(int j=0;j<v.size();++j){
						bool r1 = v[j].second;
						bool r2 = res[v[j].first-1];
						if(r2==r1){
							good = true;
							continue;
						} else if(r2==0){
							ind1tof = v[j].first-1;
						}
					}
					if(!good){
						if(ind1tof >= 0){
							res[ind1tof]=1;
							glgood = false;
							break;
						} else {
							glimp = true;
							break;
						}
					}
				}
				if(glimp){
					sggood = false;
					break;
				}
				if(glgood)
					break;
			}
			if(!sggood)
				cout<<"IMPOSSIBLE";
			else
				for(int i=0;i<res.size();++i)
					cout<<res[i]<<" ";
			cout<<endl;
		}
        } 
    // C:\Documents and Settings\Dmitry\My Documents\Visual Studio 2005\Projects\problem\problem\problem.cpp
