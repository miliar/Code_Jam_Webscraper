#include <string>
#include <fstream>
#include <set>

using namespace std;

int main()
{
	ifstream IFile("A-large.in");
	ofstream OUTFile("result.in");
	int Num;
	IFile>>Num;
	int i,j,k,l,m,n;
	set<string> oriStrSet;
	set<string> objStrSet;
	for (i=0;i<Num;++i)
	{
		int N,M;
		if(IFile>>N>>M)
		{
			oriStrSet.clear();
			objStrSet.clear();
			for (j=0;j<N;++j)
			{
				string str,s;
				IFile>>str;
				for (l=1;l<str.size();++l)
				{
					if (str[l] != '/')
					{
						s += str[l];
					}
					else
					{
						oriStrSet.insert(s);
						s += '/';
					}
				}
				oriStrSet.insert(s);
			}
			for (k=0;k<M;++k)
			{
				string str,s;
				IFile>>str;
				for (j=1;j<str.size();++j)
				{
					if (str[j] != '/')
					{
						s += str[j];
					}
					else
					{
						objStrSet.insert(s);
						s += '/';
					}
				}
				objStrSet.insert(s);
			}

			int oriSize = 0;
			set<string>::const_iterator it = oriStrSet.begin();
			for (;it != oriStrSet.end();++it)
			{
				if (objStrSet.count(*it) == 1)
				{
					++oriSize;
				}
			}
			OUTFile<<"Case #"<<i + 1<<": "<<objStrSet.size()-oriSize<<endl;


		}
	}
	return 0;
}