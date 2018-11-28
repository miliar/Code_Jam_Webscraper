#include<algorithm>
#include<iostream>
#include<vector>
#include<string>


using namespace std;

string s;

void solve()
{

	if(next_permutation(s.begin(),s.end()))
	{
		cout<<s<<endl;
		return;
	}
//	return;
	string s1;
	char mn='9';
	int i,j;
	int n=s.size();
	sort(s.begin(),s.end());
	for(i=0;i<n;++i)
		if(s[i]!='0')
		{
			s1+=s[i];
			s1+='0';
			for(j=0;j<i;++j)
				s1+=s[j];
			for(j=i+1;j<n;++j)
				s1+=s[j];
			break;
		}
	cout<<s1<<endl;
}

int main()
{
	freopen("output.txt","w",stdout);
	int t,l;
	cin>>t;
	int k;
	for(l=0;l<t;++l)
	{
		cin>>s;
		cout<<"Case #"<<l+1<<": ";
		solve();
	}
	return 0;
}