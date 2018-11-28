#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<map>
using namespace std;
int fn(string s){
	int i,l=s.length(),c=1;
	for(i=1;i<l;i++){
		if(s[i]!=s[i-1])	c++;
	}
	return c;
}
int main(){
	int k,s,i,j,l,n,t,mn,cs;
	string ss,sss;
	cin>>t;
	for(cs=1;cs<=t;cs++){
		cin>>k>>ss;
		l=ss.length();
		vector<int> v;
		for(i=0;i<k;i++){
			v.push_back(i);
		}
		mn=fn(ss);
		while(next_permutation(v.begin(),v.end())){
			sss=ss;
			for(i=0;i<l;i+=k){
				for(j=0;j<k;j++){
					sss[i+j]=ss[i+v[j]];
				}
			}
			n=fn(sss);
			if(n<mn)	mn=n;
		}
		printf("Case #%d: %d\n",cs,mn);
	}
	return 0;
}

