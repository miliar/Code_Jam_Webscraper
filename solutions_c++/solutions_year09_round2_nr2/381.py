#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int size;
	cin>>size;
	string num,s;
	getline(cin,s);
	for(int i = 1; i<=size;i++)
	{
		getline(cin,num);
		num.insert(0,"0");
		next_permutation(num.begin(),num.end());
		if(num[0] == '0')
			num.erase(0,1);
		cout<< "Case #"<<i<<": "+num+"\n";
	}
	return 0;
}