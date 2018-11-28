/*

  Adorjani Alpar
  Sapientia EMTE, 2008.jul

*/

#include <iostream>
#include <string>
using std::string;
using std::cin;
using std::cout;
using std::getline;


int N,S,Q;
string searcher[101];

int getord(string str)
{
	for(int i=0;i<S;i++)
	{
		if(searcher[i]==str)
			return i;
	}
	return -1;
}

void dolg()
{
	int i,j,k;
	int rem,o,sw;
	string str;
	int ord[101];
	getline(cin, str);
	N = atoi(str.c_str());
	for(i=1;i<=N;i++)
	{
		if(i>1)
			cout<<"\n";
		getline(cin, str);
		S = atoi(str.c_str());
		for(j=0;j<S;j++)
		{
			getline(cin, searcher[j]);
		}
		getline(cin, str);
		Q = atoi(str.c_str());
		rem = S;
		sw = 0;
		for(k=0;k<S;k++)
			ord[k]=0;
		for(j=0;j<Q;j++)
		{
			getline(cin, str);
			o = getord(str);
			if(!ord[o])
			{
				rem--;
				ord[o] = 1;
			}
			if(rem==0)
			{
				sw++;
				rem = S-1;
				for(k=0;k<S;k++)
					ord[k]=0;
				ord[o] = 1;
			}
		}
		cout<<"Case #"<<i<<": "<<sw;
	}
}

void main()
{
	dolg();
}
