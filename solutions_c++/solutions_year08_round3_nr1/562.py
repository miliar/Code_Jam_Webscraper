//Visual Studio 2008 
#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<list>
#include<math.h>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cmath>

#define PI 3.1415926535897932384626433832795

using namespace std;
template<class TemplateClass>
TemplateClass SumItemsIn(TemplateClass* x,unsigned int y)
{
	TemplateClass Answer=0;
	for(unsigned int temp=0;temp<y;temp++) 
		Answer+=x[temp];
	return Answer;
}

//////////////////////////////////


void main()
{
	ifstream inFile("in.in",ios::in);
	ofstream outFile("out.out",ios::out);
	long long T=0;
	inFile>>T;
	for(long long Case=1;Case<=T;Case++)
	{
		long long MaxLetter=0,keysava=0,alphaletters=0;
		inFile>>MaxLetter>>keysava>>alphaletters;
		vector<long long> Frequ(alphaletters);
		for (long long i=0;i<alphaletters;i++)
		{
			inFile>>Frequ[i];
		}
		sort(Frequ.begin(),Frequ.end());
		reverse(Frequ.begin(),Frequ.end());
		long long answer=0;
		for (long long i=0;i<alphaletters;i++)
		{
			answer+=Frequ[i]*(1+(i/keysava));
		}
		outFile<<"Case #"<<Case<<": "<<answer<<endl;
	}
	inFile.close();
	outFile.close();
}
