#include <iostream>
#include <map>
#include <string>

using namespace std;

int T, C, D, N;
map<char, char> oppe;
map<pair<char, char>, char> combine;

const int MAXLEN=100+5;

string Compute(const string& str)
{
	char buffer[MAXLEN];
	int pos=-1;
	for (int i=0; i<N; i++)
	{
		char ch=str[i];
		pos++;
		buffer[pos]=ch;
		if (pos>0 && combine.find(pair<char, char>(buffer[pos], buffer[pos-1]))!=combine.end())
		{
			buffer[pos-1]=combine[pair<char, char>(buffer[pos], buffer[pos-1])];
			pos--;			
		}
		else 
		{
			bool find=false;
			for (int j=0; j<pos; j++)
				if (oppe.find(buffer[pos])!=oppe.end() && oppe[buffer[pos]]==buffer[j])
				{
					find=true;
					break;
				}
			if (find)
				pos=-1;
		}
	}

	string ret;
	if (pos<0)
		ret="[]";
	else
	{
		ret="[";
		ret=ret+buffer[0];
		for (int i=1; i<=pos; i++)
		{
			ret=ret+", "+buffer[i];
		}
		ret=ret+"]";
	}
	return ret;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin>>T;
	for (int i=0; i<T; i++)
	{
		combine.clear();
		oppe.clear();

		cin>>C;
		for (int i=0; i<C; i++)
		{
			string st;
			cin>>st;
			combine[pair<char, char>(st[0], st[1])]=st[2];
			combine[pair<char, char>(st[1], st[0])]=st[2];
		}
		
		cin>>D;
		for (int i=0; i<D; i++)
		{
			string st;
			cin>>st;
			oppe[st[0]]=st[1];
			oppe[st[1]]=st[0];
		}

		cin>>N;		
		string inputStr;
		cin>>inputStr;

		string retStr=Compute(inputStr);
		cout<<"Case #"<<(i+1)<<": "<<retStr<<endl;
	}

	return 0;
}