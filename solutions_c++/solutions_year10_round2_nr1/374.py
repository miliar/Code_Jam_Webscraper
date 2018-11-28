#include <iostream>
#include <map>
using namespace std;

void add_existents(map<string, bool> &paths, string path)
{
	for(size_t i = 1; i < path.size(); i++)
	{
		if(path[i] == '/') paths[path.substr(0, i)] = true;
	}
	
	paths[path] = true;
}

int count_mkdir(map<string, bool> &paths, string path)
{
	int count = 0;
	
	for(size_t i = 1; i < path.size(); i++)
	{
		if(path[i] == '/' && !paths[path.substr(0, i)])
		{
			count++;
			paths[path.substr(0, i)] = true;
		}
	}
	
	if(!paths[path])
	{
		count++;
		paths[path] = true;
	}
	
	return count;
}

int main(void)
{
	int T, N, M;
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++)
	{
		map<string, bool> paths;
		int total = 0;
		
		cin >> N >> M;
		
		paths["/"] = true;
		for(int i = 1; i <= N; i++)
		{
			string p;
			
			cin >> p;
			add_existents(paths, p);
		}
		
		for(int i = 1; i <= M; i++)
		{
			string p;
			
			cin >> p;
			total += count_mkdir(paths, p);
		}
		
		cout << "Case #" << numCase << ": " << total << endl;
	}
}		
