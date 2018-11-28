#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<vector<string>*> in;
vector<string> out;
char seperator = 0x20;

char* trim(char* src)
{
	int length = strlen(src);
	for (int i = length - 0x01; i > -0x01; i--)
	{
		if (src[i] == 0x0d || src[i] == 0x0a)
			src[i] = 0x00;
		else
			break;
	}
	return src;
}

void input(char* src)
{
	int size = 0xffff;
	char buf[0xffff];
    FILE* fp = fopen(src, "rb");
	while(fgets(buf, size, fp) != 0x00)
	{
		vector<string>* v = new vector<string>();
		char* s = trim(buf);
		int length = strlen(s);
		for (int i = 0x00; i < length; i++)
		{
			if (buf[i] == seperator)
			{
				buf[i] = 0x00;
				string str(s);
				v->push_back(str);
				buf[i] = seperator;
				s = &buf[i + 0x01];
			}
		}
		string str(s);
		v->push_back(str);
		in.push_back(v);
	}
	fclose(fp);
}

void output(char* src)
{
	FILE* fp = fopen(src, "wb");
	for (vector<string>::iterator it = out.begin(); it < out.end(); it++)
	{
		if (it != out.begin())
			fprintf(fp, "\n%s", (*it).data());
		else
			fprintf(fp, "%s", (*it).data());
	}
	fclose(fp);
}

void release(void)
{
	for (vector<vector<string>*>::iterator itr = in.begin(); itr < in.end(); itr++)
	{
		(*itr)->clear();
		delete (*itr);
	}
	in.clear();
	out.clear();
}

void theme_park(void)
{
	char* sin = (char*)"small.in";
	char* sout = (char*)"small.out";
	seperator = 0x20;
	input(sin);
	
	vector<vector<string>*>::iterator itr = in.begin();
	int count = atoi((*((*itr)->begin())).data());
	itr++;

	int c = 0;
	while (count > c)
	{
		int r = atoi(((*(*itr))[0]).data());
		int k = atoi(((*(*itr))[1]).data());
		int n = atoi(((*(*itr))[2]).data());
		itr++;

		int* g = new int[n];
		for (int i = 0; i < n; i++)
		{
			g[i] = atoi(((*(*itr))[i]).data());
		}
		itr++;

		int y = 0;
		int p = 0;
		for (int i = 0; i < r; i++)
		{
			int s = 0;
			int l = 0;
			while (true)
			{
				s += g[p];
				if (s > k)
					break;
				y += g[p];
				p++;
				if (p == n)
					p = 0;
				l++;
				if (l == n)
					break;
			}
		}

		char buf[64];
		sprintf(buf, "Case #%d: %d", (c + 1), y);
		string str(buf);
		out.push_back(str);

		c++;
	}
	
	output(sout);
	release();
	return;
}

int main (int argc, char* argv[])
{
	theme_park();
	
    return 0x00;
}