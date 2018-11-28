#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

int main()
{
    ifstream input("B-large.in");
    ofstream output("1.txt");
    int total_case;
    input>>total_case;
    int temp_id;
    
    for(temp_id=1;temp_id<=total_case;++temp_id)
    {
       int N,S,p,temp;
       input>>N>>S>>p;
       vector<int> ivec;
       int i;
       for(i=1;i<=N;i++){
          input>>temp;
          ivec.push_back(temp);
          
          
          
       }
       sort(ivec.begin(),ivec.end());
          
       int a = ivec.end() - lower_bound(ivec.begin(),ivec.end(),max(p,3*p-2));
          
       int b = min(S,   (lower_bound(ivec.begin(),ivec.end(),max(p,3*p-2)) - lower_bound(ivec.begin(),ivec.end(), max(p,3*p-4) ) ));
       cout<<a<<endl;
       cout<<b<<endl;
       output<<"Case #"<<temp_id<<": ";
       
       output<<a+b;
       output<<endl;
    }
    cin>>temp_id;
}
