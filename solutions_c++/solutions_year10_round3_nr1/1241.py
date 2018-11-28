#include <fstream>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

void solve(ifstream& ifile, ofstream& ofile, int t)
{
	int n;
	ifile >> n;
	vector<pair<int,int> > left;
	vector<pair<int,int> > right;
	vector<pair<int, int> > func;
	int cnt=0;
	for(int i=0;i<n;++i)
	{
		int l, r, s, c;
		ifile >> l;
		left.push_back(make_pair(0,l));
		ifile >> r;
		right.push_back(make_pair(1,r));
		s = r - l;
		c = l;
		func.push_back(make_pair(s,c));
	}
	for(int i=0;i<func.size();++i)
	{
		for(int j=i+1;j<func.size();++j)
		{
			if(func[i].first == func[j].first) continue;
			double t1 = func[j].second-func[i].second;
			double t2 = func[i].first-func[j].first;
			double x1 = t1 / t2;
			if(x1 < 1 && x1 > 0)
				cnt++;
		}
	}
	ofile << "Case #" << t+1 << ": " << cnt << endl;
	t++;
}

int main()
{
	ifstream ifile("a.txt");
	ofstream ofile("res.txt");
	int t;
	ifile >> t;
	for(int i=0;i<t;++i)
	{
		solve(ifile, ofile, i);
	}
	ifile.close();
	ofile.close();
	return 0;
}

