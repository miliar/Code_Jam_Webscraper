#include<map>
#include<fstream>
#include<string>

using namespace std;

int main()
{
	map<char, char> hash;
	
	ifstream ip1("input.txt");
	ifstream ip2("input1.txt");

	ifstream ip3("A-small-attempt2.in");
	ofstream op("A-small-attempt2.out");
	
	char tmp1,tmp2;
	while(ip1>>tmp1)
	{
		if(tmp1==' ')
			continue;

		ip2>>tmp2;
		hash[tmp1]=tmp2;
	}
	hash[' ']=' ';
	hash['z']='q';
	hash['q']='z';
	
	int n;
	ip3>>n;
	string str;
	getline(ip3,str);
	for(int i=0;i<n;i++)
	{
		op<<"Case #"<<i+1<<": ";
		getline(ip3,str);
		for(int i=0;i<str.length();i++)
			op<<hash[str[i]];
		op<<endl;
	}
			
	return 0;
}

