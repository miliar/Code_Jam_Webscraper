#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int ELEM = 26;

int cmbmat[ELEM][ELEM];
int oppmask[ELEM];

int convert(char c){
    return (c - 'A');
}

char revert(int v){
    return (v + 'A');
}

string format(const string& resp){
    string ret = "[";
    if(resp.size() > 0){
	ret += resp[0];
	for(int i=1;i<resp.size();++i){
	    ret += ", ";
	    ret += resp[i];
	}
    }
    ret += "]";
    return ret;
}

string calc(const string& input){
    string ret = "";
    ret.reserve(input.size());
    int curmask = 0;
    int qtd[ELEM];
    
    for(int i=0;i<input.size();++i){
	int ind = convert(input[i]);
	
	while(ret != ""){
	    int last = convert(*ret.rbegin());
	    if(cmbmat[ind][last] < 0){
		break;
	    }
	    
	    ind = cmbmat[ind][last];
	    ret.erase(ret.end()-1);
	    qtd[last]--;
	    if(qtd[last] == 0){
		curmask ^= (1<<last);
	    }
	}
	
	if((oppmask[ind] & curmask) != 0){
	    ret = "";
	    curmask = 0;
	}
	else{
	    ret += revert(ind);
	    if((curmask & (1<<ind)) != 0){
		qtd[ind]++;
	    }
	    else{
		qtd[ind] = 1;
		curmask |= (1<<ind);
	    }
	}
    }
    
    return ret;
}

int main(){   
    int t;
    cin >> t;
    
    for(int lp=1;lp<=t;++lp){
	int c;
	cin >> c;
	for(int i=0;i<ELEM;++i){
	    for(int j=0;j<ELEM;++j){
		cmbmat[i][j] = -1;
	    }
	}
	
	for(int i=0;i<c;++i){
	    string s;
	    cin >> s;
	    int a = convert(s[0]);
	    int b = convert(s[1]);
	    int k = convert(s[2]);
	    cmbmat[a][b] = cmbmat[b][a] = k;
	}
	
	int d;
	cin >> d;
	for(int i=0;i<ELEM;++i){
	    oppmask[i] = 0;
	}
	
	for(int i=0;i<d;++i){
	    string s;
	    cin >> s;
	    int a = convert(s[0]);
	    int b = convert(s[1]);
	    oppmask[a] |= (1<<b);
	    oppmask[b] |= (1<<a);
	}
	
	int n;
	cin >> n;
	string input;
	cin >> input;
	cout << "Case #" << lp << ": " << format(calc(input)) << "\n";
    }
    
    return 0;
}