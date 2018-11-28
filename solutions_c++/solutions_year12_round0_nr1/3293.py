#include<fstream>
#include<string.h>
#define dmax 103
using namespace std;
ifstream in("googlerese.in");
ofstream out("googlerese.out");

const char map[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
					 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

void translate(char* str, int index)
{
	char x[dmax];

	int l = strlen(str);
	
	for(int i=0; i<l; i++)
	{
		if(str[i] >= 'a' && str[i] <= 'z')
		{
			x[i] = map[str[i]-'a'];
		}
		else x[i] = str[i];
	}	
	
	x[l] = NULL;
	out<<"Case #"<<index<<": "<<x<<'\n';
	
}


int main()
{
	int t;
	
	in>>t;
	
	char str[dmax];
	
	in.getline(str, dmax, '\n');	
	
	for(int i=1; i<=t; i++)
	{
		in.getline(str, dmax, '\n');	
		translate(str, i);
	}

	in.close();
	out.close();
	return 0;
}	