#include<iostream>
#include<string>
#include<algorithm>

using namespace std;
int main()
{
	int i,j,k,n;
	string s,s1;
	int t;int cnt=1;
	cin>>t;
	while(t--){
		cout<<"Case #"<<cnt<<": ";
		cin>>s;
		s1=s;
		next_permutation(s.begin(),s.end());
	//	cout<<s<<endl;
		if(s1<s){
			cout<<s<<endl;
		}else{
		//	if(s1[s.size()-1]=='0')cout<<s1<<"0\n";
			s+='0';
			sort(s.begin(),s.end());
			int i11=0;
			while(s[i11]=='0')i11++;
			//cout<<i11<<"\n";
			char tmp=s[i11];
			s[i11]=s[0];
			s[0]=tmp;
/*			else{
			sort(s.begin(),s.end());
			s='0'+s;
			swap(s[0],s[1]);*/
			cout<<s<<endl;
		}
		
		cnt++;
	}	
	return 0;
}
