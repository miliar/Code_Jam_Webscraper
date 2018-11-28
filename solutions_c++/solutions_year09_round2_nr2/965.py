#include<stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <stdlib.h>
#include <libgen.h>
#include <algorithm>

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

        char *nC = regcmp("([0-9]+)$0", 0);
        if (!nC)
        {
            cerr << "regcmp error: Nums\n" ;
            return -1;
        }

	for(int i=0;i<count;++i)
	{
	    if (!fgets(line, sizeof line, fp_))
	    {
		cerr << "nothign found in the file\n";
		return -1;
	    }
	    char  sL[1000]={0};
	    if (!regex(nC, line, sL))
	    {
		cerr << "failed to read\n";
		return -1;
	    }
//	    cout << sL << ' ';
	    lines.push_back(sL);
	}

	return count;
    }

};

int baseN(int b, int n)
{
    if (n < b)
	return n;

    int res = 0;
    int cnt=1;
    while(n >= b)
    {
	int t = n%b;
	n/=b;
	res += t * cnt;
	cnt *=10;
    }
    res += n * cnt;
    return res;
}

int happyNum(int b,int n)
{

    while(1)
    {
	if (n == 1 ) return 1;
	if (n < 10) return 0;
	cout << "try " << n << endl;
	int val=0;

	while(n)
	{
	    int t = n %10;
	    n /=10;
	    val += t*t;
	}
	n = baseN(b, val);
    }

    return 0;
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
	string org = lines[i];
	if (next_permutation(lines[i].begin(), lines[i].end()))
	{
//	    cout << org << ": " << lines[i] << endl;
	}
	else // need to insert zero
	{
	    // sort lines[i]
	    // swap MS 0 if exists with non zero digit in the next MS place
	    // insert 0 at 2nd MS place

//	    cout << "Need to work: " << lines[i] << endl;
	    sort(lines[i].begin(), lines[i].end());
//	    cout << "Sortd: " << lines[i] << endl;
	    
	    if(lines[i][0] == '0')
	    {
		for(int j=1;j<lines[i].length();++j)
		{
		    if (lines[i][j] != '0')
		    {
			swap(lines[i][0],lines[i][j]);
			break;
		    }
		}
	    }
	    string::size_type si = 1;
	    lines[i].resize(lines[i].length() + 1);
	    lines[i].insert(si, 1, '0');
//	    cout << org << ": " << lines[i] << endl;
	}
	printf("Case #%d: %s\n", i+1, lines[i].c_str()  );
    }

    return 0;
}
