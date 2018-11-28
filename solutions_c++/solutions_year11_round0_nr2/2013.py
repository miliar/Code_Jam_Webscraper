#include <iostream>
#include <fstream>
using namespace std;
#define INPUT "B-large.in"

struct combine
{
	char a;
	char b;
	char r;
};

struct dead
{
	char a;
	char b;
};

struct Case
{
	int ncom;
	combine*  com;
	int ndead;
	dead* dis;
	int length;
	char* body;
};
	
Case* readin(int& n)
{
	ifstream fin (INPUT);
	fin >> n;
	Case* mm  = new Case[n];
	for ( int i = 0; i < n; i++)
	{
		fin >> mm[i].ncom;
		if (mm[i].ncom != 0)
		{
			mm[i].com = new combine[mm[i].ncom];	
			for( int j = 0; j < mm[i].ncom; j++)
				fin >>  mm[i].com[j].a >> mm[i].com[j].b >> mm[i].com[j].r;
		}
		fin >> mm[i].ndead;
		if (mm[i].ndead != 0)
		{
			mm[i].dis = new dead[mm[i].ndead];	
			for( int j = 0; j < mm[i].ndead; j++)
				fin >>  mm[i].dis[j].a >> mm[i].dis[j].b;
		}
		fin >>  mm[i].length;
		mm[i].body = new char[mm[i].length + 2];
		fin >> mm[i].body;
	}
	return mm;
}

char result[105];
int rc = 0;

void checkcom(int n, combine* com)
{
	char tmp1 = result[rc-2];
	char tmp2 = result[rc-1];
	for(int i = 0; i < n; i++)
		if (((com[i].a == tmp1)&&(com[i].b == tmp2))||((com[i].b == tmp1)&&(com[i].a == tmp2)))
		{
			result[rc-2] = com[i].r;
			result[rc-1] = '\0';
			rc--;
			return;
		}
}

void checkdis(int n, dead* dis)
{
	int tmp;
	for(int i = 0; i < n; i++)
	{
		char tmp1 = dis[i].a;
		char tmp2 = dis[i].b;
		tmp = 0;
		for(int j = 0; j < rc; j++)
			if (result[j] == tmp1)
			{
				tmp++;
				break;
			}
		for(int j = 0; j < rc; j++)
			if (result[j] == tmp2)
			{
				tmp++;
				break;
			}
		if (tmp == 2)
		{
			result[0] = '\0';
			rc = 0;
			return;
		}
	}
}

int main()
{
	int n;
	Case* mm = readin(n);
	
	ofstream fout ("111.txt");
	for( int ccc = 0; ccc < n; ccc++)
	{
		result[0] = '\0';
		rc = 0;
		for( int i = 0; i < mm[ccc].length; i++)
		{
			result[rc] = mm[ccc].body[i];
			rc++;
			result[rc] = '\0';
			if(rc != 1)
			{
				checkcom(mm[ccc].ncom,mm[ccc].com);
				checkdis(mm[ccc].ndead, mm[ccc].dis);
			}
		}
		fout << "Case #" << ccc + 1 << ": [";
		int ss = 0;
		for ( int i = 0 ;  i < rc ; i++)
		{
			if (ss != 0)
				fout << ", ";
			fout << result[i];
			ss = 1;
		}
		fout << "]" << endl;
	}
	return 0;
}	
