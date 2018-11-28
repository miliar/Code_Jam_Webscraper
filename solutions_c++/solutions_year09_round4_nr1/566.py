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
using namespace std;

//=========================================================
// program:
//
int N;
vector<string> board;

bool valid(const vector<string> cur, int a, int b)
{
    for (int i=a; i<=b; i++)
        for (int j=i+1; j<N; j++)
            if(cur[i][j]=='1')
                return false;
    /*cerr<<"This is valid:"<<endl;
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++) cout<<cur[i][j];
        cout<<endl;
    }*/
    return true;
}

int subProblem(vector<int> trans, vector<int> sorted)
{
    //cout<<"--"<<endl;
    int steps = 0;
    /*for (int i=0; i<N; i++) cout<<trans[i]<<" "; cout<<endl;
    for (int i=0; i<N; i++) cout<<sorted[i]<<" "; cout<<endl;*/
    for (int i=0; i<N; i++)
    {
/*    for (int ii=0; ii<N; ii++) cout<<trans[ii]<<" "; cout<<endl;
    for (int ii=0; ii<N; ii++) cout<<sorted[ii]<<" "; cout<<"*"<<endl;*/

        int good = -1;
        for (int j=i; j<N; j++)
        {
            if( trans[j] <= i+1 )
            {
                good=j;
                break;
            }
        }
        assert(good!=-1);
        steps += good-i;
        int g = trans[good];
        for (int j=good; j>i; j--)
            trans[j]=trans[j-1];
        trans[i]=g;
    }
    return steps;

}

int solve()
{
    int steps = 0;
    vector<int> trans(N);
    for (int i=0; i<N; i++)
    {
        trans[i] = N;
        while ( board[i][ trans[i]-1 ] == '0')
            trans[i]--;
    }
    vector<int> sorted = trans;
    sort(sorted.begin(), sorted.end());
    vector<int> s =sorted, t= trans;
    reverse(s.begin(), s.end() );
    reverse(t.begin(), t.end() );
    return /*std::min( subProblem(t,s),*/subProblem( trans,sorted) /*)*/ ;
    
    
}



inline void init(){}
//=========================================================
// I/O:
//
int main(int argc, const char* argv[])
{
    int mode = 0;
    if(argc >= 2) sscanf(argv[1],"%d",&mode);
    if (argc >= 3 )
    {
        /* I use a dual core CPU, so for long solutions I might use this
         multi-process thing, splitting the input in halves effectively
         halving execution time of slow solutions. But due to overhead it
         increases the time of fast solutions, so it is optional... */
        mode = 1;
        remove(".finished");
        cerr<<"--Multi process mode--"<<endl;
        string inputfile = argv[2];
        string command = argv[0];
        command += " 2 < "+inputfile+" > .tem &";
        system(command.c_str());
        freopen(inputfile.c_str(),"r",stdin);
    }
    
    init();
    int TestCases;
    cin>>TestCases;

    for (int i=1;i<=TestCases;i++)
    {
        cin >> N;
        board.resize(N);
        for (int j=0; j<N; j++)
        {
            board[j].resize(N,'0');
            for (int k=0; k<N; k++)
                cin>>board[j][k];
        }
        
        if( (mode==0) || ( (mode!=2)== (i*2<=TestCases) ) )
        {
            cerr<<"["<<i<<" / "<<TestCases<<"]"<<endl;
            cout<<"Case #"<<i<<": ";
            cout<<solve();
            cout  << endl;
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
