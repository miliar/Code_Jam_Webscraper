#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;



string szinput = "C-small-attempt1.in";
//string szinput = "../test.txt";
//string szinput = "../A-large-practice.in";
string szoutput = "../output.txt";

int tentimes(int n)
{
	int ret = 1;
	for(int i=1;i<n;i++)
		ret = ret*10;
	return ret;
}

int main()
{

	int T;

	ifstream in;
	in.open(szinput);

	ofstream out;
	out.open(szoutput,ios::out);

	in>>T;
	in.ignore(100,'\n');

	for(int i=0;i<T;i++)
	{
		int A,B;
		in>>A>>B;
		in.ignore(100,'\n');

		int len=0;
		int temp = A;
		while(true)
		{
			temp=temp/10;
			len++;
			if(temp==0)
				break;
		}

		int counter=0;
		if(len==1)
		{
			out<<"Case #"<<i+1<<": "<<counter<<endl;
			continue;
		}
		
		for(int j=A;j<B;j++)
		{
			vector<int> digits;
			int n = j;
			for(int k=0;k<len;k++)
			{
				digits.push_back(n%10);
				n=n/10;
			}
			reverse(digits.begin(),digits.end());
			
			set<int> mset;
			for(int k=0;k<len-1;k++)
			{
				int rd = len-1-k;
				int c = len;
				int m = 0;
				do
				{
					m = m+digits[(len - rd)%len]*(tentimes(c));
					rd--;
					c--;
				}while(c>0);
				if(m>j && m<=B && mset.find(m)==mset.end())
				{
					mset.insert(m);
					counter++;
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<counter<<endl;
		
	}
	return 1;
}