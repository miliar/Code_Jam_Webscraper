#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	ofstream fout;
	fout.open("output.txt");
	fout.setf(ios::fixed,ios::floatfield);
	fout.precision(6);
	int cases;
	cin>>cases;
	int sorts[1004];
	int sorted[1004];
	int vals;
	int total;

	for (int h=0;h<cases;h++)
	{
		cin>>vals;
		total=0;
		for (int i=0;i<vals;i++) 
		{
			cin>>sorts[i];
			sorted[i]=sorts[i];
		}
		sort(sorted,sorted+vals);
		for (int i=0;i<vals;i++)
		{
			if (sorts[i]!=sorted[i]) total++;
		}
		/*
		for (int i=0;i<vals;i++)
		{
			if (sorts[i]!=sorted[i])
			{
				int j=i;
				while (sorts[j]!=sorted[i])j++;
				sorts[j]=sorts[i];
				sorts[i]=sorted[i];
				total++;
			}
		}
		*/
		fout<<"Case #"<<h+1<<": "<<double(total)<<endl;

	}

	return 0;
}
