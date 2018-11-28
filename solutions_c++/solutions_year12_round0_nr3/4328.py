#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cmath>

using namespace std;

//void reverse(string& ss)
//{
//	int len = ss.length();
//	for(int i=0;i<len/2;i++){
//		char t = ss[i];
//		ss[i] = ss[len - 1 - i];
//		ss[len-1 - i] = t;
//	}
//	return;
//}

int stringToInt(string ss)
{
	int num = 0;
	for(int i=0;i<ss.length();i++){
		num = num * 10 + ss[i] - '0';
	}
	return num;
}

string intToString(int num)
{
	string res;
	while(num > 0){
		res += (num%10) + '0';
		num /= 10;
	}

	reverse(res.begin(), res.end());
	return res;
}

int numOfm(int n, int B)
{
	int sum = 0;
	string nStr = intToString(n);
	int len = nStr.length();
	map<int, int> seen;
	for(int i=1 ; i <= len -1 ;i++){
		string nSubStr = nStr.substr(i, len-i);
		string newStr = nSubStr + nStr.substr(0, i);
		int m = stringToInt(newStr);
		seen[m]++;
		if(m > n && m<=B && seen[m]==1) {
			++sum;
			//cout << n << " " << m << ", ";
		}
	}

	//if(sum > 0)
	//	cout << endl;

	return sum;
}

_int64 solve(int A, int B)
{
	_int64 sum = 0;
	for(int n = A ; n < B-1; n++)
	{
		sum += numOfm(n, B);
	}

	return sum;
}

//int RecycledNumbers()
int main()
{
	freopen("RecycledNumbersS.in", "r", stdin);
	freopen("RecycledNumbersS.out", "w", stdout);

	int t;
	cin >> t;
	
	for(int i=1;i<=t;++i)
	{
		int A, B;
		cin >> A >> B;
		
		cout << "Case #" << i << ": ";
		cout << solve(A, B) << endl;
	}
	return 0;
}