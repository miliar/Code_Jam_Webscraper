#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;
int main()
{
	int n;
	ifstream fin("inputl.in");
	ofstream fout("output.txt");
	fin >> n;
	char hz[10];
	fin.getline(hz,sizeof(hz));
	for(int cases=1;cases<=n;cases++)
	{
		string nr;
		getline(fin,nr);
		vector <char> left;
		char max='0';
		int i;
		int coef=0;
		bool trebu=true;
		for(i=nr.length()-1;i>=0;i--)
		{
			if (nr[i]>=max)
			{
				max=nr[i];
				coef=i;
				left.push_back(nr[i]);
			}
			else
			{
				trebu=false;
				break;
			}
		}
		if (!trebu)
		{
			for(int j=i+1;j<nr.length();j++)
			{
				if ((nr[j]>nr[i])&&(nr[j]<max))
				{
					max=nr[j];
					coef=j;
				}
			}
		
		for(int j=0;j<left.size();j++)
			if (left[j]==nr[coef])
			{
				left[j]=nr[i];
				break;
			}
		nr[i]=nr[coef];
		}
		if (trebu)
		{
			for(int j=0;j<left.size();j++)
				if ((left[j]>'0')&&(left[j]<=max)) 
				{
					max=left[j];
					coef=j;
				}
			i=0;
			nr[0]=max;
			left[coef]='0';
		}
		sort(left.begin(),left.end());
		for(int j=i+1;j<nr.size();j++)
			nr[j]=left[j-i-1];
		int siz=nr.length();
		string c="";		
		if (trebu)
		{
			c=left[left.size()-1];
		}
		fout << "Case #" <<cases <<": " << nr << c <<"\n";
	}
	return 0;
}