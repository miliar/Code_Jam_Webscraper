#include<stdio.h>
#include<map>
#include<string>

using namespace std;


int main()
{
	map <string,int> pathes;
	FILE *fin = fopen("INP.IN","r");
	FILE *fout = fopen("OUT.out","w");
	int t;
	fscanf(fin,"%d",&t);
	for(int x = 1; x <= t; x ++)
	{
		pathes.clear();
		int counter = 0;
		int found,wanted;
		fscanf(fin,"%d %d\n",&found,&wanted);
		for(int i = 0; i < found;i++)
		{
			char path[102];
			fscanf(fin,"%s",path);
			string xx = path;
			int current = 1;
			while(true)
			{
				int nextpos = xx.find('/',current);
				if (nextpos == -1)
					break;
				pathes[xx.substr(0,nextpos)] = 1;
				current = nextpos + 1;
			}
			pathes[xx] = 1;
		}
		for(int i = 0 ; i < wanted;i++)
		{
			char path[102];
			fscanf(fin,"%s",path);
			string xx = path;
			int current = 1;
			while(true)
			{
				int nextpos = xx.find('/',current);
				if (nextpos == -1)
					break;
				string p = xx.substr(0,nextpos);
				if (pathes[p] == 0)
				{
					pathes[p] = 1;
					counter ++;
				}
				current = nextpos + 1;
			}
			if (pathes[xx] == 0)
			{
				pathes[xx] = 1;
				counter ++;
			}
		}
		fprintf(fout,"Case #%d: %d\n",x,counter);
	}
}
