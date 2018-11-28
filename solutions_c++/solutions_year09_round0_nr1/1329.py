#include <iostream>
#include <string>
using namespace std;
int L,D,N;

bool match(string a, string b)
{
	int pt = 0;int i=0;
	for(;i<b.size() && pt<a.size();i++)
	{
		if(b[i]!='(')
		{
			//cerr<<b[i]<<" "<<a[pt]<<endl;
			if(b[i]!=a[pt]) return false;
			
		}
		else
		{
			bool matched = false;
			while(++i)
			{
				if(b[i]==')') break;
				if(b[i]==a[pt]) matched = true;
			}
			if(!matched) return false;
		}
		pt++;
	}
	return true;
}



int main()
{
	cin>>L>>D>>N;
	string words[10000];
	
	for(int i=0;i<D;i++)
		cin>>words[i];
	for(int i=0;i<N;i++)
	{
		string k;
		cin>>k;
		int c = 0;
		//cout<<k;
		for(int j=0;j<D;j++)
			if(match(words[j],k)) c++;
		cout<<"Case #"<<i+1<<": "<<c<<endl;
	}
	
	
}