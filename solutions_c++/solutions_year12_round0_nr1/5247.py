#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

char in_file[] = "A-small-attempt1.in";
char out_file[] = "small-out.data";

map<char,char> mapper;
char *sam_in[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                   "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char *sam_out[3] = {"our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up"};

int main()
{
    int case_count;
    int i,j,t;
    string line;
    int len;

    for (i=0; i<3; i++)
    {
        len = strlen(sam_in[i]);
        for (j=0; j<len; j++)
        {
            mapper[sam_in[i][j]] = sam_out[i][j];
        }
    }
    mapper['y'] = 'a';
    mapper['e'] = 'o';
    mapper['q'] = 'z';
    mapper['z'] = 'q';

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    cin >> case_count;
    cin.get();          //clear \n
    
    for (t=1;t<=case_count;t++)
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
