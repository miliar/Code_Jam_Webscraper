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

#define  SEP ('/')

typedef vector<string> strings;

struct Path
{
	Path(const string& s):_name(s) {
		int begin=0;
		int cur=0;
		for (;cur<s.length(); cur++){
			if (s[cur]==SEP){
				string temp = s.substr(begin, cur-begin);
				_disposed.push_back(temp);
				begin = cur+1;
			}
		}
		_disposed.push_back(s.substr(begin, cur-begin));
		//cout<<"disposed:"<<_disposed<<endl;
	}
	Path(const strings& subs):_disposed(subs){
		//_name = SEP;
		for (int i=1; i<subs.size(); i++)
		{
			_name+=SEP;
			_name+=subs[i];
		}
		//cout<<"create:"<<_name<<endl;
	}
	int length(){return _disposed.size();};
	Path sub_Path(const int sub_size){
		if (sub_size==1)
			return Path("/");
		string new_name;
		for (int i=1; i<sub_size; i++)
		{
			new_name+=SEP;
			new_name+=_disposed[i];
		}
		return Path(new_name);
	}
	string _name;
	vector<string> _disposed;
};

void output_paths(vector<Path>& paths)
{
	cout<<"{"<<endl;
	for (int j=0; j<paths.size(); j++)
	{
		cout<<paths[j]._name<<endl;
	}
	cout<<"}"<<endl;
}

void sort_paths(vector<Path>& paths)
{
	if (paths.size()==0)
		return;
	for (int i=0; i<paths.size()-1; i++)
		for (int j=i+1; j<paths.size(); j++)
		{
			if (paths[i].length()>paths[j].length())
				swap(paths[i], paths[j]);
		}
}
bool in_paths(vector<Path>& paths, Path& find_p)
{
	for (int i=0; i<paths.size(); i++)
	{
		if (paths[i]._name==find_p._name)
			return true;
	}
	return false;
}

int cj(vector<string>& Ns, vector<string>& Ms)//N´æÔÚ
{
	vector<Path> MPs, NPs;
	for(strings::const_iterator i=Ms.begin(); i!=Ms.end(); i++){
		MPs.push_back(Path(*i));
	}
	for(strings::const_iterator i=Ns.begin(); i!=Ns.end(); i++){
		NPs.push_back(Path(*i));
	}
	NPs.push_back(Path("/"));
	//output_paths(MPs);
	sort_paths(MPs);
	//output_paths(MPs);
	//
	//output_paths(NPs);
	//sort_paths(NPs);
	//output_paths(NPs);

	int create = 0;
	for(int i=0; i<MPs.size(); i++)
	{
		if (in_paths(NPs, MPs[i])){
			continue;
		}
		for (int j=1; j<=MPs[i]._disposed.size(); j++)
		{
			Path temp=MPs[i].sub_Path(j);
			if (in_paths(NPs, temp))
				continue;
			create++;
			//cout<<temp._name<<endl;
			NPs.push_back(temp);
		}
	}

	return create;
}

int main()
{
	int C;
	cin>>C;
	int count=1;
	int N, M;
	vector<string> Ns;
	vector<string> Ms;
	string temp;
	for (; count<=C; count++)
	{
		Ns.clear();
		Ms.clear();
		cin>>N>>M;
		for (int i=0; i<N; i++){
			cin>>temp;
			Ns.push_back(temp);
		}
		for (int j=0; j<M; j++){
			cin>>temp;
			Ms.push_back(temp);
		}
		cout<<"Case #"<<(count)<<": "<<cj(Ns, Ms)<<endl;
	}
	return 0;
}

