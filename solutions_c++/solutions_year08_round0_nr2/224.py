#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	int N,NA,NB;
	cin>>N;
	vector<int> sa;
	vector<int> ea;
	vector<int> sb;
	vector<int> eb;
	ofstream fp("B-large.out");
	int a,b,T;
	char ch;
	for(int i = 1; i <= N; i++) {
		cin>>T>>NA>>NB;
		sa.resize(NA);
		ea.resize(NA);
		sb.resize(NB);
		eb.resize(NB);
		//cout<<T<<" "<<NA<<" "<<NB<<endl;
		for(int j = 0; j < NA; j++) {
			cin>>a>>ch>>b;
			sa[j] = a * 60 + b;
			//cout<<a<<" "<<b<<"->";
			cin>>a>>ch>>b;
			ea[j] = a * 60 + b + T;
			//cout<<a<<" "<<b<<endl;
		}
		for(int j = 0; j < NB; j++) {
			cin>>a>>ch>>b;
			sb[j] = a * 60 + b;
			//cout<<a<<" "<<b<<"->";
			cin>>a>>ch>>b;
			eb[j] = a * 60 + b + T;
			//cout<<a<<" "<<b<<endl;
		}
		sort(sa.begin(),sa.end());
		sort(ea.begin(),ea.end());
		sort(sb.begin(),sb.end());
		sort(eb.begin(),eb.end());
		int resA = NA;
		int resB = NB;
		int k = 0;
		for(int j = 0; j < NA; j++) {
			if(k < NB && sa[j] >= eb[k]) {
				resA --;
				k++;
			}
		}
		k = 0;
		for(int j = 0; j < NB; j++) {
			if(k < NA && sb[j] >= ea[k]) {
				resB --;
				k++;
			}
		}
		fp<<"Case #"<<i<<": "<<resA<<" "<<resB<<endl;
	}
	fp.close();
	return 0;
}