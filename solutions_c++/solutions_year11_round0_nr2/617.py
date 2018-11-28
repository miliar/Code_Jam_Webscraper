#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <map>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
	map<pair<char, char>, char> combine;
	set<pair<char, char> > opposed;
	vector<char> elements;
	int N;
	scanf("%d", &N);
	while(N--){
		char a, b, c;
		scanf(" %c%c%c", &a, &b, &c);
		combine[make_pair(a, b)]=c;
		combine[make_pair(b, a)]=c;
	}
	scanf("%d", &N);
	while(N--){
		char a, b;
		scanf(" %c%c", &a, &b);
		opposed.insert(make_pair(a, b));
		opposed.insert(make_pair(b, a));
	}
	scanf("%d", &N);
	while(N--){
		char a;
		scanf(" %c", &a);
		elements.push_back(a);
		while(elements.size()>1){
			char e1=elements[elements.size()-2];
			char e2=elements[elements.size()-1];
			if(combine.count(make_pair(e1, e2))){
				elements.pop_back();
				elements.back()=combine[make_pair(e1, e2)];
			}else
				break;
		}
		for(int i=0; i<elements.size(); i++)
		for(int j=i+1; j<elements.size(); j++){
			if(opposed.count(make_pair(elements[i], elements[j]))){
				elements.clear();
				break;
			}
		}
	}
	putchar('[');
	int first=1;
	for(int i=0; i<elements.size(); i++){
		if(first) first=0;
		else printf(", ");
		printf("%c", elements[i]);
	}
	puts("]");
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
