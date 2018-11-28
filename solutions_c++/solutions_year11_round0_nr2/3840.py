/*
 * File:   tc.cpp
 * Author: Divij
 *
 * Created on 26 April, 2011, 8:30 PM
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cstring>

using namespace std;
void clear(map<char,int> &test){
    map<char,int> :: iterator it;

    for(it=test.begin();it!=test.end();it++){
	it->second=0;
    }
    return;
}
int main() {
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);

    for(int l=0;l<T;l++){
	map<char,char> opp;
	map<string,char> help;
	map<char,int> test;

	int C;
	scanf("%d",&C);
	for(int m=0;m<C;m++){
	    char a,b,c;
	    cin >> a >>b >> c;
	    string temp="";
	    temp.push_back(a);
	    temp.push_back(b);
	    help[temp]=c;
	    temp="";

	    temp="";
	    temp.push_back(b);
	    temp.push_back(a);
	    help[temp]=c;

	}
	int D;
	scanf("%d",&D);

	for(int i=0;i<D;i++){
	    char a,b;
	    cin >> a>> b;
	    opp[a]=b;
	    opp[b]=a;
	    if(test.count(a)!=0)test[a]++;
	    else test[a]=0;
	    if(test.count(b)!=0)test[b]++;
	    else test[b]=0;
	}

	int N;
	string inp;
	scanf("%d",&N);
	cin >> inp;

	stack <char> ans;
	for(int i=0;i<inp.size();i++){
	   // if(!ans.empty())cout << ans.top() << endl;
	    if(ans.empty()){
		ans.push(inp[i]);
		if(test.count(inp[i])!=0)test[inp[i]]++;
		else test[inp[i]]=1;
	    }else{
		string s="";
		s.push_back(inp[i]);
		s.push_back(ans.top());

		if(help.count(s)!=0){
		    //cout << "blah"<<endl;
		    test[ans.top()]--;
		    ans.pop();

		    ans.push(help[s]);
		}else{
		    if(opp.count(inp[i])!=0 && test[opp[inp[i]]]>0){
			//cout << "hh" << endl;
			    while(!ans.empty())ans.pop();
			    clear(test);			
		    }else{
			ans.push(inp[i]);
			if(test.count(inp[i])!=0)test[inp[i]]++;
			else test[inp[i]]=1;
		    }
		}
	    }
	}

	
	string aa="]";
	while(!ans.empty()){
	    if(aa!="]"){aa.push_back(' ');
		aa.push_back(',');
	    }
	    aa.push_back(ans.top());

	    ans.pop();
	    
	}
	aa.push_back('[');

	reverse(aa.begin(),aa.end());
	printf("Case #%d: ",l+1);
	cout << aa << "\n";
    }


    fclose(stdin);
    fclose(stdout);
    return 0;
}

