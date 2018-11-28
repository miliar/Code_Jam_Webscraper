#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main(){

	 freopen("B-large.in","r",stdin);
	 freopen("outB.txt","w",stdout);

	int cases;
	cin >> cases;
	int outCase=0;
	for(int i=0;i<cases;i++){
		outCase++;
		vector<char> elems;
		vector<string> opposed,combined;
		vector<char> combination;
		int combNum,oppNum;
		cin >> combNum;
		for(int j=0;j<combNum;j++){
			string temp;
			cin >> temp;
			combined.push_back(temp);
			combination.push_back(combined.back()[2]);
			combined.back().erase(combined.back().begin()+2);
		}


		cin >> oppNum;
		for(int j=0;j<oppNum;j++){
			string temp;
			cin >> temp;
			opposed.push_back(temp);
		}

		string invoked;
		int invokes;
		cin >> invokes;
		cin >> invoked;
		for(int j=0;j<invokes;j++){
			elems.push_back(invoked[j]);
			if(elems.size()>1){
				// check for combined
				for(int k=0;elems.size()>1 && k<combNum;k++){
					string elem1,elem2;
					elem1.push_back(elems[elems.size()-1]);
					elem1.push_back(elems[elems.size()-2]);
					elem2.push_back(elems[elems.size()-2]);
					elem2.push_back(elems[elems.size()-1]);
					if(elem1 == combined[k] || elem2==combined[k]){
						elems.pop_back();
						elems.pop_back();
						elems.push_back(combination[k]);
						break;
					}
				}
				// check for opposed
				for(int k=0;k<oppNum;k++){
					for(int w=elems.size()-1; w>=0;w--){
						string cleared,cleared1;
						cleared.push_back(elems[elems.size()-1]);
						cleared.push_back(elems[w]);
						cleared1.push_back(elems[w]);
						cleared1.push_back(elems[elems.size()-1]);
						if(opposed[k] == cleared || opposed[k]==cleared1){
							elems.clear();
							k=oppNum;
							break;
						}
					}
				}
				
			}
		}

		cout << "Case #" << outCase << ": [";
		for(int l=0;l<elems.size();l++)
			cout << elems[l] << ( (l==elems.size()-1)?"":", " );
		cout <<"]"<<endl;
	}

	


	return 0;
}
