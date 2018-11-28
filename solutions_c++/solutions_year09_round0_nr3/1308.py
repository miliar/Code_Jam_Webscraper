#include <iostream>
#include <fstream>
using namespace std;

class Count
{
public:
	int* a;
	Count()
	{
		a = new int[19];
		for(int i = 0; i < 19; i++)
			a[i] = 0;
	}
	~Count()
	{
		delete[] a;
	}
	void add(int index)
	{
		int add = 0;
		if(index == 0) add = 1;
		else add = a[index - 1];
		a[index] += add;
		makeDigits(index);
	}
	void makeDigits(int i)
	{
		if(a[i] > 10000)
			a[i] = a[i] % 10000;
	}
};

int main()
{
	ifstream in("in.in");
	ofstream out("out.out");
	int n = 0;
	in >> n;
	string line = "";
	getline(in,line);
	for(int i = 1; i <= n; i++)
	{
		Count cnt;
		getline(in,line);
		for(int j = 0; j < line.length(); j++)
		{
			if(line[j] == 'w')
				cnt.add(0);
			else if(line[j] == 'e')
			{
				cnt.add(1);
				cnt.add(6);
				cnt.add(14);
			}
			else if(line[j] == 'l')
				cnt.add(2);
			else if(line[j] == 'c')
			{
				cnt.add(3);
				cnt.add(11);
			}
			else if(line[j] == 'o')
			{
				cnt.add(4);
				cnt.add(9);
				cnt.add(12);
			}
			else if(line[j] == 'm')
			{
				cnt.add(5);
				cnt.add(18);
			}
			else if(line[j] == ' ')
			{
				cnt.add(7);
				cnt.add(10);
				cnt.add(15);
			}
			else if(line[j] == 't')
				cnt.add(8);
			else if(line[j] == 'd')
				cnt.add(13);
			else if(line[j] == 'j')
				cnt.add(16);
			else if(line[j] == 'a')
				cnt.add(17);
		}
		int result = cnt.a[18];
		out << "Case #" << i << ": ";
	       	if(result < 10) out << "000";
		else if(result < 100) out << "00";
		else if(result < 1000) out << "0";
		out << result << endl;
	}
	in.close();
	out.close();
	return 0;
}


