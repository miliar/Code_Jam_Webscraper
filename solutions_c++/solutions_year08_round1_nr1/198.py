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
 char ss[10000];
         

    // BEGIN CUT HERE 
	long long getv(vector<int> &v1, vector<int> &v2){
		long long res = 0;
		for(int i=0;i<v1.size();++i)
			res+=(long long)v1[i]*v2[i];
		return res;
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
			int m;
			sscanf(s.c_str(),"%d",&m);
			v1.resize(m);
			v2.resize(m);
			for(int i=0;i<m;++i){
				cin>>s;
				sscanf(s.c_str(),"%d",&v1[i]);
			}
			for(int i=0;i<m;++i){
				cin>>s;
				sscanf(s.c_str(),"%d",&v2[i]);
			}

			//small input
			long long minv = getv(v1,v2);


			/*sort(v2.begin(),v2.end());
			do {
				minv = min(minv, getv(v1,v2));
			} while(next_permutation(v2.begin(),v2.end()));*/

			//large input

			vector<int> lz1,lz2,mz1,mz2;
			int z1, z2;
			z1 = z2 = 0;
			for(int i=0;i<v1.size();++i){
				if(v1[i]==0)
					z1++;
				else if(v1[i]<0)
					lz1.push_back(v1[i]);
				else
					mz1.push_back(v1[i]);
					
			}
			for(int i=0;i<v2.size();++i){
				if(v2[i]==0)
					z2++;
				else if(v2[i]<0)
					lz2.push_back(v2[i]);
				else
					mz2.push_back(v2[i]);
					
			}
			minv = 0;
			vector<int> rem1,rem2;
			sort(lz1.begin(),lz1.end());
			sort(mz1.begin(),mz1.end());
			sort(lz2.begin(),lz2.end());
			sort(mz2.begin(),mz2.end());
			reverse(mz1.begin(),mz1.end());
			reverse(mz2.begin(),mz2.end());
			for(int i=0;i<min(lz1.size(),mz2.size());++i){
				minv+=(long long)lz1[i]*mz2[i];
			}
			for(int i=min(lz1.size(),mz2.size());i<max(lz1.size(),mz2.size());++i){
				if(i<lz1.size())
					rem1.push_back(abs(lz1[i]));
				else
					rem2.push_back(mz2[i]);
			}
			for(int i=0;i<min(lz2.size(),mz1.size());++i){
				minv+=(long long)lz2[i]*mz1[i];
			}
			for(int i=min(lz2.size(),mz1.size());i<max(lz2.size(),mz1.size());++i){
				if(i<lz2.size())
					rem2.push_back(abs(lz2[i]));
				else
					rem1.push_back(mz1[i]);
			}
			int p = rem1.size()-z2;
			sort(rem1.begin(),rem1.end());
			sort(rem2.begin(),rem2.end());
			//reverse(rem2.begin(),rem2.end());
			for(int i=0;i<p;++i)
				minv+=(long long)rem1[i]*rem2[rem2.size()-z1-i-1];
			cout<<minv;
			cout<<endl;
		}
        } 
    // C:\Documents and Settings\Dmitry\My Documents\Visual Studio 2005\Projects\problem\problem\problem.cpp
