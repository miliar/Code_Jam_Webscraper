#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <set>
using namespace std;

int doit(vector<string> q,vector<string> s){
    set<string> ss(s.begin(),s.end());
    int qi=-1,qs=0,ret=0;
    while(++qi < q.size() ){
               set<string> st(q.begin()+qs,q.begin()+qi+1);
               if( st == ss){
                   ret++;
                   qs = qi;
               }
    }
    return ret;
}
int main()
{
    int nt;
    ifstream input("sal.in");
	input >> nt ;
	int cas=0;
	ofstream output("sal.out");
	while(nt--){
                 int se;
                 input>>se;
                 vector<string> search;
                 string t;
                 //char t[105];
                 getline(input,t);
                 while(se--) {
                             getline(input,t);
                             //tt = t;
                             //in >> t;
                             search.push_back(t);
                             //cout<<"Se = "<<se<<" :"<<t<<endl;
                             //t.clear();
                 }
                 //getchar();
                 
                 vector<string> query;
                 int qu;
                 input>>qu;
                 getline(input,t);
                 while(qu--){
                             getline(input,t);
                             //tt = t;
                             query.push_back(t);
                             //cout<<"qu = "<<qu<<" :"<<t<<endl;
                 }
                 //cout<<"input done for case "<<cas+1<<endl;
                 
                 
                 int ret = doit(query,search)+1;
                 //int start = -1,last = -1;

               
               output << "Case #" << ++cas <<": " << ret-1 <<endl;
               
               //cout<< "output done for case "<< cas<<endl<<endl;
               
    }
    output.close();
    input.close();
    cout<<"done";
    getchar();
}


