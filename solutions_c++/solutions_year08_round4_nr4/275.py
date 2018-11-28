#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int get(string a){
	int c=0;
	int start=0;
	int end=0;
	while(start!=a.length()){
		while(end<a.length() && a[end]==a[start])end++;
		c++;
		start=end;
	}
	return c;
}

void solve(int t){
	cout<<"Case #"<<t<<": ";

	int k;
	cin>>k;
	string s;
	cin>>s;

	int perm[8];
	for(int i=0;i<8;i++)
		perm[i]=i;

	int ans=1000000;
	do{
		string ret="";
		for(int start=0;start<s.length();start+=k){
			string sub=s.substr(start,k);
			for(int i=0;i<k;i++){
				ret+=sub[perm[i]];
			}
		}

		int now=get(ret);

		if(now<ans)ans=now;

	}while(next_permutation(perm,perm+k));

	cout<<ans<<endl;
}
int main(){

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);


	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		solve(i);
	}
}