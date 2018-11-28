//#include <math.h>
#include <stdio.h>
#include <set.h>
#include <map.h>
#include <list.h>
#include <vector.h>
#include <iostream.h>
#include <iomanip.h>
#include <sstream.h>
//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused

struct node{
        double weight;
        string feature;
        node * f, *nf, *par;
        node():weight(0),f(NULL), nf(NULL), par(NULL){}
        ~node(){if(f)delete f;if(nf)delete nf;}
};

node * readnode(stringstream &ss)
{
        node * ret = new node();
        while(ss.get() != '(');
        ss >> ret->weight;
//        cout << "w:" << ret->weight << endl;
        while(ss.peek() == ' ') ss.get();
        if(ss.peek() == ')') {
//                cout << "l:" << ret->weight << endl;
                return ret;
        }
        string feat;
        while(isalpha(ss.peek())) feat += ss.get();
        ret->feature = feat;
//                cout << "n:" << ret->weight << ":" << ret->feature << endl;
        ret->f = readnode(ss);
        ret->nf = readnode(ss);
        while(ss.get() != ')');
//                cout << "/n" << endl;
        return ret;
}

double answ(node * head, set<string>& props)
{
        double p = 1;
        do {
                p *= head->weight;
                head = props.find(head->feature) != props.end() ? head->f : head->nf;
        }
        while(head != NULL);
        return p;
}

void solve()
{
        int N;
        cin >> N;
        cin.ignore();
        string str;
        for(int i=0;i<N;++i){
                char buf[256];
                cin.getline(buf,256);
                str += buf;
        }
//        cout << str << endl;
        stringstream ss;
        ss << str;
        node * head = readnode(ss);
        cin >> N;
        cin.ignore();
        for(int i=0;i<N;++i){
                char buf[100*80];
                cin.getline(buf,100*80);
                strtok(buf," ");
                strtok(NULL," ");
                set<string> props;
                char * str;
                while( (str = strtok(NULL," ")) != NULL) {
                        props.insert(string(str));
                }
//                cout.precision(7);
//                cout << answ(head, props) << endl;
                sprintf(buf,"%9f",answ(head, props));
                cout<<buf<<endl;
        }
        delete head;
}

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
        cin.ignore();
	for( int i = 0; i < N; ++i ) {
                cout << "Case #" << i+1 << ":\n";
                solve();
	}
	return 0;
}
//--------------------------------------------------------------------------- 
