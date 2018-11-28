#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main()
{
	int T;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> T;
	for(int ca=0;ca<T;ca++)
	{
		int n;
		queue<int> b,o;
		queue<char> bo;
		fin >> n;
		for(int i=0;i<n;i++)
		{
			char t;
			int ti;
			fin >> t >> ti;
			bo.push(t);
			if (t=='O')
				o.push(ti);
			else
				b.push(ti);
		}
		int poso=1,posb=1;
		int count=0;
		for(int i=0;i<n;i++)
		{
			char nowc=bo.front();
			bo.pop();
			if (nowc=='O')
			{
				int nowpos=o.front();
				o.pop();
				int dif=abs(nowpos-poso)+1;
				if (!b.empty())
					if (abs(b.front()-posb)<dif)
					{
						posb=b.front();
					}
					else
						if (posb<b.front())
							posb+=dif;
						else
							posb-=dif;
				poso=nowpos;
				count+=dif;
			}
			else
			{
				int nowpos=b.front();
				b.pop();
				int dif=abs(nowpos-posb)+1;
				if (!o.empty())
					if (abs(o.front()-poso)<dif)
					{
						poso=o.front();
					}
					else
						if (poso<o.front())
							poso+=dif;
						else
							poso-=dif;
					posb=nowpos;
					count+=dif;
			}
		}
		fout << "Case #" << ca+1 << ": " << count << "\n";
	}
	return 0;
}