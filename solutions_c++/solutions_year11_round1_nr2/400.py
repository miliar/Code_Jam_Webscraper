#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>
#include<functional>
#include<set>
#include<sys/stat.h> 

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
const bool ENABLE_MULTI_PROCESS = false;
using namespace std;

//=========================================================
// program:
//
int N, M;
string dictionary[10000];
string list[100];
string result[100];

bool match (const string & guess, const string & word, const string& L, int x) {
    bool g = false;
    for (int i=0; i<guess.size(); i++) {
        for (int j=0; j<x; j++) {
            if ( (word[i] == L[j]) && (guess[i]!=word[i]) ) {
                return false;
            }
        }
        if ( (guess[i] != '?') && (guess[i] != word[i]) ) {
            return false;
        }
        g |= ( (guess[i]=='?') && (word[i]==L[x]) );
        if ( (word[i]==L[x]) && (guess[i]!='?') ) return false;
    }
    return g;
}

int simulate( const string & word, const string & L) {
    int n = word.size();
    string guess(n, '?');
    int points = 0;
    for (int i=0; i<26; i++) {
        
        bool choose = false;
        for (int j=0; j<N; j++) {
            if( n != dictionary[j].length() ) continue;
            if ( match(guess, dictionary[j], L, i) ) {
                choose = true;
            }
        }
        if ( choose ) {
            bool did = false;
            bool done = true;
            for (int j = 0 ; j < n; j++) {
                if ( word[j] == L[i] ) {
                    did = true;
                    guess[j] = L[i];
                }
                if ( guess[j] == '?' ) {
                    done = false;
                }
            }
            if (! did ) {
                //cout<<"["<<L[i]<<"]"<<guess;
                points --;
            } else {
                //cout<<"{"<<L[i]<<"}"<<guess;
            }
            
            if ( done ) break;
        }
        
    }
   //cout<<" = "<<guess<<endl;
    assert( count(guess.begin(), guess.end(), '?' ) == 0 );
    
    return points;
}

string solve(const string & L) {
    pair<int, int> best = make_pair(1, 0);
    for (int i = 0; i<N; i++) {
        int x = simulate( dictionary[i] , L );
        //cout<<L<<" "<<dictionary[i]<<" : " <<x<<endl;
        best = std::min(best, make_pair(x, i));
    }
    return dictionary[best.second];
    
}

void solve() {
    for (int i=0; i<M; i++) {
        result[i] = solve(list[i]);
    }
}

inline void init(){}
//=========================================================
// I/O:
//
int main(int argc, const char* argv[])
{
    int mode = 0;
    if(argc >= 2) sscanf(argv[1],"%d",&mode);
    if ( ( mode == 0 ) && ENABLE_MULTI_PROCESS )
    {
        string inputfile = ".input";
        system("cat > .input");
        /* I use a dual core CPU, so for long solutions I might use this
         multi-process thing, splitting the input in halves effectively
         halving execution time of slow solutions. But due to overhead it
         increases the time of fast solutions, so it is optional... */
        mode = 1;
        remove(".finished");
        cerr<<"--Multi process mode--"<<endl;
        //string inputfile = argv[2];
        string command = argv[0];
        command += " 2 < "+inputfile+" > .tem &";
        system(command.c_str());
        freopen(inputfile.c_str(),"r",stdin);
    }
    
    init();
    int TestCases;
    cin>>TestCases;

    for (int _i=1;_i<=TestCases;_i++)
    {
        /* read input goes here */
        cin >> N >> M;
        for (int i=0; i<N; i++) {
            cin >> dictionary[i];
        }
        for (int j=0; j<M; j++) {
            cin >> list[j];
        }
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<":";
            for (int i=0; i<M; i++) {
                cout<<" "<<result[i];
            }
            cout<<endl;
            
        }
        else if(mode!=2) break;
    }
    if(mode==2) system("echo done > .finished");
    else if(mode==1)
    {
        struct stat stFileInfo;
        while( stat(".finished",&stFileInfo)!=0);
        system("cat .tem");

    }
    return 0;
}
