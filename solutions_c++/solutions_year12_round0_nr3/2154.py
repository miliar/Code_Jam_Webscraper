#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int strtoint(string s)
{
    int res = 0;
    for(int i=0;i<s.size();i++) {
	res *= 10;
	res += s[i] - '0';
    }
    return res;
}

int countshifts(int k, int a, int b)
{
    int tmpk = k;
    string s = "";
    while(tmpk != 0) {
	s = ((char)('0' + tmpk%10)) + s;
	tmpk /= 10;
    }

    int count = 0;
    vector<int> v;
    for(int i=1;i<s.size();i++) {
	s = s.substr(1) + s[0];
	if(s[0] == '0')
	    continue;
	int knew = strtoint(s);
	if(knew > k && knew <= b && knew >= a) {
	    bool isnew = true;
	    for(int j=0;j<v.size();j++) {
		if(v[j] == knew) {
		    isnew = false;
		    break;
		}
	    }
	    if(isnew) {
		count++;
		v.push_back(knew);
	    }
	}
    }

    return count;
}

int main()
{
    int n; cin >> n;
    for(int i=0;i<n;i++)
    {
	int a,b; cin >> a >> b;
	int count = 0;
	for(int j=a;j<=b;j++) {
	    count += countshifts(j,a,b);
	}
	cout << "Case #" << i+1 << ": " << count << endl;
    }
    return 0;
}
