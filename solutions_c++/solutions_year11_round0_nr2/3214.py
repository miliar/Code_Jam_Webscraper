#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int N;
	cin >> N;
	for(int i = 0; i<N; i++){
		int A,B;
		vector <pair <char, char> > a;
		vector <char> aa;
		vector <pair <char, char> > b;
		cin >> A;
		char ch1,ch2;
		for(int j = 0; j < A; j++){
			cin >> ch1 >> ch2;
			//cout << ch1 << ch2;
			pair<char, char> p;
			p.first = ch1; p.second = ch2;
			a.push_back(p);
			cin >> ch1;
			//cout << ch1 << endl;
			aa.push_back(ch1);
		}
		cin >> A;
		for(int j = 0; j < A; j++){
			cin >> ch1 >> ch2;
			pair<char, char> p;
			p.first = ch1; p.second = ch2;
			b.push_back(p);
		}
		cin >> A;
		char ch;
		cin >> ch;
		/*cout << "meniace " << a.size() << endl;
		cout << "pismena " << aa.size() << endl;
		cout << "mazacie " << b.size() << endl;*/
		vector <char> s;
		s.push_back(ch);
		for(int j = 1; j < A; j++){
			int ind = -1;
			cin >> ch;
			//cout << "nove pismeno " << ch << endl;
			bool ok = false;
			int k;
			if (s.empty()) s.push_back(ch);
			else {
				//cout << "posledne pismeno: " << s[s.size()-1] << " a char: " << ch << endl;
				for(k = 0; k < a.size(); k++ ){
					if(((s[s.size()-1] == a[k].first) && (ch == a[k].second)) || 
					   ((s[s.size()-1] == a[k].second) && (ch == a[k].first))){ 
						ok = true;
						ind = k;
						//cout << ind << endl;
					}
					//cout << "aaaa" << endl;
				}
				if(ok){
					 s[s.size()-1] = aa[ind];
					 /*cout << "menim ";
					 for(int f = 0; f < s.size(); f++) cout << s[f];
					 cout << endl;*/
				}
				else{
					ok = false;
					for(k = 0; k < b.size(); k++ ){
						for(int l = 0; l < s.size(); l++)
						if(((s[l] == b[k].first) && (ch == b[k].second)) || 
						   ((s[l] == b[k].second) && (ch == b[k].first))){ 
							ok = true;
						}
					}
					if(ok){
						s.clear();
						//cout << "mazem " << endl;
					}	 
					else{
						s.push_back(ch);
						/*cout << "vkladam ";
						for(int f = 0; f < s.size(); f++) cout << s[f];
	 			 		cout << endl;*/
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": [";
		if (!s.empty()){
			for(int j = 0; j < s.size()-1; j++) cout << s[j] << ", ";
		    cout << s[s.size()-1] << "]" << endl; 
		}
		else cout << "]" << endl;
	}
    //system("PAUSE");
    return 0;
}
