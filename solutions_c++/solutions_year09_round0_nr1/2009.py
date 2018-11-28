#include <stdio.h>
#include <vector>
#include <set>
#include <string>
#include <libgen.h>
#include <iostream>
//#include <sys/types.h>
//#include <regex.h>

using namespace std;

typedef struct Case
{
    vector<string> ;
};
vector<string> words;
typedef vector<string> Pattern;
vector< Pattern > patterns;

vector<Case> allIn;
int N= 0, D=0,L=0;

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
        char *nC = regcmp("([0-9]+)$0 ([0-9]+)$1 ([0-9]+)$2", 0);
        if (!nC)
        {
            cerr << "regcmp error: count\n" ;
            return -1;
        }

        // TEST CASE COUNT
        char line[1025];
        if (!fgets(line, sizeof line, fp_))
        {
            cerr << "nothign found in the file\n";
            return -1;
        }

        char sN[10], sD[10], sL[10];
        if (!regex(nC, line, sL, sD, sN))
        {
            cerr << "not accordin to format " << line << "\n";
            return -1;
        }
        N = atoi(sN);
        L = atoi(sL);
        D = atoi(sD);
        // END

        char *wC = regcmp("([a-z]+)$0", 0);
        if (!wC)
        {
            cerr << "regcmp error: Word\n" ;
            return -1;
        }

        // EACH WORD
        for(int i =0;i<D;++i) 
        {
//            cout << i <<"/"<<N<<endl;
            // WORD
            if (!fgets(line, sizeof line, fp_))
            {
                cerr << "Words NOT found\n";
                return -1;
            }

            char word[10];
            if (!regex(wC, line, word))
            {
                cerr << "Words not accordin to format " << line << "\n";
                return -1;
            }
	    words.push_back(word);
	}
	// END

	// EACH PATTERN
	for(int j=0;j<N;++j)
	{
	    Pattern p;
	    if (!fgets(line, sizeof line, fp_))
	    {
		cerr << "Pattern NOT found\n";
		return -1;
	    }
	    char engine[101]={0};
	    int len = strlen(line);
	    bool patMode = false;
	    int st=0, en=0;
	    for(int i=0;i<len;++i)
	    {
		if (line[i] == '(' && !patMode)
		{
		    st = i+1;
		    patMode=true;
		}
		else if (line[i] == ')' && patMode)
		{
		    en = i;
		    p.push_back(string(line+st, line+en));
		    patMode=false;
		}
		else if (line[i] >='a' && line[i]<='z' && !patMode)
		{
		    string s;
		    s = line[i];
		    p.push_back(s);
		}
	    }
	    patterns.push_back(p);
	}
        // END

        return N;
    }
};

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cerr << "usage: a.out <file>\n";
        exit(0);
    }

    ReadCases r(argv[1]);
    r.readAllCases( );
    
//     cout << "Words: " << endl;
//     for(int i=0;i<words.size();++i)    
// 	cout << words[i] << endl;    

//     cout << "Pattern: " << endl;
//     for(int i=0;i<patterns.size();++i)
//     {
// 	for(int j=0;j<patterns[i].size();++j)
// 	{
// 	    if (patterns[i][j].length()>1)
// 		cout << "[" << patterns[i][j] <<"]";
// 	    else
// 		cout << patterns[i][j];
// 	}
// 	cout << endl;
//     }

    // EACH CASE / PATTERN
    for(int i=0;i<patterns.size();++i)
    {
	int match=0;
	for(int k=0;k<words.size();++k) // EACH WORD
	{    
	    int j=0;
	    for(;j<patterns[i].size();++j)
	    {
		if ( patterns[i][j].find(words[k][j]) == string::npos )
		    break;
	    }

	    if (j == patterns[i].size())
		++match;
	}
	cout << "Case #" << i+1 << ": " << match << endl;
    }
    
    return 0;
}
