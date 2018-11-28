#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

struct num
{
	long int number;
	int merge;
	num() { merge = 0; }
} tmpnum;

bool IsPrime(long int num)
{
	long int i;
	for(i = 2; i <= sqrt(num); i++)
		if(num % i == 0)
			return false;
	return true;
}
  
int main()
{
	ifstream infile("B-small-attempt2.in");
	ofstream outfile("output.txt");

	int count,i;
	long int a,b,p;
	long int j,k,res,pcount,mergeindex,tmp;
	vector<num> setlist;
	
	infile >> count;
	cout << "Number of sets: " << count << endl;
	for (i=0; i<count;i++)
	{
		cout << "Set " << i + 1 << " Started !" << endl;
		infile >> a >> b >> p;
		res = 0;
		setlist.clear();
		for (j=a; j<=b; j++)
		{
			tmpnum.number = j;
			setlist.push_back(tmpnum);
		}
		mergeindex = 1;
		for (;p<b;p++)
		{
			cout << "p: " << p << endl;
			if (!IsPrime(p))
				continue;
			pcount = -1;
			for (j=0; j<setlist.size(); j++)
			{
				if (setlist[j].number % p == 0)
					if (pcount == -1)
						pcount = j;
					else if (pcount == -2)
					{
						if (setlist[j].merge > 0)
						{
							tmp = setlist[j].merge;
							for (k=setlist.size()-1;k>=0;k--)
								if (setlist[k].merge == tmp)
									setlist[k].merge = mergeindex;
						}
						setlist[j].merge = mergeindex;
					}
					else
					{
						if (setlist[j].merge > 0)
						{
							tmp = setlist[j].merge;
							for (k=setlist.size()-1;k>=0;k--)
								if (setlist[k].merge == tmp)
									setlist[k].merge = mergeindex;
						}
						if (setlist[pcount].merge > 0)
						{
							tmp = setlist[pcount].merge;
							for (k=setlist.size()-1;k>=0;k--)
								if (setlist[k].merge == tmp)
									setlist[k].merge = mergeindex;
						}
						
						setlist[j].merge = mergeindex;
						setlist[pcount].merge = mergeindex;
						pcount = -2;
					}
			}
			mergeindex++;
		}
		for (j=0; j<setlist.size(); j++)
			if (setlist[j].merge==0)
				res++;
		for (j=1; j<=setlist.size(); j++)
			for (k=0; k<setlist.size(); k++)
				if (setlist[k].merge == j)
				{
					res++;
					break;
				}
		outfile << "Case #" << i+1 << ": " << res << endl;
		for (j=0; j<setlist.size(); j++)
			cout << setlist[j].number << "\t" << setlist[j].merge << endl;

	}

	infile.close();
	outfile.close();
}
