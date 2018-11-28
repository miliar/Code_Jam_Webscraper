#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class MatchWordSet {
	public:
		MatchWordSet(const string & s)
		{

			for(int i=0; i<s.length();) {
				if (s[i] == '(') {
					int j;

					for(j=1; s[i+j] != ')'; j++);
					j -= 1;

					string tempStr(s.begin()+i+1,s.begin()+i+j+1);
					
					// sort tempStr
					for(int k=0; k<j; k++) {
						sort(tempStr, k, 1);
					}
			
					_subItems.push_back(new string(tempStr));

					i += j + 2;
				} else {
					_subItems.push_back(new string(1,s.at(i)));
					i++;
				}
			}
		};

		~MatchWordSet()
		{
			for(int i=0;i<_subItems.size();i++)
				if (_subItems.at(i) != 0)
					delete _subItems.at(i);
		};

		bool isContained(const string & s)
		{
			for (int i=0;i<_subItems.size();i++) {
				string * p = _subItems.at(i);

				bool found=false;
				int l = 0;
				int r = p->length()-1;
				
				while (l <= r) {
					int m = (l + r) / 2;
					if(s.at(i) == p->at(m)) {
						found = true;
						break;
					} else if (s.at(i) > p->at(m))
						l = m + 1;
					else
						r = m - 1;
				};
				
				if (!found)
					return false;
			}

			return true;
		};
		
		friend ostream & operator<< ( ostream & os, const MatchWordSet & mm);

	private:
		void sort(string & s, int & top, int start)
		{
			if (top + start * 2 > s.length())
				return;

			sort(s, top, start * 2);
			sort(s, top, start * 2 + 1);

			char c = s.at(top + start - 1);

			if (top + start  * 2 + 1 > s.length()) {
				if (s.at(top + start * 2 - 1) < c){
					s[top + start - 1] = s.at(top + start * 2 - 1);
					s[top + start * 2 - 1]=c;
				}
			} else {
				if (s.at(top + start * 2 - 1) < s.at(top + start * 2)) {
					if (s.at(top + start * 2 - 1) < c){
						s[top + start - 1] = s.at(top + start * 2 - 1);
						s[top + start * 2 - 1]=c;
					}
				} else {
					if (s.at(top + start * 2) < c){
						s[top + start - 1] = s.at(top + start * 2);
						s[top + start * 2]=c;
					}
				}
			}
			
		};

		vector< string *> _subItems;
};

ostream & operator<< ( ostream & os, const MatchWordSet & mm)
{
	os << "MatchWordSet dumpout:" << endl;

	for (int i=0; i<mm._subItems.size();i++)
		os << i << "->" << * mm._subItems.at(i) << endl;

	return os;
}

int main()
{
	int L,D,N;

	cin >> L >> D >> N;

	vector <string *> dictionary;
	for(int i=0;i<D;i++) {
		string input;
		cin >> input;
		dictionary.push_back(new string(input));
	}
	
	vector <MatchWordSet *> mw;
	for(int i=0;i<N;i++) {
		string input;
		cin >> input;
		mw.push_back(new MatchWordSet(input));
	}
	
	for(int i=0;i<N;i++) {
		cout << "Case #" << i+1 << ": ";
		
		int matched = 0;	
		for (int j=0; j<D; j++)
			if (mw.at(i)->isContained(*dictionary.at(j)))
				matched++;
		
		cout << matched << endl;
	}

	for (int i=0;i<dictionary.size();i++)
		delete dictionary.at(i);

	for (int i=0;i<mw.size();i++)
		delete mw.at(i);

	return 0;
}

