/*
TASK: first
LANG: C++
*/
#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#include <map>
#include <algorithm>
#define foreach(_v,_c) for( typeof((_c).begin()) _v = (_c).begin() ; _v != (_c).end() ; ++_v )

using namespace std;

int dircount;

struct Directory{
    string name;
    map<string,Directory> next;
    
    void addPath( string path ){
        string myname = "";
        int at = 1;
        while( at < path.size() and path[at] != '/' ){
            myname += path[at];
            ++at;
        }
        
        //cout << "Directory is :: " << myname << endl;
        
        string rest = path.substr(at);
        
        //cout << "Rest of the path is " << rest << endl;
        
        if( next.find( myname ) == next.end() ){
            next[myname];
            ++dircount;
        }
        
        if( rest == "/" or rest == "" ){
            return;/// nothing to do
        }else{
            next[myname].addPath( rest );
        }
    }
};

int T;

int main(){
	freopen("first.in","r",stdin);
	freopen("first.out","w",stdout);
	
	cin >> T;
	
	//printf("%d tests in total\n", T);
	
	for( int i = 0 ; i < T ; i++ ){
        int N,M;
        Directory root;
        root.name="";
        cin >> N >> M;
        
       // printf("Test %d , N = %d , M = %d\n" , i+1 , N , M );
        
        cin.ignore();
        
        for( int j = 0 ; j < N ; j++ ){
            string path;
            getline(cin,path);
            //cout << "Path is " << path << endl;
            
            root.addPath( path );
        }
        
       // cout << "Dir count is " << dircount << endl;
        
        dircount = 0;
        
        for( int j = 0 ; j < M ; j++ ){
            string path;
            getline(cin,path);
            //cout << "Path2add is " << path << endl;
            
            root.addPath(path);
        }
        
        //cout << "Test case#" << i+1 << " is " << dircount << endl;
        cout << "Case #"<<i+1<<": "<< dircount << endl;
	}
	return 0;
}
