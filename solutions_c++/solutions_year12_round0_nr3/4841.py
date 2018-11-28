#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstring>

using namespace std;

#define LEN 1000000
#define INPUT "C:\\temp\\C-small-attempt0.in"


static string readline(ifstream& ifs)
{
	char line[LEN];
	ifs.getline(line, LEN);
	string s = line;
	return s;
}

char asc[100], as[40], bs[20];

bool isrecycled(int a, int b)
{
	sprintf(as, "%d", a);
	sprintf(bs, "%d", b);
	strcpy(asc, "");
	strcat(asc, as);
	strcat(asc, as);
	return strstr(asc, bs) != 0;
}

int main()
{
	ifstream ifs;
	ifs.open(INPUT);

	int ncases = 0;
	string ncases_str = readline(ifs);
	istringstream iss(ncases_str);
	iss>>ncases;

	for(int i=0; i<ncases; i++)
	{
		int n1, n2;
		string case_str = readline(ifs);
		istringstream ics(case_str);
		ics>>n1>>n2;
	
		int c = 0;
		for(int a=n1; a<=n2; a++)
		{
			for(int b=n1; b<=n2; b++)
			{
				if(a == b) continue;
				if(isrecycled(a,b)) c++;
			}
		}

		cout<<"Case #"<<(i+1)<<": "<<c/2<<endl;
	}

	return 0;
}	
	