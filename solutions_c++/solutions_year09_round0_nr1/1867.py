#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

bool match(string patt, string text)
{
	int i = 0;
	istringstream in(patt.c_str());

	int l=0;
	while(i < patt.size())
	{
		string cur="";
		if(patt[i] == '(')
		{
			int j;
			for(j=i ; j<patt.size() && patt[j]!=')'; j++)
				cur += string(1,patt[j]);
			i = j+1;
		}
		
		else
		{
			int j;
			for(j=i ; j<patt.size() && patt[j]!='('; j++)
				cur += patt[j];
			i = j;
		}

//		cout<<cur<<endl;	
		if(cur[0] == '(')
		{
			if(find(cur.begin() , cur.end() , text[l]) == cur.end())
				return 0;
			l++;
		}

		else
		{
			for(int k=0 ; k<cur.size() ; k++,l++)
				if(cur[k] != text[l])
					return 0;
		}
	}
	
	//cout<<text<<endl;
	return true;
}

int main()
{
	int L, D, N;
	cin>>L>>D>>N;
	char str[1000];

	vector<string> dict;
	for(int i=0 ; i<D ; i++)
	{
		string s;
		cin>>s;
		dict.push_back(s);
	}

	for(int t=1;  t<=N ; t++)
	{
		cin>>str;
		int c=0;
		for(int j=0  ; j<D ; j++)
			if(match(str , dict[j]))
				c++;

		cout<<"Case #"<<t<<": "<<c<<endl;
	}			
	return 0;
}
