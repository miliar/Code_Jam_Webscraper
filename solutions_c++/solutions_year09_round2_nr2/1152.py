#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string NextNumberMoreZero( const string number )
{
	int cnt[10];
	memset(cnt, 0, sizeof(cnt));
	for (int i=0; i<number.length(); ++i)
	{
		cnt[number[i]-'0']++;
	}
	bool firstFound = false;
	string next;
	for (int i=1;i<10;++i)
	{
		if (!firstFound && cnt[i]>0)
		{
			firstFound = true;
			next.append(1, char(i+'0'));
			next.append(cnt[0]+1, '0');
			if (cnt[i]>1)
				next.append(cnt[i]-1, char(i+'0'));
		}
		else if (cnt[i]>0)
		{
			next.append(cnt[i], char(i+'0'));
		}
	}
	return next;
}

string NextNumber(const string number)
{
	for (int i=number.length()-1; i>=0; --i)
	{
		if (number[i]<number[i+1])
		{
			int j=i+1;
			while (number[j]>number[i] && j < number.length()) ++j;
			string res;
			res += number.substr(0, i);
			res.append(1, number[j-1]);
			string s;
			s.append(1, number[i]);
			s.append(number.substr(i+1, j-i-2));
			s.append(number.substr(j));
			sort(s.begin(), s.end());
			res += s;
			return res;
		}
	}
	
	return NextNumberMoreZero( number );
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t=1; t<=T; ++t)
	{
		string number;
		cin >> number;
		cout << "Case #" << t << ": " << NextNumber( number ) << endl;
	}	
}