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

int main(){
	int T;
	scanf("%d",&T);
	cin.ignore();
	for (int cs=1; cs<=T; cs++){
		string str;
		getline(cin,str);
		
		vector<string> dat;
		Tokenize(str,dat);
		
		int pos=0;
		int C = atoi(dat[pos].c_str());
		pos++;
		vector<string> cstr;
		for (int k=0; k<C; k++){
			cstr.push_back(dat[pos]);
			pos++;
		}
		
		//cout<<C<<" "<<dat[0]<<endl;
		
		int D = atoi(dat[pos].c_str());
		pos++;
		vector<string> dstr;
		for (int k=0; k<D; k++){
			dstr.push_back(dat[pos]);
			pos++;
		}
		
		//cout<<D<<endl;
		
		int N = atoi(dat[pos].c_str());
		pos++;
		//cout<<pos<<endl;
		string tmp = dat[pos];  //for(int k=0; k<tmp.size(); k++)			elts.push_back(tmp[k]);
		
		string elts;
		elts+=tmp[0];
		for (int k=1; k<tmp.size(); k++){
			char p = elts[elts.size()-1];
			bool invoked = false;
			for (int n=0; n<C; n++){
				char c1 = cstr[n][0];
				char c2 = cstr[n][1];
				char r = cstr[n][2];
				if ((p==c1 && tmp[k]==c2)||(p==c2 && tmp[k]==c1)){
					elts[elts.size()-1]=r;
					invoked = true;
					break;
				}
			}
			if (!invoked){
				for (int n=0; n<D; n++){
					char c1 = dstr[n][0];
					char c2 = dstr[n][1];
					for (int m=0; m<elts.size(); m++){
						p = elts[m];
						if ((p==c1 && tmp[k]==c2)||(p==c2 && tmp[k]==c1)){
							elts.clear();
							invoked = true;
							break;
						}
					}
					if (invoked)	break;
				}
				
			}
			if (!invoked)	elts+=tmp[k];
		}
		
		cout<<"Case #"<<cs<<": [";
		if (elts.size()==0)	
			cout<<"]\n";
		else{
			for (int k=0; k<elts.size()-1; k++) cout<<elts[k]<<", ";
			cout<<elts[elts.size()-1]<<"]\n";
		}
	}
	return 0;
}
