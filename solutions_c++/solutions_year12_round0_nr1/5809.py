#include<iostream>
#include<string>
using namespace std;

char mapping[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int CN;
	cin >> CN;
	cin.ignore();
	for(int k=1;k<=CN;k++)
	{
		string str,res;
		getline(cin,str);
		printf("Case #%d: ",k);
		for(int i=0;i<str.size();i++)
		{
			if(str[i] != ' ')
				res += mapping[str[i]-'a'];
			else
				res += " ";
		}
		cout << res << endl;
	}
	return 0;
}