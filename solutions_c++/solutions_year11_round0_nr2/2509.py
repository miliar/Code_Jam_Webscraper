#include <iostream>
#include <vector>
#include <bitset>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

void erre( vector<char> elements ){
	//cerr << "### ";
	for(int i=0; i < elements.size(); i++) {
         cerr << elements[i] << ", ";
     }
	//cerr << endl;
}


int main() {
    int T, C, D, N;
    scanf("%d", &T);

    map<string, char> replace;
    vector<string> cl;
    vector<char> elements;

    for(int cases = 0; cases < T; cases++) {
        replace.clear();
        cl.clear();
        elements.clear();

		//cerr << "### Reading Replacement Rules" << endl;
        scanf("%d",&C);
        for(int i=0; i < C; i++) {
            string temp;
            string res = "";
            cin >> temp;
            for(int i=0; i < temp.length()-1; i++) {
                res += temp[i];
            }
            replace.insert(pair<string,char>(res,temp[2]));
            reverse(res.begin(), res.end());
            replace.insert(pair<string,char>(res, temp[2]));
        }        

		//cerr << "### Reading Opposite Rules" << endl;
        scanf("%d", &D);
        for(int i=0; i < D; i++) {
            string t;
            cin >> t;
            cl.push_back(t);
            reverse(t.begin(), t.end());
            cl.push_back(t);
        }

		//cerr << "### Reading Element List" << endl;
        scanf("%d", &N);
        for(int i=0; i < N; i++) {
            char c;
            string temp = "";
            cin >> c;
            elements.push_back(c);
			//cerr << "### !! " << c << endl;
            bool explode = false;
     
			//erre(elements);
       		if(!elements.empty() && elements.size() > 1) {
	
				//*** check for reactions....
                for(int j=elements.size()-2; j <=elements.size()-1; j++) {
                    temp += elements[j];
                }
                //cerr << "### last elements = " << temp << endl;
                
				if(!replace.empty() && replace[temp]){
					//cerr << "### reacts with " << replace[temp] << endl;
                    elements.pop_back();
                    elements.pop_back();
                    elements.push_back(replace[temp]);
                } 
				else //*** check for opposites....
				{
                    for(int k=0; k < cl.size(); k++) {
                        string ret = cl[k];
                        if(c == ret[0]) {
							// find oposite in elements..
                            for(int m = 0; m < elements.size(); m++) {
                                if(elements[m] == ret[1]) {
                                    explode = true;
                                    break;
                                }
                            }
                        } else if(c == ret[1]) {
                            for(int m=0; m < elements.size(); m++) {
                                if(elements[m] == ret[0]) {
                                    elements.clear();
                                    break;
                                }
                            }
                        }
                    }
                    //if (explode) elements.clear();
                }
            }
			//erre(elements);
        }
        cout << "Case #" << cases+1 << ": ";

		cout << "[";
        for(int i=0; i < elements.size(); i++) {
			cout << elements[i]; 
			if (i+1 < elements.size()) 
			    cout << ", ";
        }
		cout << "]" << endl;
        
    }
    return 0;
}
            