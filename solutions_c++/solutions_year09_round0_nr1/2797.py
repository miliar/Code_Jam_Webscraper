#include <iostream>
#include <vector>
#include <map>

using namespace std;


bool match(string s, string t)
{
	int pt=0;
	for(int i=0; i<s.length(); i++)
	{
		map<char, int> mp;
		if(t[pt]=='(')
		{
			pt++;
			while(t[pt]!=')') {mp[t[pt]]++; pt++;}
			pt++;
		}
		else { mp[t[pt]]++; pt++; }
		if( mp.count(s[i])==0) return false;
	}	
	return true;
}

int main()
{
	int L,D,N;
	cin>>L>>D>>N;
	vector<string> dic;
	for(int i=0; i<D; i++) {string word; cin>>word; dic.push_back(word);}

	for(int q=1; q<=N; q++)
	{
		string p;
		cin>>p;

		int cnt=0;
		for(int i=0; i<D; i++) if( match(dic[i], p) ) cnt++;
		cout<<"Case #"<<q<<": "<< cnt <<endl;
	}
	return 0;

}
