#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

class Candy
{
public:
	int T;
	vector<vector<int>> values;

	Candy(string name)
	{
		ifstream f(name.c_str());
		if (f.is_open())
		{
			f >> T;
			values.resize(T);
			for (int i=0; i<T; ++i)
			{
				int n;
				f >> n;
				values[i].resize(n);
				for (int j=0; j<n; ++j)
					f >> values[i][j];
			}
		}
		f.close();
	}

	int divide(int k)
	{
		vector<int>& value = values[k];
		int sum_xor = 0, sum = 0;
		int min_value = value[0];
		for (int i=0; i<value.size(); ++i)
		{
			sum_xor = sum_xor ^ (value[i]);
			sum += value[i];
			min_value = min(min_value, value[i]);
		}
		if (sum_xor != 0) return -1;
		else return (sum-min_value);



	}	

	void run(string name)
	{
		ofstream f(name.c_str());
		for (int k=0; k<T; ++k)
		{
			f <<"Case #"<<k+1<<": ";
			int a = divide(k);
			if (a<0) f <<"NO"<<endl;
			else f <<a<<endl;
		}
	}


};
int main(int argc, char**argv)
{
	Candy candy(argv[1]);
	candy.run(argv[2]);
}