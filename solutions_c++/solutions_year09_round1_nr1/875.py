#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <map>
#include <ctime>
#include <cmath>
using namespace std;

long transform(long num,int B)
{
	/*if (num!=0)
	{
	int k=num%B;
	num=num/B;
	transform(num,B);
	cout<<k;
	}*/
	//·ÇµÝ¹é
	int k;
	vector<int> v;//´æ·Åk;
	while (num!=0)
	{
		k=num%B;
		v.push_back(k);
		num/=B;
	}
	reverse(v.begin(),v.end());
	/*ostream_iterator<int> out(cout,"");
	copy(v.rbegin(),v.rend(),out);*/
	long sum=0;
	for (int i=0;i<v.size();++i)
	{
		sum=sum+v[i]*v[i];
	}
	return sum;
}

int main(int argc,char *argv[])
{
	ifstream in;
	ofstream out;
	in.open("A-small-attempt2.in");
	out.open("A-large.out");

	if (!in)
	{
		cerr<<"file open error!";
		return EXIT_FAILURE;
	}
	int T;
	in>>T;
	in.ignore(1,'\n');
	int icase=0;
	while (icase<T)
	{
		string str;
		getline(in,str);
		istringstream istr(str);
		int basenum=0;
		int base=0;
		vector<int> vbase;
		int mm=0;
		while (istr!=NULL)
		{
			istr>>base;
			if (mm==base)
			{
				break;
			}
			vbase.push_back(base);
			mm=base;
			basenum++;
		}
		istr.clear();

		int count=0;
		int j;
		for (j=2;;++j)
		{
			count=0;
			for (int i=0;i<basenum;++i)
			{
				long res = transform(j,vbase[i]);
				int cc=0;
				while (res!=1)
				{
					res=transform(res,vbase[i]);
					cc++;
					if (cc>20)
					{
						break;
					}
				}
				if (res==1)
				{
					count++;
				}
			}
			if (count==basenum)
			{
				break;
			}
		}

		icase++;
		out<<"Case #"<<icase<<": "<<j<<endl;
	}

	in.close();
	out.close();
	return 0;
}