#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	fstream in("a.in");
	ofstream out("a.out");
	int N=0;
	in>>N;
	int i,j;
	for (i = 0; i<N; i++)
	{
		int S=0;
		in>>S;
		vector<string> strVec;
		for (j=0;j<S; j++)
		{
			string temp="";
			while (temp=="")
			{
				getline(in,temp);
			}
			strVec.push_back(temp);
		}
		int Q;
		in>>Q;
		vector<string> qVec;
		for (j=0;j<Q; j++)
		{
			string temp="";
			while (temp=="")
			{
				getline(in,temp);
			}
			qVec.push_back(temp);
		}
// 		for (j=0; j<qVec.size();j++)
// 		{
// 			cout<<qVec[j]<<endl;
// 		}
		int nReturn=-1;
		int nCnt=0;
		for (j=0;j<Q;j=nCnt,nReturn++)
		{
			nCnt = 0;
			for (int k=0;k<S;k++)
			{
				for (int l=j;l<Q;l++)
				{
					if (strVec[k]==qVec[l])
						break;
				}
				if (l>nCnt)
				{
					nCnt=l;
				}
			}
		}
		if (nReturn<0)
		{
			nReturn=0;
		}
/*		cout<<nReturn<<endl;*/
		out<<"Case #"<<i+1<<": "<<nReturn<<endl;
	}
}