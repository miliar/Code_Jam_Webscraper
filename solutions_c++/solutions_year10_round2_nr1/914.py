/*
using boost 1.42
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <boost/shared_ptr.hpp>
#include <boost/foreach.hpp>
#include <boost/tokenizer.hpp>

using namespace std;
using namespace boost;

#define metafor(it, v) for ( it = v.begin(); it != v.end(); it++ )

class FS
{
public:
	map<string, shared_ptr<FS> > directories;
};

void ReadFS( int N, ifstream &in, shared_ptr<FS> root )
{
	for(int i=0; i<N; i++)
	{
		string dir;
		getline(in, dir);
		char_separator<char> sep("/");
		tokenizer<char_separator<char>> tokens(dir, sep);
		shared_ptr<FS> curr = root;
		BOOST_FOREACH(string d, tokens)
		{
			if ( curr->directories.find(d) == curr->directories.end())
			{
				curr->directories[d].reset(new FS);
			}
			curr = curr->directories[d];
		}
	}
}

int CountMkdirs( shared_ptr<FS> root, shared_ptr<FS> requested )
{
	queue<pair< shared_ptr<FS>, shared_ptr<FS> > > toCreate;
	toCreate.push(make_pair(root,requested));
	int mkdirs = 0;
	while (!toCreate.empty())
	{
		shared_ptr<FS> pRealDir = toCreate.front().first;
		shared_ptr<FS> pCreateDir = toCreate.front().second;
		map<string, shared_ptr<FS> >::iterator it;
		metafor(it, pCreateDir->directories)
		{
			if ( pRealDir->directories.find(it->first) == pRealDir->directories.end())
			{
				pRealDir->directories[it->first].reset(new FS);
				mkdirs++;
			}
			toCreate.push(make_pair(pRealDir->directories[it->first],it->second));
		}
		toCreate.pop();
	}
	return mkdirs;
}
int main()
{
	ifstream in("C:\\Users\\German\\Documents\\Visual Studio 2005\\Projects\\Problemas\\A-large.in");
	//ifstream in("sample.in");
	ofstream out("C:\\Users\\German\\Documents\\Visual Studio 2005\\Projects\\Problemas\\sol.out");
	int T;
	in >> T;
	for(int t=1; t<=T; t++)
	{
		shared_ptr<FS> root(new FS);
		shared_ptr<FS> requested(new FS);
		int N, M;
		in >> N >> M;
		getline(in, string());
		ReadFS(N, in, root);
		ReadFS(M, in, requested);
		int mkdirs = CountMkdirs(root, requested);
		out << "Case #" << t << ": " << mkdirs << endl;
		cout << "Case #" << t << ": " << mkdirs << endl;
	}

	system("pause");
	return 0;
}
