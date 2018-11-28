#include <fstream>
#include <set>
using namespace std;

int main()
{
	ofstream out("out.txt");
	ifstream in("in.txt");
	int t;
	in>>t;
	
	for(int i=1; i<=t; i++)
	{
		set<long> s;
		int a,b;
		in>>a>>b;
		int numdigits =0;
		int tmp = a;
		while(tmp)
		{
			tmp  /= 10;
			numdigits++;
		}
		//int count = 0;
		for(int j=a; j<b; j++)
		{
			for(int k=1; k<numdigits; k++)
			{
				int mul = (int)powf(10, k);
				int xmul = (int)powf(10, (numdigits-k));
				int newJ = ((j%mul)*xmul)+j/mul;
				if(newJ > j && newJ <= b)
				{	
					s.insert(j*(int)powf(10,numdigits)+newJ);
				}
			}
		}
		out<<"Case #"<<i<<": "<<s.size()<<endl;
	}

	in.close();
	out.close();
}