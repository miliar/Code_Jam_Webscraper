#include<iostream>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<sstream>
#include<vector>
using namespace std;


bool fun(int number)
{
	int digit1 = number %10, digit2;
	while(number!=0)
	{
		digit2 = number % 10;
		if(digit1 != digit2)
		{
			return false;
		}
		number /= 10;
	}
	return true;
}

int numofdigits(int number)
{
	int re = 0;
	while(number != 0)
		number/=10, re++;
	return re;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int A, B, t, digit, number, tempo;
	string str, str1 = "", str2;
	cin >> t;
	stringstream ss, ss1;
	for(int w = 1; w <= t; w++)
	{
		int res = 0, temp;;
		cin >> A >> B;
		ss.clear();
		ss1.clear();
		map <pair<int, int>, int> m;
		for(int i = A; i <= B; i++)
		{
			temp = i;
			tempo = i;
			number = 0;
			str2 = "";
			str = "";
			int tempos;
			while(temp/10 != 0)
			{
				temp/=10;
				//bn2s el rakam
				digit = tempo%10;
				tempos = tempo;
				tempo /= 10;
				ss1.clear();
				//rakam mn 3'er a5er digit
				ss1 << tempo;
				ss1 >> str;
				ss1.clear();
				//first digit
				ss1 << digit;
				ss1 >> str2;
				ss1.clear();
				str1 = str2 + str;
				ss1 << str1;
				ss1 >> number;
				ss1.clear();
				if(number >= A && number <= B)
				{
					pair<int, int> p, p1;
					p.first = number;
					p.second = i;
					p1.first = i;
					p1.second = number;
					if(!fun(number) && /*!arr[number] && !arr[tempo]*/m[p] != 1 && m[p1] != 1)
					{
						m[p] = 1;
						if(number == i)
							continue;
						if(numofdigits(number) < numofdigits(i))
							continue;
						res++;
					}
				}
				tempo = number;
			}

		}
		cout << "Case #" << w << ": " << res << endl;
	}

}