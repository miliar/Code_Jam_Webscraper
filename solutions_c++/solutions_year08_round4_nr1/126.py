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
		struct Node{
			bool canBeChanged;
			bool value;
			bool leaf;
			bool isAnd;
			vector<int> children;
		};
		void scanint(string &s, int& n){
			sscanf(s.c_str(),"%d",&n);
		}
vector<Node> vg;

int getvalue(bool isOr, bool resvalue, int l1, int l2, int r1, int r2){
	int res = 1e8;
	if(isOr){
		if(resvalue == false){
			if(l1>=0 && r1>=0){
				res = min(res,l1+r1);
			}
		} else {
			if(l1>=0 && r2>=0){
				res = min(res,l1+r2);
			}
			if(l2>=0 && r1>=0){
				res = min(res,l2+r1);
			}
			if(l2>=0 && r2>=0){
				res = min(res,l2+r2);
			}
		}
	} else {
		if(resvalue == false){
			if(l1>=0 && r1>=0){
				res = min(res,l1+r1);
			}
			if(l1>=0 && r2>=0){
				res = min(res,l1+r2);
			}
			if(l2>=0 && r1>=0){
				res = min(res,l2+r1);
			}
		} else {
			if(l2>=0 && r2>=0){
				res = min(res,l2+r2);
			}
		}
	}
	return res;
}
int dp[100000][2];
int go(int index, int value){
	Node n = vg[index];
	if(n.leaf == true){
		return n.value == value? 0 : -1;
	} else {
		int &res = dp[index][value];
		if(res!=-2)
			return res;
		res = 1e8;
		int l1,l2,r1,r2;
		vector<int> & vi = n.children;
		l1 = go(vi[0],0);
		l2 = go(vi[0],1);
		r1 = go(vi[1],0);
		r2 = go(vi[1],1);
		
		res = getvalue(!n.isAnd,value,l1,l2,r1,r2);
		if(n.canBeChanged)
			res = min(res,1+getvalue(n.isAnd,value,l1,l2,r1,r2));
		if(res >=1e8)
			res = -1;
		return res;	
	}

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
			for(int i=0;i<100000;++i)
				for(int j=0;j<2;++j)
					dp[i][j]=-2;
			int m, v;
			cin>>s;
			scanint(s,m);
			cin>>s;
			scanint(s,v);
			
			//interior
			vector<string> vs;
			for(int i=0;i<(m-1)/2;++i){
				cin>>s;
				string t;
				cin>>t;

				vs.push_back(s+" " +t);
			}
			
			//leaf
			vector<string> leafs;
			for(int i=0;i<(m+1)/2;++i){
				cin>>s;
				leafs.push_back(s);
			}
			
			vector<Node> vn;
			for(int i=0;i<vs.size();++i){
				int a,b;
				sscanf(vs[i].c_str(),"%d %d",&a,&b);
				Node t;
				t.canBeChanged = b;
				t.isAnd = a;
				t.leaf = false;
				t.value = false;
				vn.push_back(t);
			}
			for(int i=0;i<leafs.size();++i){
				int a;
				sscanf(leafs[i].c_str(),"%d",&a);
				Node t;
				t.canBeChanged = false;
				t.isAnd = a;
				t.leaf = true;
				t.value = a;
				vn.push_back(t);
			}
			for(int i=0;i<(m-1)/2;++i){
				vector<int> tmp;
				tmp.push_back(2*i+1);
				tmp.push_back(2*i+2);
				vn[i].children = tmp;
			}
			vg = vn;
			int res = go(0,v);
			if(res == -1)
				cout<<"IMPOSSIBLE";
			else
				cout<<res;
			cout<<endl;
		}
        } 
    // C:\Documents and Settings\Dmitry\My Documents\Visual Studio 2005\Projects\problem\problem\problem.cpp
