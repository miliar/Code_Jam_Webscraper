#include <iostream>
#include <fstream>

using namespace std;

int xor(int a, int b)
{
	return a^b;
}

int main()
{
	ofstream fout;
	fout.open("output.txt");
	int cases;
	cin >>cases;
	int candy;
	int ctemp[1001];
	int total;
	int xtotal;
	int min;

	for (int h=0;h<cases;h++)
	{
		min = 60000000;
		total=0;
		xtotal=0;
		int candies;
		cin>>candies;
		for (int i=0;i<candies;i++)
		{
			cin>>candy;
			total=total+candy;
			xtotal=xor(xtotal,candy);
			if (candy<min)
			{
				min=candy;
			}
		}

		if (xtotal!=0) fout<< "Case #"<<h+1<<": NO"<<endl;
		else fout<< "Case #"<<h+1<<": "<<(total-min)<<endl;
	}
	fout.close();
	return 0;
}