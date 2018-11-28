#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}

int gcd(int a, int b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int lcm(int a, int b)
{
    int temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}

int main(){
	int T;
	scanf("%d",&T);
	cin.ignore();
	for (int cs=1; cs<=T; cs++){
		long long N, L, H;
		cin >>N >>L >>H;
		vector<long long> freq(N);
		for (long long i=0; i<N; i++)
			cin >> freq[i];
		sort(freq.begin(), freq.end());
		
		long long lcm = 1;
		for (long long i=L; i<=H; i++){
				bool end = true;
				//cout<<i<<endl;
				for (long long j=0; j<N; j++)
					if (i>=freq[j] && i%freq[j]!=0){
						end = false;
						break;
					}
					else if (i<freq[j] && freq[j]%i!=0){
						end = false;
						break;
					}
				if (end){
					lcm = i;
					break;
				}
			}
		cout<<"Case #"<<cs<<": ";
		if (lcm>=L && lcm <=H)
			cout<<lcm<<endl;
		else
			cout<<"NO"<<endl;
		
	}
	return 0;
}
