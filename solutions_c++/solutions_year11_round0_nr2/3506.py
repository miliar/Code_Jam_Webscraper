#include <fstream>
#include <cstdio>
#include <vector>
#define ms(a) memset(a,0,sizeof(a))
#define fori(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
int pairs[30][30];
int destr[30][30];

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int T,C,D,N,sz;
	in>>T;
	vector<int> seq;
	char l,r,p;
	fori(i,1,T)
	{
		ms(pairs);
		ms(destr);
		in>>C;
		fori(g,1,C)
		{
			in>>l>>r>>p;
			pairs[l-'A'+1][r-'A'+1]=p-'A'+1;
			pairs[r-'A'+1][l-'A'+1]=p-'A'+1;
		}
		in>>D;
		fori(g,1,D)
		{
			in>>l>>r;
			destr[l-'A'+1][r-'A'+1]=1;
			destr[r-'A'+1][l-'A'+1]=1;
		}
		in>>N;
		fori(g,1,N)
		{
			in>>l;
			seq.push_back(l-'A'+1);
			sz=seq.size();
			if(sz>1)
				if(pairs[seq[sz-2]][seq[sz-1]])
					seq[sz-2]=pairs[seq[sz-2]][seq[sz-1]],sz--,seq.pop_back();
			for(int j=sz-2;j>=0;j--)
				if(destr[seq[j]][seq[sz-1]]==1)
				{
					seq.clear();
					break;
				}
		}
		out<<"Case #"<<i<<": "<<'[';
		if(!seq.empty())
		{
			for(int f=0;f<seq.size()-1;f++)
				out<<(char)(seq[f]+'A'-1)<<", ";
		}
		if(!seq.empty())
			out<<(char)(seq[seq.size()-1]+'A'-1);
		out<<']'<<endl;
		seq.clear();
	}
	return 0;
}