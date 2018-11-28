#include <iostream>
#include <algorithm>
#include <vector>
#include <string>



using namespace std;



int main()
{
	int L, D, N;
	cin >> L >> D >> N;

	vector<string> vDest;
	
	for(int i=0; i<D; ++i) {
		string str;
		cin >> str;
		vDest.push_back(str);
	}

	sort(vDest.begin(), vDest.end());

	vector<string> vOrigin = vDest;

	int testcase = 1;
	while(N--) {
		cout << "Case #" << testcase++ << ": ";
		vDest = vOrigin;
		
		string str;
		cin >> str;

		bool open = false;
		string temp;
		temp.clear();
		vector<string> vSrc;
		
		for(int i=0; i<(int)str.size(); ++i) {		
			if(str[i] == '(') {
				open = true;
				continue;
			}
			else if(str[i] == ')') {
				open = false;				
				vSrc.push_back(temp);				
				temp.clear();
				continue;
			}
			else if(open==true) {
				temp += str[i];
			}
			else if(open==false) {
				temp += str[i];
				vSrc.push_back(temp);
				temp.clear();
			}
		}
		
		vector<string>::iterator iter;
		for(int i=0; i<(int)vSrc.size(); ++i) {
			for(iter=vDest.begin(); iter!=vDest.end(); ) {
				bool flag = false;
				for(int k=0; k<(int)vSrc[i].size(); ++k) {															
					if((*iter)[i] == vSrc[i][k])
						flag = true;
				}
				if(flag == false)
					iter = vDest.erase(iter);												
				else
					++iter;				
			}
		}

//		for(iter = vDest.begin(); iter != vDest.end(); ++iter)
//			cout << *iter << endl;
		cout << vDest.size() << endl;

		
	}







	



	


	return 0;
}