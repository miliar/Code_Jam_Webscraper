#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out ("out.txt");
	int t;
	in >> t;
	int n;
	long long k,temp;
	
	vector <int> bin;
	for(int i=0;i<t;i++)
	{
		bool pr=false;
		bin.clear();
		in >> n >> k;
		temp = k;
		while(temp!=0)
		{
			bin.push_back(temp%2);
			temp/=2;
		}
		if(bin.size() >=n)
		{
			for(int j=0;j<=n-1;j++)
			{
				if(bin[j]==0)
				{
					pr=true;
				}
			}
			if(!pr)
				out << "Case #" << i+1 << ": ON"<<endl;
			else
				out << "Case #" << i+1 << ": OFF"<<endl;
		}
		else
			out << "Case #" << i+1 << ": OFF"<<endl;
	}
	return 0;
}