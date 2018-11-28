#include <vector>
#include <iostream>

using namespace std;

unsigned int num_mot;
unsigned int num_query;

unsigned int actual_min=~0;

vector<unsigned int> mot;

unsigned int solve(unsigned int start)
{
	int max=0;
	for(int i=0;i<num_mot;i++)
	{
		int u=0;
		int j;
		for(j=start;j<num_query;j++)
		{
			if(mot[j]==i+1)
			{
				u=j;
				break;
			}
		}
		if(j==num_query)
			return 1;
		if(u>max)
			max=u;
	}
	return solve(max)+1;
}

class names
{
public:
	char name[101];
	bool operator==(const names& n)
	{
		return !strcmp(name,n.name);
	}
};

int main(int argc, char* argv[])
{
	FILE* f=fopen(argv[1],"r");

	unsigned int cases;
	fscanf(f,"%u\n",&cases);

	for(int c=0;c<cases;c++)
	{
		if(c==cases-1)
			char a=0;
		//unsigned int num_mot;
		fscanf(f,"%u\n",&num_mot);
		vector<names> eng(num_mot);
		for(int e=0;e<num_mot;e++)
		{
			fgets(eng[e].name,100,f);
			eng[e].name[strlen(eng[e].name)-1]=0;
			//cout << eng[e].name << endl;
		}
		//unsigned int num_query;
		fscanf(f,"%u\n",&num_query);
		//cout << "NQ " << num_query << endl;
		vector<unsigned int> mot;
		for(int q=0;q<num_query;q++)
		{
			names n;
			fgets(n.name,100,f);
			n.name[strlen(n.name)-1]=0;
			vector<names>::iterator it=find(eng.begin(),eng.end(),n);
			mot.push_back(it-eng.begin()+1);
		}

		::mot=mot;
		unsigned int min=solve(0)-1;
		cout << "Case #" << c+1 << ": " << min << endl;
	}
}
