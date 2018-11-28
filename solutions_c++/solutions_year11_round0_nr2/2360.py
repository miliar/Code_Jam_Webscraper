#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <stdint.h>
#include <vector>
#include <cassert>
using namespace std;

typedef vector< pair<char,char> > dest_t;
void go(string &t, int c, char * elements, dest_t & dest){
    //cout << t << "\n";
    vector<char> invoked;
    string test;
    invoked.reserve(1000);
    invoked.push_back(t[0]);
    uint32_t hash[256];
    memset(hash,0,256 * 4);
    size_t i = 1;
    hash[t[0]] = 1;
    //cout << " " << t[0] << "\n";
    test.append(1,t[0]);
    while(i < t.length()){
	size_t h = ((size_t)invoked.back() << 8) + (size_t)t[i];
	assert(h < (256 * 256));
	//cout << " " << t[i] << " h: " << h << " value: " << (int)elements[h] << "\n";
	test.append(1,t[i]);
	if(elements[h] > 0){
	    //cout << "   Invoke! " << invoked.back() << " " << t[i] << "\n";
	    hash[invoked.back()]--;
	    invoked.back() = elements[h];
	    hash[elements[h]]++;
	}else{
	    invoked.push_back(t[i]);
	    hash[t[i]]++;
	}

	i++;

	for(size_t j = 0; j < dest.size(); ++j){
	    //cout << "    hash[" << (char)dest[j].first << "] = " << hash[dest[j].first] << " hash[" << (char)dest[j].second << "] = " << hash[dest[j].second] << "\n";
	    if(hash[dest[j].first] > 0 && hash[dest[j].second] > 0){
		//cout << "  Dest:   " << (char)dest[j].first << (char)dest[j].second << "\n";
		memset(hash,0,256 * 4);
		invoked.clear();
		if(i < t.length()){
		    invoked.push_back(t[i]);
		    hash[t[i]] = 1;
		    test.append(1,t[i]);
		    i++;
		    //cout << " " << t[i] << "\n";
		}
		break;
	    }
	}
	/*
	cout << "Stack: ";
	for(size_t j = 0; j < p; ++j){
	    cout << invoked[j];
	}
	cout << "\n";
	*/
    }
    assert(test == t);
    cout << "Case #" << c << ": [";
    if(invoked.size() > 0){
	cout << (char)invoked[0];
	for(size_t j = 1; j < invoked.size(); ++j){
	    cout << ", " << invoked[j];
	}
    }
    cout << "]\n";
}

int main(int argc, char *argv[]){
    ifstream in(argv[1]);
    std::string line, t;
    getline(in,line);
    int cases = atoi(line.c_str());
    char elements[256*256];
    dest_t dest;
    for(size_t c = 0; c < cases; c++){
	memset(elements,0,256*256);
	dest.clear();
	getline(in,line);
	//cout << line << "\n";
	stringstream ss(line);
	getline(ss,t,' ');
	size_t x = atoi(t.c_str());
	for(size_t i = 0; i < x; i++){
	    getline(ss,t,' ');
	    size_t p1 = ((size_t)t[0] << 8) + (size_t)t[1];
	    size_t p2 = ((size_t)t[1] << 8) + (size_t)t[0];
	    //cout << "Invoke: " << t << "\n";
	    elements[p1] = t[2];
	    elements[p2] = t[2];
	}
	getline(ss,t,' ');
	x = atoi(t.c_str());
	dest.reserve(x);
	for(size_t i = 0; i < x; i++){
	    getline(ss,t,' ');
	    //cout << "Dest: " << t << "\n";
	    dest.push_back(pair<char,char>(t[0],t[1]));
	}
	getline(ss,t,' ');
	getline(ss,t,' ');
	go(t,c + 1, elements, dest);
    }
}
