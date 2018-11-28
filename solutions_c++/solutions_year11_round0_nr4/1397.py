#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

//input-output

//algorithm

//bool generatePartition( vector<int>& partition//large to small
//					   )
//{
//
//	int n = partition.size();
//	//assert(n>=1);
//	if (partition[0]==1) return false;
//	//we find the lastest element >= 2
//	int k = n;
//	int sum = 0, a = 0;
//	for (int i=n-1; i>=0; --i)
//	{
//		sum += partition[i];
//		if (partition[i]>=2) 
//		{
//			k = i;
//			a = partition[i]-1;
//			break;
//		}
//	}
//	partition.resize(k);
//
//	while (sum !=0)
//	{
//		if (sum>=a)
//		{
//			partition.push_back(a);
//			sum -= a;
//		}
//		else
//		{
//			partition.push_back(sum);
//			sum = 0;
//		}
//	}
//}
//

class Gorosort
{
public:
	int T;
	vector<vector<int>> datas;

	Gorosort(string name)
	{
		ifstream f(name.c_str());
		if (f.is_open())
		{
			f >> T;
			datas.resize(T);
			for (int i=0; i<T; ++i)
			{
				int n;
				f >> n;
				datas[i].resize(n);
				for (int j=0; j<n; ++j)
				{
					f >> datas[i][j];
				}
			}
		}
	}

	int result(int k)
	{
		vector<int>& data = datas[k];
		int count = 0;
		for (int i=0; i<data.size(); ++i)
		{
			if (data[i]!=i+1) count++;
		}
		return count;
	}

	void run(const string& output)
	{
		ofstream f(output.c_str());
		for (int i=0; i<T; ++i)
		{
			f << "Case #"<<(i+1)<<": ";
			f << result(i)<<endl;
		}
	}
};
int main(int argc, char** argv)
{
	Gorosort goro(argv[1]);
	goro.run(argv[2]);
}