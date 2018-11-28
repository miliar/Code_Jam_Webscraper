using namespace std;

#include <sstream>
#include<iostream>
#include<fstream>
#include<map>
#include<string>
#include<algorithm>

string NumberToString ( int Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}

int StringtoNumber (string Number)
{
	int num;
	istringstream(Number)>>num;
	return num;
}

int recycled_numbers(int a, int b)
{
	int num[2000001], n, k, res=0;
	for(int i=a; i<= b;i++) 
		num[i] = 0;
	for(int i=a; i<=b; i++)
	{
		if(num[i]) continue;
		num[i]=1;
		if(i < 10) continue;
		string s=NumberToString(i);
		n=i;
		k=1;
		do
		{
			rotate(s.begin(), s.begin()+1, s.end());
			n=StringtoNumber(s);
			if(n >= a && n <=b && n != i) 
			{
				num[n]=1;
				k++;
			}
		} while(n != i);
		res += k*(k-1)/2;
	}
	return res;
}

int main()
{
	ofstream fout ("recycled.out");
	ifstream fin ("recycled.in");
	int T;
	fin>>T;
	for(int i=0; i < T; i++)
	{
		int a,b,res;
		fin>>a>>b;
		res=recycled_numbers(a,b);
		fout<< "Case #" << i+1 << ": " << res << endl;
	}
	return 0;
}
