#include <iostream>
#include <vector>
using namespace std;

string i2s(int n){
	//cout << "i2s got " << n << endl;
	string ret;
	while (n>=10){
		string temp="a";
		temp[0]='0'+n%10;
		ret=temp+ret;
		n/=10;
	}
	string temp="a";
	temp[0]='0'+n%10;
	ret=temp+ret;
	//cout << "i2s ret " << ret << endl;
	return ret;
	
}

int s2i(string &s){
	//cout << "s2i got " << s << endl;
	int ret=0;
	for (int i=0;i<(int)s.length();i++){
		ret*=10;
		ret+=s[i]-'0';
	}
	//cout << "s2i ret " << ret << endl;
	return ret;

	
}



int recy(int m,int a,int b){

	string number=i2s(m); 
		//cout << "checking for "  << m  << "(" << number << ")" << endl;
	vector<int> marked;
	for (int i=0;i<(int)number.length();i++){
		string x=number.substr(i+1,(int)number.length()-i-1)+number.substr(0,i+1);
		if (x[0]=='0') continue;
		//cout << "made " << x << endl;
		int n=s2i(x);
		if (n<m && n>=a && n<=b && find(marked.begin(),marked.end(),n)==marked.end()) 
		{
			//cout << n << "(" << x << ")" << " ----------->is good " << endl;
			marked.push_back(n);
		}
	}
	//cout << "returinign " << marked.size() << endl;
	return marked.size();
}


int main(){
	int tests;
	cin >> tests;
	for (int test=0;test<tests;test++){
		int a,b;
		cin >> a >> b;
		int ans=0;
		for (int i=a;i<=b;i++)
			ans+=recy(i,a,b);
		cout << "Case #" << test+1 << ": " << ans << endl;
	}

	return 0;
}