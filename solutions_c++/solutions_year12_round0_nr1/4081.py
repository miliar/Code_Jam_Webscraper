#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

/*

Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up

 */

const char cmap[] =
{ 'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q' };
// a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z

const char gmap[] =
{ 'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q' };
// a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z

void Googlerese()
{
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");

    string str;
    getline(fin, str);
    int T = atoi(str.c_str());

    for (int i = 1; i <= T; ++i)
    {
    	getline(fin, str);

    	int n = str.size();
    	for (int j = 0; j < n; ++j)
    	{
    		if (str[j] == ' ') continue;
    		str[j] = gmap[str[j]-'a'];
    	}
        fout << "Case #" << i << ": " << str << endl;
    }
    fin.close();
    fout.close();
}
