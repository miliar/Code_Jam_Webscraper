#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<queue>
#include<complex>
#include<numeric>
#include<bitset>

using namespace std;
typedef long long Int;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef pair<Int,Int> pint;

int zero(string s){
	if(s.length()==1 && s[0]=='0') return 1;
	return 0;
}

string mn(string a,string b){
	if(a.length()<b.length()) return a;
	if(a.length()>b.length()) return b;
	for(int i=a.length()-1;i>=0;i--){
		if(a[i]<b[i]) return a;
		if(a[i]>b[i]) return b;
	}
	return a;
}

string pl(string a,string b){
	int c=0;
	string ans;
	if(mn(a,b)==a) swap(a,b);
	int i;
	for(i=b.length();i<a.length();i++){
		b+='0';
	}
	for(i=0;i<a.length();i++){
		int t=(a[i]-'0')+(b[i]-'0')+c;
		ans+=('0'+t%10);
		c=t/10;
	}
	if(c!=0) ans+='1';
//	cout << "plus " << a << "	" << b << "	" << ans << endl;
	return ans;
}
	
string mi(string a,string b){
	if(mn(a,b)==a) swap(a,b);
	int c=0;
	string ans;
	int i;
	for(i=b.length();i<a.length();i++){
		b+='0';
	}
	for(i=0;i<a.length();i++){
		int t=(a[i]-'0')-(b[i]-'0')+c;
		if(t<0) t+=10,c=-1;
		else c=0;
		ans+=('0'+t);
	}
	ans+=('0'+c);
	for(i=ans.length()-1;i>=0&&ans[i]=='0';i--);
	if(i==-1) i=0;
	string ans2;
	for(int j=0;j<=i;j++)ans2+=ans[j];
//	cout << "minus " << a << "	" << b << "	" << ans2 << endl;
	return ans2;
}

string jouyo(string a,string b){
	string tmp[200];
	tmp[0]=b;
//	cout << a << "	" << b << "	";
	for(int i=1;i<200;i++){
		tmp[i]=pl(tmp[i-1],tmp[i-1]);
	}
	for(int i=199;i>=0;i--){
		if(mn(tmp[i],a)==tmp[i]) a=mi(a,tmp[i]);
	}
//	cout << a << endl;
	return a;
}

//GCD
string gcd(string a,string b){
	return zero(b)==0 ? gcd(b,jouyo(a,b)) : a;
}


int main(){
	int t;
	cin >> t;
	int n;
	string s[1001];
	for(int ii=0;ii<t;ii++){
		cin >> n;
		int i,j;
		for(i=0;i<n;i++){
			cin >> s[i];
			reverse(&s[i][0],&s[i][0]+s[i].length());
		}
		string ans=mi(s[0],s[1]);
		for(i=2;i<n;i++){
			ans=gcd(ans,mi(s[i-1],s[i]));
		}
		string mins=s[0];
		for(i=1;i<n;i++){
			mins=mn(mins,s[i]);
		}
		if(mn(mins,ans)==ans) mins=jouyo(mins,ans);
//		cout << ans << "	" << mins << endl;
		if(zero(mins)==0) ans=mi(ans,mins);
		else ans='0';
		reverse(&ans[0],&ans[0]+ans.length());
		printf("Case #%d: %s\n",ii+1,ans.c_str());
	}
	return 0;
}


