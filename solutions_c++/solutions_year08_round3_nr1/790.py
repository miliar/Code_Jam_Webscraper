#include "iostream"
#include "fstream"
#include "vector"
#include "algorithm"
using namespace std;

int main()
{
	ifstream ifile("d:\\in.txt");
	ofstream ofile("d:\\out.txt");
	int n,p,k,l;
	int nf;
	int base;
	int count;
	int res;
	int num=1;
	vector<int> fre;
	ifile>>n;
	while (n)
	{
		fre.clear();
		ifile>>p>>k>>l;
		while (l)
		{
			ifile>>nf;
			fre.push_back(nf);
			l--;
		}
		sort(fre.begin(),fre.end());
		count=fre.size();
		res=0;
		base=1;
		for (int i=0;i<count;i++)
		{
			res+=base*fre[count-i-1];
			if((i+1)%k==0)
				base++;
		}
		ofile<<"Case #"<<num<<": "<<res<<endl;
		num++;
		n--;
	}
	return 1;
}