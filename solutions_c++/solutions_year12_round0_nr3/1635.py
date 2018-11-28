#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
using namespace std;
string its(long);
void main()
{
	ifstream fin("C-large.in");
	ofstream fout("output.txt");
	int cases;
	fin>>cases;
	for(int c=1;c<=cases;c++)
	{
	long a,b;
	fin>>a>>b;
	//cout<<a<<" "<<b;
	int count=0,temp=0,temp1=0;
	for(long n=a;n<b;n++)
	{
		string s=its(n);
		vector <long> v;
		for(int i=1;i<s.length();i++)
		{
			string t="";
			temp=0;
			int flag=0;
			t=s.substr(i);
			t=t+s.substr(0,i);
			temp=atol(t.c_str());
			if(temp>n && temp<=b)
			{
				for(vector<int>::size_type pos=0;pos<v.size();pos++)
				{
					if(temp==v[pos])
					{
						flag=1;
						break;
					}
				}
				if(flag==0)
				{
				count++;
				v.push_back(temp);
				}
			}

		}
		v.clear();
	}
	fout<<"Case #"<<c<<": "<<count<<"\n";
	}
	fout.close();
	fin.close();

}
string its(long i)
{
    std::stringstream ss;
    std::string s;
    ss << i;
    s = ss.str();

    return s;
}