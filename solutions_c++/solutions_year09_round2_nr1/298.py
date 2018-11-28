#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <boost/lexical_cast.hpp>

using namespace std;

typedef set<string> Props;

int next_paren(string& s, int idx)
{
    int cnt = 1;
    for(int i=idx+1;i<s.size();i++){
	if( s[idx] == ')' ){
	    cnt--;
	    if( cnt == 0 )return i;
	}
	else if( s[idx] == '(' ){
	    cnt++;
	}
    }
    return -1;
}

bool isalpha(char ch)
{
    return 'a' <= ch && ch <= 'z';
}

bool isnumch(char ch)
{
    return ('0' <= ch && ch <= '9') ||
	ch == '.';
}

bool skip(char ch)
{
    return ch != '(' && ch != ')' && !(isalpha(ch)) && !(isnumch(ch));
}


struct Tree
{
    double prob;
    string name;
    vector<Tree> subs;

    Tree()
	{
	}
    
    Tree(double _prob):prob(_prob)
	{
	}
    
    Tree(double _prob, string _name, Tree& left, Tree& right):prob(_prob),name(_name)
	{
	    subs = vector<Tree>(2);
	    subs[0] = left;
	    subs[1] = right;
	}

    Tree(string& s)
	{
	    int idx  = 0;
	    (*this) = parse(s, idx);
	}

    Tree parse(string& s, int& idx)
	{
	    double prob;
	    string name;
	    // cout << "tree start: " << s.substr(idx) << endl;
	    
	    while( skip(s[idx]) ){ idx++; }
	    idx++;
	    
	    while( skip(s[idx]) ){ idx++; }

	    string tmp;
	    while( isnumch(s[idx]) ){
		tmp += string(1, s[idx]);
		idx++;
	    }
	    // cout << "lex: " << tmp << endl;
	    prob = boost::lexical_cast<double>(tmp);

	    while( skip(s[idx]) ){ idx++; }

	    if( s[idx] == ')' ){
		idx++;
		return Tree(prob);
	    }

	    name = string();
	    while( isalpha(s[idx]) ){
		name += string(1, s[idx]);
		idx++;
	    }
	    // cout << "name: " << name << endl;
	    
	    while( skip(s[idx]) ){ idx++; }

	    Tree left = parse(s, idx);
	    Tree right = parse(s, idx);

	    while( skip(s[idx]) ){ idx++; }
	    idx++;
	    
	    return Tree(prob, name, left, right);
	}

    string show()
	{
	    return "(" + boost::lexical_cast<string>(prob) + 
		(subs.size()>0?(" " + name + " " + subs[0].show() + " " + subs[1].show()):"") + ")";
	}

    double calc(double d, Props& props)
	{
	    d *= prob;
	    if( subs.size() > 0 ){
		if( props.find(name) != props.end() ){
		    return subs[0].calc(d, props);
		}
		else{
		    return subs[1].calc(d, props);
		}
	    }
	    else{
		return d;
	    }
	}
    
		
		
};



int main(void)
{
    int N;
    string dummy;
    cin >> N;
    getline(cin, dummy);

    Tree t;
    
    for(int i=0;i<N;i++){
	int L;
	cin >> L;
	string treestr;
	getline(cin, dummy);
	for(int j=0;j<L;j++){
	    string tmp;
	    getline(cin,tmp);
	    treestr += tmp;
	}
	// cout << treestr << endl;
	
	Tree t(treestr);
	// cout << t.show() << endl;

	cout << "Case #" << (i+1) << ":" << endl;
	int A;
	cin >> A;
	for(int j=0;j<A;j++){
	    string aname;
	    cin >> aname;
	    int n;
	    cin >> n;
	    Props props;
	    for(int k=0;k<n;k++){
		string p;
		cin >> p;
		props.insert(p);
	    }

	    cout << setprecision(8) 
		 << setiosflags(ios::fixed) 
		 << t.calc(1.0, props) << endl;
	}
    }
    return 0;
}

