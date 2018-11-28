#include <cstdio>
#include <sstream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

vector<int> hist;
vector<int>::iterator it;
vector<int> r;

int find(int B,int A,string str)
{
	hist.clear();
	int len=str.length();
	int len2=1;
	int count=0;

	for(int i=len-1;i>=1;i--)
	{
		string end=str.substr(i,len2);
		string start=str.substr(0,i);
		string both=end+start;

		int m=atoi(both.c_str());
		int n=atoi(str.c_str());

		it=find(hist.begin(),hist.end(),m);
		if(end[0]!='0' && n<m && m<=B && it==hist.end())
		{
			count++;
			hist.push_back(m);
		}
		len2++;
	}

	return count;
}

int main()
{
	int A;
	int B;
	int count;
	int result;

	string buff;

	ifstream file;
	file.open("input.txt");

	getline(file,buff);
	count=atoi(buff.c_str());

	for(int i=0;i<count;i++)
	{
		result=0;

		getline(file,buff);
		sscanf_s(buff.c_str(),"%d %d",&A,&B);

		for(int q=A;q<=B;q++)
		{
			stringstream ss;
			ss.clear();
			ss<<q;
			result+=find(B,A,ss.str());
		}
		
		r.push_back(result);
		printf("Case #%d: %d\n",i+1,result);
	}

	file.close();

	ofstream out;
	out.open("output.txt");
	
	for(unsigned int i=0;i<r.size();i++)
	{
		out<<"Case #"<<(i+1)<<": "<<r[i]<<endl;
	}

	out.close();

	system("PAUSE");
	return 0;
}