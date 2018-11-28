

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
#define PB push_back
#define PF push_front
#define All(V) (V).begin(), (V).end()
#define TOUT(V) copy(V.begin(), V.end(), ostream_iterator<string>(fout, "\n"));
#define SOUT(V) copy(V.begin(), V.end(), ostream_iterator<string>(cout, "\n"));
#define DOUT(V) copy(V.begin(), V.end(), ostream_iterator<double>(cout, " "));
#define IOUT(V) copy(V.begin(), V.end(), ostream_iterator<int>(cout, " "));

using namespace std;

void sol()
{
    ifstream fin("C:\\Users\\jrying\\Downloads\\B-large.in");
    ofstream fout("C:\\Users\\jrying\\Downloads\\B-large.out");

//    ifstream fin("C:\\Users\\jrying\\Downloads\\B-small-attempt0.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\B-small.out");

//    ifstream fin("C:\\Users\\jrying\\Downloads\\B-test.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\B-test.out");

    int T;
    fin >> T;
    F0M(i,T)
    {
        long long L, t, N, C;
        fin>>L>>t>>N>>C;
        vector<int> D;
        F0M(j,C)
        {
            int s;
            fin>>s;
            D.PB(s);
        }
        vector<long long> av;
        long long total = 0;
        bool ok = 0;
        F0M(j,N)
        {
            int cur=D[j%C];
            total += cur;
            if(total > t/2)
            {
                if(!ok){av.push_back(total-t/2); ok=1;}
                else av.push_back(cur);
            }
//
        }
        sort(All(av));
        long long ded = 0;
        for(int i = 0; i < L && i < av.size(); i++) {ded+=av[av.size()-i-1];}
        long long  result = total*2 - ded;

        fout<<"Case #"<<i+1<<": "<<result <<endl;

    }
}


int main()
{

    sol();
    return 0;
}
