#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <math.h> 
#include <queue>
#include <fstream>

int testCases;

using namespace std;

int main(void)
{
	ifstream in("B-small.in");
	ofstream out("B-output.out");
	string line;
	
	int testCases; 
	getline(in,line); stringstream s1(line); s1 >> testCases;
	
	for(int tst=0; tst<testCases; tst++)
	{
	
		getline(in,line);
		
		long long N; long long initN;
		
		stringstream spin(line); spin >> N;
		
		cout << line << " " <<  N << endl;
		
		 initN = N;
		
		
		vector <int> count(10,0);
		cout << "here" << endl;
		
		for(int i=0; i<line.length(); i++) { count[line[i]-'0']++; }
		
		cout << "here" << endl;
		
		bool found = false;
		long long best = -1;
		
		int n = line.length();
		
		string res;
		
		cout << "here" << endl;
		
		for(int i=1; i<n; i++)
		{
			string tmp = line.substr(n-i-1,i+1);
			cout << tmp << endl;
			bool isInc = false;
			
			for(int j=1; j<tmp.length(); j++)
			{
				if(tmp[j]>tmp[j-1]) {
					isInc = true;
					break;
				}
			}
			
			if(isInc) {
				
				res = "";
				
				vector <int> cnt(10,0);
				
				for(int j=0; j<tmp.length(); j++) { cnt[tmp[j]-'0']++; }
				
				for(int j=0; j<10; j++) { 
					if(cnt[j] > 0 && j > tmp[0]-'0') {
						res += '0'+j;
						cnt[j]--;
						for(int k=0; k<10; k++) {
							while(cnt[k] > 0) {
								res += '0'+k;
								cnt[k]--;
							}
						}
					break;
					}
				}
					
				cout << res << " " << endl;
				
				res = line.substr(0,n-i-1) + res;
				found = true;
				break;
			}
		}
		
		string ret = res;
		
		if(!found)
		{
			count[0]++; ret = "";
			
			for(int i=1; i<10; i++)
			{
				if(count[i] > 0)
				{
					ret += '0'+i;
					count[i]--;
					break;
				}
			}
			
			for(int i=0; i<10; i++)
			{
				while(count[i] > 0) {
					string tmp = ""; tmp += '0'+i;
					ret += tmp;
					count[i]--;
				}
			}
			
			
			
			
		}
		
	
			
			
		
	out << "Case #" << tst+1 << ": " << ret << endl;

	
	}


}