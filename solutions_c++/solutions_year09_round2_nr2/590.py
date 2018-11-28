#include <simple.h>

	// number of cases 100;  animals 100; features 100


int main() {
	//char	line[1001];
	char	s[1001];
	int CS;
	cin  >> CS; cin.getline(s,1000); 


	for ( int cs=1;   cs<=CS ;   cs++)  {
		cout << "Case #" << cs << ": ";		
		vector<char>	v;
		char c;
		v.push_back('0');
		while (c=cin.get(), isdigit(c))
			v.push_back(c);

					//for (int i=0; i<v.size(); i++) cerr << v[i];   cerr << endl;
			next_permutation(v.begin(), v.end());
					if (v[0]=='0')  { for (int i=1; i<v.size(); i++) cout << v[i];   cout << endl; }
					else		{ for (int i=0; i<v.size(); i++) cout << v[i];   cout << endl; }
		//cin.getline(s,1000); 
	}
										//cerr << endl;
	return 0;
}
