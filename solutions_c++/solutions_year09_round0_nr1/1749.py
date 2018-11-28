#include <iostream>
#include <string>
#include <list>

using namespace std;
main()
{   

int word_l, dict_size, no_queries;

cin >> word_l >> dict_size >> no_queries;

list<string> dictionary; string word; getline(cin, word);
for(int d=0; d<dict_size; d++) { getline(cin,word); dictionary.push_back(word); }

list<string> queries;
for(int cases=0; cases<no_queries; cases++) {
	getline(cin, word); 
	queries.push_back(word);
}

list<string> pattern; int query=1;
for(list<string>::iterator it=queries.begin(); it!=queries.end(); it++) {
	word=*it;	
	pattern.clear(); string pattern_el;
	int pos=0; 
	int par_mode=0;
	while(pos<word.size()) {
	   pattern_el.clear(); 
	   if(pos<word.size() && !word.compare(pos,1,"(")) { pos++; par_mode=1;} 
	   if(pos<word.size() && !word.compare(pos,1,")")) { pos++; par_mode=0;}
	   while(word.compare(pos,1,"(") && word.compare(pos,1,")") && pos < word.size()) {
		//cout << word.at(pos) << " , ";		
		if(par_mode) pattern_el+=word.at(pos); else {pattern_el=word.at(pos); pattern.push_back(pattern_el);}
		//cout << pattern_el << endl;
		pos++;
	   }
	   if(!pattern_el.empty() && par_mode) pattern.push_back(pattern_el);
	}
	int matches=0;
	for(list<string>::iterator itd=dictionary.begin(); itd !=dictionary.end(); itd++) {
	   word=*itd; //cout << word << endl;
	   int pos=0; 
	//for(list<string>::iterator it=pattern.begin(); it !=pattern.end(); it++) cout << *it << " , "; cout << endl;
	   list<string>::iterator it1=pattern.begin(); 
	   while(it1!=pattern.end() && ((*it1).find(word.at(pos))!=string::npos)) {it1++; pos++;} 
	   if(it1==pattern.end()) ++matches;
	}

        //for(list<string>::iterator it=pattern.begin(); it !=pattern.end(); it++) cout << *it << " , "; 
	cout << "Case #"<< query++ <<": " << matches << endl;

}



}
