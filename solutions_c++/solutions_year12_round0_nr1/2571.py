#include <vector> 
#include <map> 
#include <iostream> 

using namespace std;


char *sam_out[3] = {"our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up"};
char *sam_in[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                   "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char in_file[] = "A-small-attempt0.in";
char out_file[] = "A-small.out";
map<char,char> mapper;

int main()
{
    int case_count;
    int i = 0;
    int j = 0;
    int t = 0;
    int len = 0;
    string line;

    // set up mapper
    for (i=0; i<3; i++)
    {
        len = strlen(sam_in[i]);
        for (j=0; j<len; j++)
        {
            mapper[sam_in[i][j]] = sam_out[i][j];
        }
    }

    // add other character
    mapper['q'] = 'z';
    mapper['e'] = 'o';
    mapper['y'] = 'a';
    mapper['z'] = 'q';

    freopen(in_file,  "r", stdin);
    freopen(out_file, "w", stdout);

    cin >> case_count;
    getline(cin, line);

    for (t=1; t<=case_count; t++)
    {
        getline(cin, line);
        len = line.size();
        cout << "Case #" << t <<": ";
        for (i=0; i < len;)
        {
            cout << mapper[line[i++]];
        }
        cout << endl;
    }

	return 0;    
}
