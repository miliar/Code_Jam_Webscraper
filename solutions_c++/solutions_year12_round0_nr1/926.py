#include <fstream>
#include <string>

using namespace std;
ifstream fin("input.in");
ofstream fout("output.out");

int mapping[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};

int main()
{
	int t;
	string s;

    fin>>t;
	getline(fin,s);
	for (int i=1;i<=t;i++)
	{
		getline(fin,s);
		int len=s.length();
		for (int j=0;j<len;j++)
          if (s[j]!=' ')
			  s[j]=(char)(mapping[s[j]-97]+97);
		fout<<"Case #"<<i<<": "<<s<<endl;
	}
	return 0;
}
