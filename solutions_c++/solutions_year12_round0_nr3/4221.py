#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>


using namespace std;
ifstream inp("c:\\C-small-attempt0.in");
ofstream out("c:\\gcj\\no3.out");

string itos(int i)
{
	string ret;
	int tmp = i;
	while (tmp)
	{
		int r = tmp % 10;
		tmp /=10;
		string rs;
		rs += (char)(r+'0');
		ret = rs+ret;
	}
	return ret;
}

void process(int t)
{
	int A,B;
	inp >> A >> B;
	int ret = 0;
	for (int d = A; d <= B; d++)
	{
		string s = itos(d);
		int len = s.length();
		map<int,bool> visited;
		for ( int i = 1; i < len; i++ )
		if ( s[i] != '0')
		{
			string s1 = s.substr(i, len-i) + s.substr(0,i);
			stringstream ss(s1);
			int m;
			ss >> m;
			if ( m > d && m >= A && m <= B && !visited[m] )
			{
				visited[m] = true;
				ret ++;
			}
		}
	}

	
	out<<"Case #"<<t+1<<": "<<ret<<endl;
 
}

int main()
{
	int T;
	inp >> T;
	cout<<T<<endl;
	for ( int t = 0; t < T; t++)
	{
		process(t);
		
	}
}