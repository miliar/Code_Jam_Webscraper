
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<climits>
#include<iomanip>
#include<iterator>

#define F0M(I,MAX) for(int I=0;I!=MAX;++I)
#define FPM(I,P,MAX) for(int I=P;I!=MAX;++I)
#define MAX(x,y,z)(((MAX(x,y))>(z))?(((MAX(x,y)):(z)))
#define MIN(x,y,z)(((MIN(x,y))<(z))?(((MIN(x,y)):(z)))
#define MAX(x,y)(((x)>(y))?(x):(y))
#define MIN(x,y)(((x)<(y))?(x):(y))
//copy(v.begin(), v.end(), ostream_iterator<string>(fout, "\n"));

using namespace std;


void candySplitting()
{

//    ifstream fin("C:\\Users\\jrying\\Downloads\\C-small-attempt0.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\C-small.out");

    ifstream fin("C:\\Users\\jrying\\Downloads\\C-large.in");
    ofstream fout("C:\\Users\\jrying\\Downloads\\C-large.out");

//    ifstream fin("C:\\Users\\jrying\\Downloads\\C-test.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\C-test.out");
    int N;
    fin>>N;
    F0M(i,N)
    {
        int T;
        fin>>T;
        int result = 0;
        int total = 0;
        int min = INT_MAX;
        F0M(j,T)
        {
            int k;
            fin>>k;
            result = result xor k;
            total += k;
            min = MIN(min, k);
        }
        if(result != 0)fout<<"Case #"<<i+1<<": NO"<<endl;
        else fout<<"Case #"<<i+1<<": "<<total-min<<endl;
    }
}


int main()
{
    candySplitting();
    return 0;
}
