#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
template<class T>
ostream& operator<<(ostream& out, const vector<T>& nums)
{
	out<<"[";
	for(vector<T>::const_iterator i=nums.begin(); i!=nums.end(); i++)
		out<<"\""<<(*i)<<"\""<<", ";
	out<<"]";
	return out;
}
typedef vector<int> ints;

int cj(const vector< pair<int, int> >& lines)
{

	int cross = 0;
	for (int i=0; i<lines.size(); i++)
	{
		for (int j=0; j<i; j++)
		{
			if ( (lines[i].first-lines[j].first) * (lines[i].second-lines[j].second) < 0)
				cross++;
		}
	}
	return cross;
}

int main()
{
	int T;
	cin>>T;
	int count=1;
	int N, a, b;
	vector< pair<int, int> > lines;
	for (; count<=T; count++)
	{
		cin>>N;
		lines.clear();
		for(int i=0; i<N; i++){
			cin>>a>>b;
			lines.push_back(pair<int, int>(a, b));
		}
		cout<<"Case #"<<(count)<<": "<<cj(lines)<<endl;
	}
	return 0;
}

