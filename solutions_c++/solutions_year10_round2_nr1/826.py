#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

set<string> exist;
vector<string> makeup;

void splitpath(string path, string &parent, string name)
{
	parent = path.substr(0, path.find_last_of('/'));
	name = path.substr(path.find_last_of('/')+1);

	//cout<<parent<<" "<<name<<endl;
}

int main()
{
	int T, N, M, i, j;
	string str, parent, name;

	cin>>T;
	for (i = 1; i <= T; i++) {
		cin>>N>>M;
		for (j = 0; j < N; j++) {
			cin>>str;
			exist.insert(str);
		}

		for (j = 0; j < M; j++) {
			cin>>str;
			makeup.push_back(str);
		}

		sort(makeup.begin(), makeup.end());

		int res = 0;
		for (j = 0; j < M; j++) {
			//cout<<makeup[j]<<endl;
			if (exist.find(makeup[j]) != exist.end()) {
				continue;
			}
			exist.insert(makeup[j]);
			//cout<<"insert "<<makeup[j]<<endl;
			res++;
			splitpath(makeup[j], parent, name);
			while (parent != "" && exist.find(parent) == exist.end()) {
				exist.insert(parent);
				//cout<<"insert "<<parent<<endl;
				res++;
				splitpath(parent, parent, name);
			}
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
		exist.clear();
		makeup.clear();
	}
	return 0;
}
