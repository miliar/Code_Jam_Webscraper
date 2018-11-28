#include<fstream>
#include<vector>
#include<string>
using namespace std;
int decode(string s,char base);
int main()
{
	ifstream in("a.in");
	ofstream out("a.out");
	int notc;
	in>>notc;
for(int y=1;y<=notc;y++)
{
	string s;
	string s2;
	vector<char> v;
	int counter = '1';
	in>>s;
	for(int i=0;i<37;i++)
	{
		v.push_back('-');
	}
	for(int i=0;i<s.size();i++)
	{
		if(isdigit(s[i]) )
		{
			if(v[s[i]-'0']=='-')
			{
				v[s[i]-'0']=counter;
				s2.push_back(counter);
				if(counter=='9')
				{
					counter='a';
				}
				else if(counter=='1')
				{
					counter='0';
				}
				else if (counter =='0')
				{
					counter='2';
				}
				else
					counter++;
			}
			else
			{
				s2.push_back(v[s[i]-'0']);
			}
		}
		else
		{
			if(v[s[i]-'a'+10]=='-')
			{
				v[s[i]-'a'+10]=counter;
				s2.push_back(counter);
				if(counter=='9')
				{
					counter='a';
				}
				else if(counter=='1')
				{
					counter='0';
				}
				else if (counter =='0')
				{
					counter='2';
				}
				else
					counter++;
			}
			else
			{
				s2.push_back(v[s[i]-'a'+10]);
			}
		}
	}
//	cout<<s2<<endl;
	//else if(counter)
	out<<"Case #"<<y<<": "<<decode(s2,counter)<<endl;
}
in.close();
out.close();
}
int decode(string s,char base)
{
	int iBase;
	if(isdigit(base))
		iBase=base-'0';
	else
		iBase=base-'a'+10;
	if(iBase==0||iBase==1)
		iBase=2;
	unsigned long value=0,multiplier=1;
	for(int i=s.size()-1;i>=0;i--)
	{
		unsigned long z;
		if(isdigit(s[i]))
			z=s[i]-'0';
		else
			z=s[i]-'a'+10;
		value+=z*multiplier;
		multiplier*=iBase;
	}
	return value;
}