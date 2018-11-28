#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

class dir
{
public:
	string nume;
	vector<dir> kids;
	
	bool operator == (dir f)
	{
		return nume.compare(f.nume);
	}
};

int main(int argc, char** argv)
{
	int t;
	FILE *f = fopen(argv[1], "rt");
	fscanf(f, "%d", &t);
	int crt = 0;
	
	while(crt<t)
	{
		int n,m;
		fscanf(f, "%i %i\n", &n, &m);
		
		dir root;
		root.nume = "root";
		
		int ret = 0;
		
		while(n)
		{
			char buffer[105];
			fgets(buffer, 103, f);
			int k = strlen(buffer);
			
			buffer[k-1] = '/', buffer[k] = 0;
			
			char* p = strchr(buffer, '/');
			
			dir* last = &root;
			char* q = buffer;
			
			while(p)
			{
				*p = 0;
				
				string temp = q;
				if (temp.size() == 0)
				{
					q = p+1;
					p = strchr(q, '/');
					continue;
				}				
				
				bool ala = false;	
				unsigned int i;
				for (i=0;i<(*last).kids.size();i++)
				{
					if ((*last).kids[i].nume == temp)
					{
						last = &last->kids[i];
						ala = true;
						break;
					}
				}
				
				if (!ala)
				{
					dir newdir;
					newdir.nume = temp.c_str();
					//printf("Folder nou: %s\n", temp.data());
					(*last).kids.push_back(newdir);
					last = &(last->kids[last->kids.size()-1]);
				}
				
				q = p+1;
				p = strchr(q, '/');
			}
			n--;
		}
		
		/*if (root.kids.size() > 0)
		for (int i=0;i<root.kids[0].kids.size();i++)
		{
			printf("folder %i: %s\n", i, root.kids[0].kids[i].nume.c_str());
		}*/
		
		while(m)
		{
			char buffer[105];
			fgets(buffer, 103, f);
			int k = strlen(buffer);
			
			buffer[k-1] = '/', buffer[k] = 0;
			
			char* p = strchr(buffer, '/');
			
			dir* last = &root;
			char* q = buffer;
			
			while(p)
			{
				*p = 0;
				
				string temp = q;
				if (temp.size() == 0)
				{
					q = p+1;
					p = strchr(q, '/');
					continue;
				}
				
				bool ala = false;
				unsigned int i;
				for (i=0;i<(*last).kids.size();i++)
				{
					//printf("%s %s %s\n\n", (*last).nume.data(), (*last).kids[i].nume.data(), temp.data());
					if ((*last).kids[i].nume == temp)
					{
						last = &last->kids[i];
						ala = true;
						break;
					}
				}
				
				if (!ala)
				{
					dir newdir;
					newdir.nume = temp.data();
					//printf("Folder nou: %s\n", temp.data());
					(*last).kids.push_back(newdir);
					last = &(last->kids[last->kids.size()-1]);
					ret ++;
				}
				
				q = p+1;
				p = strchr(q, '/');
			}
			m--;
		}
		/*for (int i=0;i<root.kids[0].kids.size();i++)
		{
			printf("folder %i: %s\n", i, root.kids[0].kids[i].nume.data());
		}*/
		printf("Case #%i: %i\n", ++crt, ret);
		//crt++;
	}
	
	return 0;
}
