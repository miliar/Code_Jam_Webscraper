#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const char in_name[]="B-large.in";
const char out_name[]="B.out";

int main()
{
	ifstream in(in_name);
	ofstream out(out_name);

	int test,i,j,k;
	int C,D,N;
	vector<pair<string,char> > cs;
	vector<string> ds;
	string res,search(3,'\0');
	char tmp;

	in>>test;
	for(i=0;i<test;i++)
	{	//input
		in>>C;
		cs.resize(C,pair<string,char>(string(3,'\0'),0));
		for(j=0;j<C;j++)
		{	in>>cs[j].first;
			cs[j].second=cs[j].first[2];
			cs[j].first.resize(2);
		}
		in>>D;
		ds.resize(D);
		for(j=0;j<D;j++)
			in>>ds[j];

		//чтение строки
		in>>N;
		res.clear();
		for(j=0;j<N;j++)
		{	in>>tmp;
			if(res.empty())
				res.push_back(tmp);
			else
			{	//слияние
				search[0]=res.back();
				search[1]=tmp;
				for(k=0;k<C;k++)
					if((cs[k].first[0]==search[0] && cs[k].first[1]==search[1]) || (cs[k].first[0]==search[1] && cs[k].first[1]==search[0]))
					{	res.back()=cs[k].second;
						goto Label1;
						break;
					}
				res.push_back(tmp);
				Label1:
				//разрушение
				for(k=0;k<D;k++)
					if((res.back()==ds[k][1] && res.find(ds[k][0])!=-1) || (res.back()==ds[k][0] && res.find(ds[k][1])!=-1))
					{	res.clear();
						break;
					}
			}
		}

		//output
		out<<"Case #"<<i+1<<": [";
		if(res.length()==0)
			out<<"]\n";
		else
		{	out<<res[0];
			for(k=1;k<res.length();k++)
				out<<", "<<res[k];
			out<<"]\n";
		}
	}

	in.close();
	out.close();
	return 0;
}