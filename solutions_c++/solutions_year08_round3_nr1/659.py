
#include <fstream>
#include <algorithm>
#include <vector>


using namespace std;


int main()
{
	ifstream ifile;
	ofstream ofile;
	
	
	ifile.open("A-small-attempt0.in");
	ofile.open("A.out");

	int T;
	ifile>>T;

	for(int i=0; i<T; i++)
	{
		int P=0;
		int K=0;
		int L =0;
		ifile>>P>>K>>L;

		vector<int> Lp(L);

		for(int j=0; j<L; j++)
			ifile>>Lp[j];
		
		sort(Lp.begin(), Lp.end());

		int rest= 0;

		int kk=0;
		for(int j=L-1; j>=0; j--)
		{
			rest+= Lp[j] *(kk/K +1);
			kk++;
		}

		ofile<<"Case #"<<i+1<<": "<<rest<<endl;
		
	}

	ifile.close();
	ofile.close();

}