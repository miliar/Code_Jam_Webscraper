#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
vector<string> dp;
vector<string> v;

void process(){
	dp.push_back("0");
	v.push_back("0");
	for(int i=1;i<=1000;i++){
		string s;	// existing
		string s1;	// resultant
		s1 = dp[i-1];
		int carry = 0;
		int temp,rem;
		temp = 0;
		carry = 1;
		for(int i=0;i<s1.size();i++){
			temp = (s1.at(i) - 48) + carry;
			rem = temp%10;
			carry = temp/10;
			s1[i] = rem+48;
		}
		if(carry != 0)
			s1.push_back(carry+48);
		//cout<<"now s1 is "<<s1<<endl;
		string s2;
		for(int i=s1.size()-1;i>=0;i--)
			s2.push_back(s1[i]);
		//cout<<"s2 is "<<s2<<endl;
		v.push_back(s2);
		dp.push_back(s1);
	}
}

int main(void){
	process();
	int findPos;
	int cnt = 0;
	int t,A,B;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for(int k=1;k<=t;k++){
		scanf("%d %d",&A,&B);
		cnt = 0;
		string s,s1;
		for(int i=A;i<=B;i++){
			for(int j=i+1;j<=B;j++){
				s1 = v[j];
				s = s1.append(s1);
				findPos = s.find(v[i]);
				if(findPos != -1){
					//cntArr[i]++;
					//cout<<s<<"::"<<v[i]<<endl;
					//cout<<i<<"::"<<j<<endl;
					cnt++;
				}
			}
		}
		cout<<"Case #"<<k<<": "<<cnt<<endl;
	}
	return 0;
}