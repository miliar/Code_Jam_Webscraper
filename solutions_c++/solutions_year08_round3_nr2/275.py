#include <iostream>
#include <string>

using namespace std;

int f(long long k, char a, const string &s)
{
    if(s=="") {
	if(k%2==0 || k%3==0 || k%5==0 || k%7 == 0)
	    return 1;
	else
	    return 0;
    }
    
    long long result = 0;
    for(int i=1; i<=s.size(); i++) {
	string lefts = s.substr(0,i);
	string rights = s.substr(i);
	long long left;
	sscanf(lefts.c_str(), "%lld", &left);

	long long tmp;
	if(a == '+')
	    tmp = k+left;
	else
	    tmp = k-left;
	
	if(rights=="")
	    result += f(tmp, '+', rights);
	else {
	    result += f(tmp, '+', rights);
	    result += f(tmp, '-', rights);
	}
    }
    return result;
}

int solve()
{
    string s;
    cin >> s;
    return f(0,'+',s);
}

int main()
{
    int N;
    cin >> N;
    for(int i=1; i<=N; i++)
	cout << "Case #" << i << ": " << solve() << endl;
    return 0;
}
