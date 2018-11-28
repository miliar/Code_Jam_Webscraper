#include <fstream>
#include <vector>

using namespace std;

int n,m;
int REZ=0;

class nod
{
public:
	char* name;
	vector<nod*> children;
	nod(){
		name=new char[110];
	}
};

nod* root;

nod* createNod(char* name,nod* tata)
{
	nod* newnod = new nod();
	strcpy(newnod->name,name);
	tata->children.push_back(newnod);
	return newnod;
}

void parseNod(char* path)
{
	// /george/mere/mata
	int len = strlen(path);
	char dir[100];
	int dlen=0;
	nod* cnod=root;
	for(int i=1;i<len;i++)
	{
		bool done=false;
		if(path[i]!='/' && i<len-1)
		{
			dir[dlen]=path[i];
			dlen++;
		} else {
			if(i==len-1)
			{
				dir[dlen]=path[i];
				dlen++;
			}
			dir[dlen]=NULL;
			for(int y=0;y<cnod->children.size();y++)
			{
				if(strcmp(((nod*)cnod->children[y])->name,dir)==0)
				{
					//ffs, exista
					cnod = (nod*)cnod->children[y];
					done=true;
				} else {
					//cnod = createNod(path,cnod);
				}
			}
			if(!done)
			{
				cnod = createNod(dir,cnod);
			}
			done=false;
		}
		if(path[i]=='/')
		{
			dir[0]=NULL;dlen=0;
		}
	}
}

void parseNod2(char* path)
{
	int len = strlen(path);
	char dir[100];
	int dlen=0;
	nod* cnod=root;
	for(int i=1;i<len;i++)
	{
		bool done=false;
		if(path[i]!='/' && i<len-1)
		{
			dir[dlen]=path[i];
			dlen++;
		} else {
			if(i==len-1)
			{
				dir[dlen]=path[i];
				dlen++;
			}
			dir[dlen]=NULL;
			for(int y=0;y<cnod->children.size();y++)
			{
				if(strcmp(((nod*)cnod->children[y])->name,dir)==0)
				{
					//ffs, exista
					cnod = (nod*)cnod->children[y];
					done=true;
					y=99999;
				} else {
					//cnod = createNod(path,cnod);
				}
			}
			if(!done)
			{
				cnod = createNod(dir,cnod);
				REZ++;
			}
			done=false;
		}
		if(path[i]=='/')
		{
			dir[0]=NULL;dlen=0;
		}
	}
}

int main()
{
	ifstream f("A-small.in");
	ofstream f2("output.out");

	int T;
	f>>T;

	char path[255];

	for(int TEST=0;TEST<T;TEST++)
	{
		REZ=0;
		f>>n>>m;
		if(root)
			delete root;
		root = new nod();
		for(int i=0;i<n;i++)
		{
			f>>path;
			parseNod(path);
		}
		for(int i=0;i<m;i++)
		{
			f>>path;
			parseNod2(path);
		}
		f2<<"Case #"<<TEST+1<<": "<<REZ<<endl;
	}

	f.close();
	f2.close();
	return 0;
}