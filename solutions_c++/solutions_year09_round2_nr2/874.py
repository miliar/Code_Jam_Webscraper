#include <iostream>
#include <vector>
#include <string>

using namespace std;
int n,t,len;
vector <char> a,b;
string s;
bool eend;

int main (){
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	cin>>t;
	for (int k=0;k<t;k++){
		cin>>s;
		len=s.length();
		a.clear();
		eend=true;
		for (int i=0;i<len-1;i++)
			if (s[i]<s[i+1]) eend=false;
		if (eend) a.push_back('0');
		for (int i=0;i<len;i++)a.push_back(s[i]);
		if (eend) len++;
		next_permutation(a.begin(),a.end());
		while (a[0]=='0') next_permutation(a.begin(),a.end());
		cout<<"Case #"<<k+1<<": ";
		for (int i=0;i<len;i++) cout<<a[i];
		cout<<endl;
	}

	return 0;
}
