#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<cassert>
#include<climits>
using namespace std;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vb> vvb;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef pair<int,int> ii;
typedef pair<int,ii> pii;
typedef long long LL;
#define sz(c) (int)c.size()
#define pb push_back
#define all(v) v.begin(),v.end()
#define inc(i,n) for(int i=0;i<n;i++)
#define dec(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,a,n) for(int i=a;i<n;i++)
#define INF 100000000
#define F first
#define S second
int main(){

	int T;
	cin>>T;
	for(int g=1;g<=T;g++){
		vector<vector<char> > combine(26,vector<char>(26,0));
		int N1;
		cin>>N1;
		inc(i,N1){
			string x;
			cin>>x;
			combine[x[0]-'A'][x[1]-'A']= x[2];
			combine[x[1]-'A'][x[0]-'A']= x[2];
		}
		map<pair<char,char> ,int > opposed;
		int N2;
		cin>>N2;
		inc(i,N2){
			string x;
			cin>>x;
			pair<char,char> p(x[0],x[1]);
			opposed[p]=1;
			swap(p.F,p.S);
			opposed[p]=1;
		}
		int len;
		cin>>len;
		string input;
		cin>>input;
		string output;
		output.pb(input[0]);
		for(int i=1;i<len;i++)
		{
			char pre = 0;
			if(sz(output))
				pre = output[sz(output)-1];
			if(pre){
				char ch = combine[input[i]-'A'][pre-'A'];
				bool flag=0;
				if(ch){
					output[sz(output)-1]=ch;
					flag = 1;
				}
				else{
					inc(j,sz(output)){
						if(opposed.find(make_pair(output[j],input[i]))!=opposed.end()){
							output.clear();
							flag = 1;
							break;
						}
					}
				}
				if(!flag)
					output.pb(input[i]);
			
			}
			else
				output.pb(input[i]);
		}
		printf("Case #%d: [",g);
		inc(i,sz(output)-1)
			printf("%c, ",output[i]);
		if(sz(output))
			printf("%c",output[sz(output)-1]);
		puts("]");
	}
return EXIT_SUCCESS;

}
