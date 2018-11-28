#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

string convStr(int j){
    ostringstream conv;
    conv  << j;
    string t = conv.str();
    return t;
}

int main(int argc, const char * argv[])
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    int T;
    input >> T;
    for(int i=0;i<T;i++){
	cout << i  << endl;
        int A,B;
	int count = 0;
        input >> A >> B;
	output << "Case #" << i+1 << ": ";
        for(int j=A; j<=B; j++){
	    string s,t,aa,bb;
	    t = convStr(j);
	    aa = convStr(A);
  	    bb = convStr(B);

	    int len = t.length();
	    s=t+t;	
	    vector<string> strs(len);
	    for(int k=0; k<len; k++){
		strs[k] = s.substr(k,len);
	    }
	    sort(strs.begin(),strs.end());
	    vector<string>::iterator new_end = unique(strs.begin(),strs.end());
	    for(vector<string>::const_iterator it = strs.begin(); it!=new_end; ++it ){
     		if(aa.compare(*it)<=0 && bb.compare(*it)>=0 && t.compare(*it)!=0) {
		    ++count;
		    //cout << t << " " << *it << " " << count << endl;
		}
	    }
	    
        }
        output << count/2 << endl;
    }
    input.close();
    output.close();
    
    return 0;
}

