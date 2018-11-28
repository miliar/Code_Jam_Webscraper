#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm> 
#include <utility>
#include <stack>
#include <queue> 
#include <cmath>
#include <map>
#include <sstream>
#include <functional>
#include <numeric>

#define mp make_pair
#define pb push_back

using namespace std;

long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }
template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}

int main(int argc, char *argv[]){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++){
    	printf("Case #%d: ", tt);
    	vector<string>v;
    	for(int i=0; i<4; i++){
    		string a;
    		cin>>a;
    		v.pb(a);
    	}
    	bool x = 0;
    	for(int i=0; i<v.size(); i++){
    		int c = 0;
    		for(int j=0; j<v[i].size(); j++){
    			if(v[i][j]=='X'||v[i][j]=='T')
    				c++;
    		}
    		if(c==4){
    			x = 1;
    			break;
    		}
    	}
    	for(int i=0; i<4; i++){
    		int c = 0;
    		for(int j=0; j<4; j++){
    			if(v[j][i]=='X'||v[j][i]=='T')
    				c++;
    		}
    		if(c==4){
    			x = 1;
    			break;
    		}
    	}
    	int c = 0;
    	for(int i=0; i<v.size(); i++)
    		if(v[i][i]=='X'||v[i][i]=='T')
    			c++;
    	if(c==4)
    		x = 1;
    	c = 0;
    	for(int i=0; i<v.size(); i++)
    		if(v[i][3-i]=='X'||v[i][3-i]=='T')
    			c++;
    	if(c==4)
    		x = 1;

    	bool o = 0;
    	for(int i=0; i<v.size(); i++){
    		int c = 0;
    		for(int j=0; j<v[i].size(); j++){
    			if(v[i][j]=='O'||v[i][j]=='T')
    				c++;
    		}
    		if(c==4){
    			o = 1;
    			break;
    		}
    	}
    	for(int i=0; i<4; i++){
    		int c = 0;
    		for(int j=0; j<4; j++){
    			if(v[j][i]=='O'||v[j][i]=='T')
    				c++;
    		}
    		if(c==4){
    			o = 1;
    			break;
    		}
    	}
    	c = 0;
    	for(int i=0; i<v.size(); i++)
    		if(v[i][i]=='O'||v[i][i]=='T')
    			c++;
    	if(c==4)
    		o = 1;
    	c = 0;
    	for(int i=0; i<v.size(); i++)
    		if(v[i][3-i]=='O'||v[i][3-i]=='T')
    			c++;
    	if(c==4)
    		o = 1;
    	if(x)
    		printf("X won\n");
    	else if(o)
    		printf("O won\n");
    	else{
    		bool ok = 1;
    		for(int i=0; i<v.size(); i++)
    			for(int j=0; j<v[0].size(); j++)
    				if(v[i][j]=='.'){
    					ok = 0;
    					i=v.size();
    					break;
    				}
    		if(ok)
    			printf("Draw\n");
    		else printf("Game has not completed\n");
    	}
    }
    return 0;
}