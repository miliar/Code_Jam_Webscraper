#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

#decine MAX 1005

string toString (int i)
{
	ostringstream out;
	out<<i;
	return out.str();
}

int toNum (string s)
{
	int len = s.length();
	int ret = 0;
	for (int i=0;i<len;i++)
		ret += (s[i]-'0')*pow(10.0,len-i-1);
	
	return ret;
}
void rotate(string &s) {
  for (int i = 1; i < s.size(); i++)
    swap(s[i-1], s[i]);
}

int main ()
{
	ifstream fin("CodeJam.in");
	ofstream fout("CodeJam.out");

	int tests;
	cin>>tests;

	for (int it=0;it<tests;it++)
	{
		int A,B,cnt=0;
		cin>>A>>B;

		bool visited [MAX][MAX];
		memset (visited,false,sizeof(visited));

		for (int i=A;i<=B;i++)
		{
			string s = toString (i);
			for (int j=0;j<s.length()-1;j++)
			{
				rotate(s);
				int x = toNum (s);
				if (visited[i][x])	continue;
				if (x>=A && x<=B && x!=i)	{cnt++;	visited[i][x]=true; visited[x][i]=true;}
			}
		}
		cout<<"Case #"<<it+1<<": "<<cnt<<endl;
	}
	return 0;
}