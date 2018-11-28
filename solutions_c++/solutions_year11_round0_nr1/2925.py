#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
vector<pair<int, int> > orange;
vector<pair<int, int> > blue;
int getseconds();
int main() {
	int t, n;
	char col;
	int num;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cin>>n;
		for(int j=1;j<=n;j++) {
			cin>>col;
			cin>>num;
			if(col=='O'){
				orange.push_back(make_pair (num, j));
			}
			else {
				blue.push_back(make_pair (num, j));
			}
		}
		cout<<"Case #"<<i<<": "<<getseconds()<<endl;
	}
}

int getseconds() {
	int t=0;
	int bcur = 1;
	int ocur = 1;
	bool flag = false;
	while(!orange.empty() && !blue.empty()) {
		t++;
		flag = false;
		if((orange.front()).first > ocur) {
			ocur++;
		}
		else if((orange.front()).first < ocur) {
			ocur--;
		}
		else {
			if((orange.front()).second < (blue.front()).second) {
				flag = true;
			}
		}
		if((blue.front()).first > bcur) {
			bcur++;
		}
		else if((blue.front()).first < bcur) {
			bcur--;
		}		
		else {
			if((blue.front()).second < (orange.front()).second) {
				blue.erase(blue.begin());
			}
		}
		if(flag) {
			orange.erase(orange.begin());
		}
	}
	while(!orange.empty()){
		t++;
		if((orange.front()).first > ocur) {
			ocur++;
		}
		else if((orange.front()).first < ocur) {
			ocur--;
		}
		else {
			orange.erase(orange.begin());
		}
	}
	while(!blue.empty()){
		t++;
		if((blue.front()).first > bcur) {
			bcur++;
		}
		else if((blue.front()).first < bcur) {
			bcur--;
		}
		else {
			blue.erase(blue.begin());
		}
	}
	return t;
}

