#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
int main(int argc, char *argv[])
{

	ifstream  ifs("input");
	ofstream ofs("output");

	int N;
	ifs >> N;
	cout << (3^5) << endl;

	cout << (6^5) << endl;
	cout << (3^6) << endl;


	for (int cas = 0; cas < N; ++cas)
	{
//		cout << "Case " <<cas << endl;
		int count;
		ifs >> count;
		vector< int> vr(count);
		for (int i =0; i< count; ++i)
			ifs >> vr[i];

		int m = -1;

		for (int i = 1; i+1< 1<<vr.size();++i)
		{
			int res1 =0;
			int res2 =0;
			int sum1= 0;
			int sum2 = 0;
			for (int j =0; j< vr.size(); ++j)
			{
				if (1<<j & i)
				{
					res1 ^= vr[j];
					sum1 += vr[j];
				}
				else
				{
					res2 ^= vr[j];
					sum2 += vr[j];
				}
			}
			if (res1 == res2)
			{
				m = max(m, sum1);
				m = max(m, sum2);
			}

		}
		ofs << "Case #" << cas +1 << ": ";
		if (m == -1)
			ofs << "NO" <<endl;
		else
			ofs << m <<endl;
//		for (int i =0; i < )
//		ofs << "Case #" << cas +1 << ": "<< cur_time <<endl;

//		for (int i =0; i< vr.size(); ++i)
//			cout << vr[i].first << " "<< vr[i].second << endl;
	}


}
