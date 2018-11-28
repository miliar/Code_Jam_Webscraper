#include<vector>
#include<algorithm>
#include<iostream>
#include<map>
#include<numeric>
#include<functional>
#include<utility>
using namespace std;
void invoke(int cases);
int main() {
	int t;
	cin>>t;
	for(int i=1; i<=t; i++) {
		invoke(i);
	}
}
bool operator<(const pair<char,char>& p1, const pair<char,char>&p2) {
	if(p1.first == p2.first) {
		return p1.second < p2.second;
	}
	return p1.first < p2.first;
}

void invoke(int cases) {
	int c,d,n;
	multimap<char,char> comb;
	map<pair<char,char>,char> combr;
	map<pair<char,char>,char> opp;
	vector<char> v;
	cin>>c;
	
	for(int i=0;i<c;i++) {
		char ch1,ch2,ch3;
		cin>>ch1>>ch2>>ch3;
		pair<char, char>p12(min(ch1,ch2),max(ch1,ch2));
		//multimap.insert(p12);
		combr.insert(make_pair(p12,ch3));
	}
	cin>>d;
	for(int i=0;i<d;i++) {
		char ch1, ch2;
		cin>>ch1>>ch2;
		pair<char, char>p12(min(ch1,ch2),max(ch1,ch2));
		opp.insert(make_pair(p12,'a'));
	}
	cin>>n;
	for(int i=0;i<n;i++) {
		char ch;
		cin>>ch;
		v.push_back(ch);
	}
	vector<char> re;
	re.push_back(v[0]);
	//process
	map<pair<char,char>,char >::iterator cit;
	for(int i =1; i<n;i++) {
		char cur = v[i];
		//check for comb
		char tail = re[re.size()-1];
		pair<char,char> cp(min(cur,tail),max(cur,tail));
		cit = combr.find(cp);
		if(cit!=combr.end()) {
			//we can combine
			re.pop_back();
			re.push_back(cit->second);
		} else {
			re.push_back(cur);
		}
		//check for opp
		//use the last element to check
		int size = re.size(); 
		tail = re[size-1];
		for(int i=0;i<size-1;i++) {
			pair<char,char> op(min(re[i],tail),max(re[i],tail));
			cit = opp.find(op);
			if(cit!=opp.end()) {
				//opp found, clear
				re.clear();
				break;
			}
		}
	}
	cout<<"Case #"<<cases<<": [";
	int size =re.size();
	for(int i=0;i<size-1;i++) {
		cout<<re[i]<<", ";
	}
	if(size>0) {
	cout<<re[size-1]<<"]"<<endl;
	}else {
		cout<<"]"<<endl;
	}
}
