#include <iostream>
#include <list>

using namespace std;

struct folder {
	char *name;
	list<folder*> sub;
};

int T, N, M;
int C;

void insert_folder(folder *root, char *path)
{
	folder* current = root;
	char *part;

	part = strtok(path, "/");
	while(part != NULL)
	{

	folder* y = new folder;
	y = 0;

	for(list<folder*>::iterator x=current->sub.begin(); x !=current->sub.end(); ++x)
	{
		if(strcmp((*x)->name, part) == 0) y = (*x);
	}

	if(y == 0)
	{
		C++;
		y = new folder;
		y->name = part;
		current->sub.push_back(y);
	}

	current = y;

	part = strtok(NULL, "/");
	}
}

void main()
{
	folder *root;
	FILE *input;
	char *f=new char[2555];

	input = fopen("C:\\1.in", "r");

	fscanf(input, "%u", &T);

	for(int i=1; i<=T; i++)
	{
		root = new folder;
		fscanf(input, "%u %u", &N, &M);
		for(int j=0; j<N; j++)
		{
			fscanf(input, "%s", f);
			insert_folder(root, f);
			f = new char[2555];
		}
		C = 0;
		for(int j=0; j<M; j++)
		{
			fscanf(input, "%s", f);
			insert_folder(root, f);
			f = new char[2555];
		}
		cout << "Case #" << i << ": " << C << "\n";
	}

	fclose(input);
}