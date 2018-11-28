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

class Pile{
	public:
		vector<unsigned long> ci;
		unsigned long sum1;
		unsigned long sum2;
		Pile(){
			sum1=0;
			sum2=0;
		}
		void addC(unsigned long c){
			ci.push_back(c);
			sum1^=c;
			sum2+=c;
		}
};

int main(){
	int T, N;
	cin >> T;
	for (int cs=1; cs<=T; cs++){
		cin >> N;
		string str;
		
		cin.ignore();
		getline(cin,str);
		
		vector<string> dat;
		Tokenize(str,dat);
		
		vector<unsigned long> candies;
		for (int k=0; k<dat.size(); k++){
			unsigned long l = atol(dat[k].c_str());
			candies.push_back(l);
		}
		sort(candies.begin(),candies.end());
		
		Pile P1, P2;
		P1.addC(candies[0]);
		P2.addC(candies[1]);
		for (int k=2; k<N; k++){
			if (P2.sum1^candies[k]<P1.sum1)
				P2.addC(candies[k]);
			else
				P1.addC(candies[k]);
		}
		
		cout<<"Case #"<<cs<<": ";
		if (P1.sum1!=P2.sum1)
			cout<<"NO\n";
		else
			cout<<max(P1.sum2,P2.sum2)<<endl;
			//cout<<max(P1.sum2,P<<"/"<<P2.sum1<<" ... "<<P1.sum2<<"/"<<P2.sum2<<endl;
	}
	return 0;
}
