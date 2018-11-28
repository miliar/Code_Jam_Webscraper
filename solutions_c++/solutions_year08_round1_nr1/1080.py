#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<map>
#include<algorithm>
#include<iterator>
#include<utility>
#include<cmath>
#include<vector>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<numeric>
using namespace std;
int string_to_int(const string& s);
double string_to_double(const string& s);
int main()
{
	ifstream in("a.in");
	ofstream out("output.txt");
	int n;
	string st;
	getline(in,st);
	n=string_to_int(st);
	for(int i=1;i<=n;i++)
	{
		string str;
		int k;
		getline(in,str);
		k=string_to_int(str);
		//vector<double> ivec1;
		//vector<double> ivec2;
		vector<int> ivec1;
		vector<int> ivec2;

		string str1;
		string str2;
		getline(in,str1);
		getline(in,str2);
		stringstream ss1(str1);
		stringstream ss2(str2);
		string temp;
		while(ss1>>temp)
		{
			ivec1.push_back(string_to_int(temp));
		}
		while(ss2>>temp)
		{
			ivec2.push_back(string_to_int(temp));
		}
		sort(ivec1.begin(),ivec1.end());
		reverse(ivec1.begin(),ivec1.end());
		sort(ivec2.begin(),ivec2.end());
		//vector<double> result;
		//vector<double>::iterator iter2=ivec2.begin();
		vector<int> result;
		vector<int>::iterator iter2=ivec2.begin();

		for(vector<int>::iterator iter1=ivec1.begin();iter1!=ivec1.end();iter1++,iter2++)
		{
			result.push_back(*iter1 * *iter2);
		}
		int ans=accumulate(result.begin(),result.end(),0);
		out<<"Case #"<<i<<": "<<ans<<endl;
	}
}
int string_to_int(const string& s)
{
	stringstream str(s);
	//str<<s;
	int result;
	str>>result;
	return result;
}
double string_to_double(const string& s)
{
	stringstream str(s);
	//str<<s;
	int result;
	str>>result;
	return result;
}
