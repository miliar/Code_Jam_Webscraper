#include<stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <string.h>

using namespace std;
vector<string> lines;
class ReadCases
{
private:
    FILE *fp_;

    bool init(const char *name)
    {
        fp_ = fopen(name, "r");
        if (!fp_)
        {
            cerr << "Could not open file: " << name <<'\n';
            return false;
        }
    }

public:
    ReadCases(const char *name)
    {
        init(name);
    }

    ~ReadCases()
    {
        if(fp_)
            fclose(fp_);
    }

    int readAllCases( )
    {
	char line[1025];
        if (!fgets(line, sizeof line, fp_))
        {
            cerr << "nothign found in the file\n";
            return -1;
        }
	int count =0;
	sscanf(line, "%d", &count);
//	printf( "Count %d\n", count);
	for(int i=0;i<count;++i)
	{
	    if (!fgets(line, sizeof line, fp_))
	    {
		cerr << "nothign found in the file\n";
		return -1;
	    }
	    lines.push_back(line);
	}

	return count;
    }

};

long occur =0;
char s[] ="welcome to code jam";
int len = strlen(s);

void getcount(string &line, int srcpos, int linepos)
{
    if (srcpos == len)
    { 
	++occur; 
	return;
    }
    
    for(int i = linepos; i<line.length(); ++i)
    {
	if (s[srcpos] == line[i])
	{
	    getcount(line, srcpos+1, i+1);
	}
    }	
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cerr << "usage: a.out <file>\n";
	return -1;
    }

    ReadCases r(argv[1]);
    r.readAllCases( );

    for(int i =0;i<lines.size();++i)
    {
	occur = 0;
	getcount(lines[i], 0,0);
	printf("Case #%d: %04ld\n", i+1, occur % 10000 );
    }

    return 0;
}
