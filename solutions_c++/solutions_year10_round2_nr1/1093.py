#include<iostream>
#include<string>
#include<map>

using namespace std;

struct Directory
{
	map<string, Directory> subDirectories;
};

int parsePathnames(int const n, Directory & root)
{
	int newAdditions = 0;

	string path, dir;

	for(int i = 0; i < n; ++i)
	{
		getline(cin, path);

		Directory * current = &root;

		for(int j = 1; path[j] != '\0';)
		{
			dir.clear();

			do
			{
				dir += path[j];
				++j;
			}
			while(path[j] != '/' and path[j] != '\0');

			if(path[j] == '/')
				++j;

			map<string, Directory>::iterator subdir = current->subDirectories.find(dir);

			if(subdir == current->subDirectories.end())
			{
				current->subDirectories[dir] = Directory();
				++newAdditions;

				current = &current->subDirectories.find(dir)->second;
			}
			else
				current = &subdir->second;
		}
	}

	return newAdditions;
}

int main()
{
	int T;
	cin >> T;

	for(int x = 1; x <= T; ++x)
	{
		int N, M;
		cin >> N >> M;
		cin.get();

		Directory root;

		parsePathnames(N, root);

		cout << "Case #" << x << ": " << parsePathnames(M, root) << "\n";
	}

	return 0;
}