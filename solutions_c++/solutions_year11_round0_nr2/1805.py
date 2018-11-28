/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define PB push_back
typedef pair<char,char> PI;
#define f first
#define s second

const char baseElem[8]={'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

PI getPair(char c,char d){
	if(c>d)	swap(c,d);
	return PI(c,d);
}

int main(){
	int t;
	cin>>t;
	FF(kase,1,t+1){
		cout<<"Case #"<<kase<<": ";
		int c,d,n;
		cin>>c;
		map< PI , char > combine;
		while(c--){
			string s;
			cin>>s;
			if(s[1]<s[0])	swap(s[0],s[1]);
			PI p = PI(s[0],s[1]);
			combine[p]=s[2];
		}
		set< PI > opposed;
		cin>>d;
		while(d--){
			string s;
			cin>>s;
			PI p;
			p.f=s[0];
			p.s=s[1];
			if(p.s<p.f)	swap(p.f,p.s);
			opposed.insert(p);
		}
		cin>>n;
		string inp;
		cin>>inp;
		vector<char> out;
		map<char,int> inList;
		F(i,n){
			char c=inp[i];
			bool ok=true;
			if(out.size()){
				if(combine.find(getPair(out.back(),c))!=combine.end()){
					inList[out.back()]--;
					out.back() = combine[getPair(out.back(),c)];
					inList[out.back()]++;
					ok=false;
				}
				else{
					F(j,8){
						char d=baseElem[j];
						if(inList[d]>0 && opposed.find(getPair(c,d))!=opposed.end()){
							inList.clear();
							out.clear();
							ok=false;
							break;
						}
					}
				}
			}
			if(ok){
				inList[c]++;
				out.PB(c);
			}
		}
		cout<<"[";
		if(out.size())	cout<<out[0];
		FF(i,1,out.size())	cout<<", "<<out[i];
		cout<<"]"<<endl;
	}
	return 0;
}
