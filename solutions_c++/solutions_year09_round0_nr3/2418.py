#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
string t="welcome to code jam";
unsigned long long cnt;

void findAll(string& str,int curInd,int curPos)
{
	if(curInd==t.size())
	{
		cnt++;
		return;
	}
	int ind=curPos;
	while((ind=str.find_first_of(t[curInd],ind))!=-1)
	{
		findAll(str,curInd+1,++ind);
	}
}
int main()
{
	int N;
//#ifndef LOCAL
	ifstream cin("C-small.in");
	ofstream cout("C-small.out");
//#endif
	cin>>N;
	cin.get();
	for(int ii=1;ii<=N;ii++)
	{
		string str;
		getline(cin,str,'\n');
		for(int i=0;i<str.size();i++)
			str[i]=tolower(str[i]);
		cnt=0;
		
		findAll(str,0,0);
		stringstream strm;
		strm<<cnt;
		string t;
		strm>>t;
		while(t.size()<4)
			t="0"+t;
		cout<<"Case #"<<ii<<": "<<t.substr(t.size()-4,4)<<endl;
	}
	return 0;
}