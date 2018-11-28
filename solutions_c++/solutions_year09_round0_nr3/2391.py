#include<iostream>
#include<fstream>
#include <iomanip>


using namespace std;

int match(string str1, string str2)
{
	int count = 0;
	int found = 0;
	if(str1.length() == 1)
	{
		while((found = str2.find(str1)) != string::npos)
		{
			//cout<<str2<<endl;
			count++;
			str2 = str2.substr(found+1, str2.length()-found);
		}
		return count;
	}
	char c = str1[0];
	str1 = str1.substr(1, str1.length()-1);
	while((found = str2.find(c)) != string::npos)
	{
		str2 = str2.substr(found+1, str2.length()-found);
		count += match(str1, str2);
	}
	return count;

}

int main()
{
	ifstream fin
	("D:\\CodingForFun\\google code jam\\2009 1 Qualification\\files\\C1.in");
	ofstream fout
	("D:\\CodingForFun\\google code jam\\2009 1 Qualification\\files\\C1.out");

	int N;
	fin>>N;
	cout<<N<<endl;
	string str;
	getline(fin, str);
//	cout<<match("welcome to code jam", "wweellccoommee to code qps jam");
	for(int i = 0; i < N; i++)
	{
		getline(fin, str);
		int mat = match("welcome to code jam", str);

		cout<<"Case #"<< i+1 <<": "<<mat<<endl;
		fout<<"Case #"<< i+1 <<": "<<setw(4)<<setfill('0')<<mat<<endl;
	}

	return 0;
}
