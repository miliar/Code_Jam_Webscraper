#include <iostream>
#include <fstream>

using namespace std;

ifstream ci("in");
ofstream co("out");

char s[5000],ch[2];
int count[19];
string str="welcome to code jam";
int N;

int main()
{
	ci>>N;
	ci.read(ch,1);
	for (int i=0;i<N;++i)
	{
		int k=0;
		ci.read(ch,1);
		s[k]=ch[0];
		while ((!ci.eof())&&(int(s[k])>=32))
		{
			++k;
			ci.read(ch,1);
			s[k]=ch[0];
		}
		if (ci.eof())
			++k;
		for (int j=0;j<19;++j)
			count[j]=0;
		for (int j=0;j<k;++j)
		{
			for (int w=18;w>-1;--w)
				if (str[w]==s[j])
					if (w!=0)
						count[w]=(count[w]+count[w-1])%1000;
					else
						count[w]=(count[w]+1)%1000;
		}
		co<<"Case #"<<i+1<<": ";
		if (count[18]<1000)
			co<<"0";
		if (count[18]<100)
			co<<"0";
		if (count[18]<10)
			co<<"0";
		co<<count[18];
		co<<endl;
	}
}