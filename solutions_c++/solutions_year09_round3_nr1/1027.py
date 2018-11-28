#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<map>
#include<cmath>

using namespace std;

int main()
{
	int test = 0;

	std::ifstream ifs( "test.txt" );
	std::ofstream ofs( "output.txt" );

	ifs >> test;
	ifs.ignore();

	map<char, int> m;
	for(int k = 0; k < test; k++)
	{
		char buf[10000];
		ifs.getline(buf, 10000);
		istringstream isfs(buf);
		int count = 0;
		int base = 0;
		while(!isfs.eof())
		{
			buf[count] = isfs.get();
			if(m[buf[count]] == 0)
			{
				base++;
				m[buf[count]] = -1;
			}
			count++;
		}
		count--;
		base--;
		//for(int i = 0; i < count; i++)
		//{
		//	cout << buf[i] << endl;
		//}
		//cout << base << endl;

		if(base == 1)
		{
			base = 2;
		}

		int value = 0;
		m[buf[0]] = 1;
		for(int i = 1; i < count; i++)
		{
			if(m[buf[i]] == -1)
			{
				m[buf[i]] = value;
				value++;
				if(value == 1)
				{
					value++;
				}
			}
		}

		int sum = 0;
		for(int i = count - 1; i >= 0; i--)
		{
			sum += m[buf[i]] * pow((double)base, count - i - 1);
		}
		cout << "Case #" << k + 1 << ": " << sum << endl;
		ofs << "Case #" << k + 1 << ": " << sum << endl;

		m.clear();
	}

	return 0;
}