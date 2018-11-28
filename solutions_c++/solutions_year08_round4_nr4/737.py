#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>

#define FOR(i,a)     for(typeof(a) i=0;i<a;i++)
#define foreach(i,a) for(typeof((a).begin()) i=(a).begin();i!=(a).end();i++)

using namespace std;

string s;

vector<int> a;

string apply()
{
    string t = "";
    for(int l=0;l<(int)(s.size()/a.size());l++)
        for(int i=0;i<a.size();i++)
            t=t+s[a.size()*l+a[i]];
    return t;
}

int mani(string str)
{
    int ret=0;
    char p = ' ';
    for(int i=0;i<str.size();i++)
    {
        if(str[i]!=p)
            ret++;
        p=str[i];
    }
    return ret;
}

int main() {
	ofstream fout ("D.out");
	ifstream fin ("D.in");
	int T;
	fin >> T;
	cout << T;
	for(int loo=0;loo<T;loo++)
	{
	int k,val,min=10000000;
	string temp;
	fin >> k;
	fin >> s;
	a.resize(k);
	for(int i=1;i<=k;i++)
            a[i-1] = i-1;
        temp = apply();
        cout << temp << endl;
        min = mani(temp);
        cout << min << endl;
        while(next_permutation(a.begin(),a.end()))
        {
            foreach(op,a) cout <<*op<< " " ;
            cout << endl;
            temp = apply();
            val = mani(temp);
            cout << val << endl;
            if(val<min)
                min = val;
        }
	fout << "Case #" << loo+1 << ": "<< min << endl;
	}
	return 0;
}
