#include <iostream>
#include <map>

using namespace std;

int main() {
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int N,j;
    cin>>N;
    for(j=1;j<=N;j++){
        int S,Q,i,level=0;
        bool ifany;
        string current;
        map<string,int> engines;
        cin>>S;
        for(i=0;i<=S;i++){
            getline(cin,current);
            if(i==0)
                continue;
            engines[current]=0;
        }
        cin>>Q;
        for(i=0;i<=Q;i++){
            //body
            string temp;
            getline(cin,temp);
            if(i==0)
                continue;
            engines[temp]=level+1;
            ifany=false;
            for(map<string,int>::iterator ii=engines.begin();ii!=engines.end();ii++)
                if((*ii).second==level){
                    ifany=true;
                    break;
                }
            if(!ifany){
                level++;
                engines[temp]=level+1;
            }
        }
        cout<<"Case #"<<j<<": "<<level<<"\n";
    }
	return 0;
}
