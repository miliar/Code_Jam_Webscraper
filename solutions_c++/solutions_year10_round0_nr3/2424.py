#include <fstream>
#include <queue>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int cases;
	fin>>cases;
	int tcase = 1;
	while(cases--)
	{
		int r,k,n,g,coin = 0;
		fin>>r>>k>>n;
		queue<int> myque;
		queue<int> myque2;
		for(int i = 0; i < n; i++)
		{
			fin>>g;
			myque.push(g);
		}
		while(r--)
		{
			int sum = 0;
			while(!myque.empty() && sum + myque.front() <= k)
			{
				sum += myque.front();
				myque2.push(myque.front());
				myque.pop();
			}
			while(!myque2.empty())
			{
				myque.push(myque2.front());
				myque2.pop();
			}
			coin += sum;
			
		}
		fout<<"Case #"<<tcase++<<": "<<coin<<endl;
	}
	fin.close();
	fout.close();
	
	return 0;
}