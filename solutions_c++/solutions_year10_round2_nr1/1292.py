
#include <iostream>
#include <string>
#include  <cmath>
#include  <fstream>
#include <vector>
#include <map>
using namespace std;
vector <string> nodes;
void spiltstring(string s)
{
   int i=1;
   int st=1;
   while(st!=string::npos){
	   int k=s.find_first_of('/',st);
	   if(k==0){
		   k=string::npos;
		   st=k;
	   }
	   else{st=k+1;}
	   string t=s.substr(0,k);
	   for(i=0;i<nodes.size();i++){
		   if(nodes.at(i)==t){break;}
	   }
	   if(i>=nodes.size()){
		   nodes.push_back(t);
	   }
   }

}
int  getcount(string s)
{
	int st=1;
	int i;
	int count=0;
	while(st!=string::npos){
		int k=s.find_first_of('/',st);
		if(k==string::npos){
			k=string::npos;
			st=k;
		}
		else{st=k+1;}
		string t=s.substr(0,k);
		for(i=0;i<nodes.size();i++){
			if(nodes.at(i)==t){break;}
		}
		if(i>=nodes.size()){
			nodes.push_back(t);
			count++;
		}
	}
	return count;
}
int  main()
{
    ifstream cin("A-large.in");
    ofstream fout("programbig.out");
    int out_case_num=1;
    int case_num;
    int n,m,i;
    string s;
	cin>>case_num;
    while(case_num--){
        nodes.clear();
        cin>>n>>m;
        fout<<"Case #"<<out_case_num<<": ";
        out_case_num++;
        for(i=0;i<n;i++){
            cin>>s;
            spiltstring(s);
        }
        int count=0;
        for(i=0;i<m;i++){
            cin>>s;
            count+=getcount(s);
        }
        fout<<count<<endl;
    }
    return 0;

}
