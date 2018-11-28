#include <iostream>
#include <sstream>

using namespace std;

string itoa(int);
bool is_pair(int,int);
int num_pairs(int,int);

int main()
{
	int n;
	cin >> n;
	for(int i = 1; i <=n; i++)
	{
		int a, b;
		cin >> a >> b;
		cout << "Case #" << i << ": " << num_pairs(a,b) << endl;
	}
}

string itoa(int num)
{
	stringstream ss;
	ss << num;
	return ss.str();
}

bool is_pair(int in, int im)
{
	string n = itoa(in), m = itoa(im);
	if(n.length() != m.length()) return false;
	for(int i = 1; i < n.length(); i++)
	{
		string tmp = n.substr(i) + n.substr(0,i);
		if(tmp.compare(m) == 0) return true;
	}
	return false;
}

int num_pairs(int a, int b)
{
	int cnt = 0;
	for(int i = a; i < b; i++)
	{
		for(int j = i+1; j <= b; j++)
		{
			if(is_pair(i,j))
				cnt++;
		}
	}
	return cnt;
}