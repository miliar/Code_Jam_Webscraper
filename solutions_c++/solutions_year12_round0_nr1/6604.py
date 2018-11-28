#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class Problem
{
public:
    static char decode[256];

	void Solve(int nCase)
	{
	    char buf[200];
	    cin.getline(buf, 200);
	    string res = buf;
		for (int i=0; i<res.length(); ++i)  res[i] = decode[res[i]];
        cout << "Case #" << nCase << ": " << res << endl;
	}
};
char Problem::decode[256];

int main()
{
    string sample[] = {
        "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up",
        "yeq z", "aoz q"
    };
    for (int i=0; i < sizeof(sample)/sizeof(string); i+=2)
        for (int j=0; j < sample[i].length(); ++j)
            Problem::decode[sample[i][j]] = sample[i+1][j];
    

    char buf[100];  cin.getline(buf, 100);
	int T;  istringstream(buf) >> T;
	Problem sol;	for (int i=1; i<=T; ++i)  sol.Solve(i);
	return 0;
}