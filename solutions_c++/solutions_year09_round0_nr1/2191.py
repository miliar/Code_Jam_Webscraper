#include<iostream>
#include<fstream>
#include<vector>
#include<set>
#include<string>
using namespace std;

int L,D,N;
string words[5001];
struct pattern
{
    set<char> a[16];
};

pattern pt[500];

string tmp;

int main()
{
    ifstream in("A-large.in");
    in>>L>>D>>N;
    for(int i=0;i<D;i++){
        in>>words[i];        
    }
    for(int i=0;i<N;i++){
        in>>tmp;
        int i_p=0;
        bool is_p=false;
        for(int j=0;j<tmp.size();j++){
            if(tmp.at(j)=='('){
                is_p=true;
            }else if(tmp.at(j)==')'){
                is_p=false;
                i_p++;
            }else{
                pt[i].a[i_p].insert(tmp.at(j));
                if(is_p==false)
                    i_p++;
            }
        }        
    }

    for(int i=0;i<N;i++){
        int sum=0;
        for(int j=0;j<D;j++){
            bool is_pt=true;
            for(int k=0;k<words[j].size();k++){
                if(pt[i].a[k].find(words[j].at(k))==pt[i].a[k].end()){
                    is_pt=false;
                    break;
                }
            }
            if(is_pt==true)
                sum++;
        }
        cout<<"Case #"<<(i+1)<<": "<<sum<<endl;
    }
    return 0;
}
