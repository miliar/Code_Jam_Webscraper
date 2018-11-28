#include <iostream>
#include <iomanip>

using namespace std;

const int maxT = 100;
const int maxLen = 60;	// line length

int main()
{
	int T, len, cnt, base, d;
	char s[maxLen+1];  // max animal info length
	char tbl[128];
	long long r;

	cin >> T;
	//cout << T << '\n';
	for(int t=1; t<=T; t++){
		/************************************
			Input Data
		*************************************/
		cin >> s;
		len = strlen(s);
		//cin.ignore(maxLen,'\n'); // skipping end-of-line
		//cout << s << endl;
		/************************************
			Solve the Problem
		*************************************/
		// Determine the base (quantity of distinct digits)
		memset(tbl,0,sizeof(tbl));
		cnt = 0;
		for(int i=0; i<len; i++)
		{
			if(!tbl[s[i]])
			{
				tbl[s[i]] = 1;
				cnt++;
			}
		}
		base = cnt; if(base==1) base++;
		// Assign digits to symbols
		memset(tbl,0,sizeof(tbl));
		r = 0; cnt = -1;
		//cout << endl; // debug
		for(int i=0; i<len; i++)
		{
			if(!tbl[s[i]])
			{
				switch(cnt){
					case -1:	cnt = 1; break;
					case  1:	cnt = 0; break;
					case  0:	cnt = 2; break;
					default:
								++cnt;	
				}
				tbl[s[i]] = cnt+1;
			}
			d = tbl[s[i]]-1;
			//cout << d; // debug
			// Compute the number of seconds
			r = r*base + d;
		}
		//cout << endl; // debug
		/************************************
			Output Results
		*************************************/
		cout << "Case #" << t << ": " << r << endl;
		/* Debug
		cout << "----------------\n";
		for(int j=0; j<n; j++)
			cout << X[j] << " " << Y[j] << endl;
		cout << "----------------\n";
		*/
	}
	return 0;
}
