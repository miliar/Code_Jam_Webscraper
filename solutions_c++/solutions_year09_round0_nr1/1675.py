#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
    int L, D, N;
    cin >> L;
    cin >> D;
    cin >> N;

    list<string> words;
    string w; 
    char c;

    for (int i(0); i<D; ++i)
    {
	cin >> w;
	words.push_back(w);
    }

    for (int casenum(1); casenum<=N; ++casenum)
    {
	list<string> goodwords(words);
	list<string> tmp;
	list<string>::iterator it;
	for (int cn(0); cn<L; ++cn)
	{
	    /*
	    for (list<string>::iterator it2=goodwords.begin(); it2!=goodwords.end(); ++it2)
		cout << (*it2) << endl;
	    cout << endl;
		*/
	    tmp.clear();
	    cin >> c;
	    if (c=='(')
	    {
		cin >> c;
		while(c != ')')
		{
		    for (it=goodwords.begin(); it!=goodwords.end(); ++it)
		    {
			//cout << (*it)[cn] << endl;
			if ((*it)[cn] == c) tmp.push_back(*it);
		    }
		    cin >> c;
		}
	    }
	    else
	    {
		for (it=goodwords.begin(); it!=goodwords.end(); ++it)
		{
		    if ((*it)[cn] == c) tmp.push_back(*it);
		}
	    }
	    goodwords=tmp;
	}

	cout << "Case #" << casenum << ": " << goodwords.size() << endl;
    }

    return 0;
}
