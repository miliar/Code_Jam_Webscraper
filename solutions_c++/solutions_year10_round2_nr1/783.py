
// (c) Alvaro Salmador 2010

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>

using namespace std;

int N=0,M=0;

class dir
{
public:
	dir()
	{
	}

	int addDir(char* path)
	{
		//int cost;
		int len=strlen(path);
		//char* str = path;

//		fprintf(stderr, "adding %s\n",path);

		if (len==0) {
//			fprintf(stderr, "\n\n");
			return 0;}

		for(int i=0; i<len; ++i)
			if (path[i]=='/' || path[i]=='\n'|| path[i]=='\r')
			{
				if (path[i]=='\n'|| path[i]=='\r')
					path[i+1]=0;
				path[i]=0;
				//if (path[0]==0) {fprintf("\n\n\n");return 0;}
				map<string,dir*>::iterator I =hashmap.find((string)path);
				if (I!=hashmap.end()) {
//					fprintf(stderr, "<rec create %s>", path, path+i+1);
					return I->second->addDir(path+i+1);
				}
				else {
//					fprintf(stderr, "<created %s>", path);
					hashmap[(string)path] = new dir();
					return 1 + hashmap[(string)path]->addDir(path+i+1);
				}
			}
		if (strlen(path)>0) {
//			fprintf(stderr, "<*created %s>\n\n", path);
			return 1;
		}
		else { 
//			fprintf(stderr,"\n\n");
		return 0;}
	}

	//void

	map<string, dir*> hashmap;

};

dir root;
char buffer[200];

int cost;

bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		root.hashmap.clear();

		if (scanf("%d %d", &N, &M)!=2)
			return false;

		while(fgetc(stdin)!='\n') ;

		int i;
		for(i=0; i<N; ++i)
		{
			fgets(buffer, 199, stdin);

			root.addDir(buffer+1);

//			fprintf(stderr, "\n");
		}

//			fprintf(stderr, "-----\n");
		for(i=0; i<M; ++i)
		{
			fgets(buffer, 199, stdin);

			cost += root.addDir(buffer+1);
//			fprintf(stderr, "\n");
		}

		return true;
	}
	else
		return false;
}


int main()
{
	cost = 0;

	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		printf("Case #%d: %d\n", ncase, cost);
		cost = 0;

	}

	return 0;
}