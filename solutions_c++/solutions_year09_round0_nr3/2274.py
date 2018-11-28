#include <iostream>
#include <iomanip>
#include <vector>
#include <string>

using namespace std;
inline void incr(vector<long> &comb, const int pos)
{
    comb[pos]+=comb[pos-1];
    comb[pos]%=10000;
}

int main()
{
    cout << setfill('0');
    int cases;
    cin >> cases;
    string empty;
    getline(cin, empty);
    for (int num=0; num<cases; ++num)
    {
	string line;
	getline(cin, line);
	vector<long> comb(20);
	comb[0]=1;
	for (int i=0; i<line.length(); ++i)
	{
	    switch(line[i])
	    {
	        //welcome to code jam
	        //1234567890123456789
		case 'w': incr(comb,1); break;
		case 'e': incr(comb,2);
			  incr(comb,7);
			  incr(comb,15); break;
		case 'l': incr(comb,3); break;
		case 'c': incr(comb,4);
			  incr(comb,12); break;
		case 'o': incr(comb,5);
			  incr(comb,10);
			  incr(comb,13); break;
		case 'm': incr(comb,6);
			  incr(comb,19); break;
		case ' ': incr(comb,8);
			  incr(comb,11);
			  incr(comb,16); break;
		case 't': incr(comb,9); break;
		case 'd': incr(comb,14); break;
		case 'j': incr(comb,17); break;
		case 'a': incr(comb,18); break;
		default: break;
	    }
//            for (int j=0; j<19; ++j) 
// 	        cout << comb[j];
//            cout << ' ' << line[i] << endl;
	}
	cout << "Case #" << num+1 << ": " << setw(4) << comb[19] << endl;
    }
    return 0;
}
