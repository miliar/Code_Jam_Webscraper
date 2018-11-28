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

#define F0M(I,MAX) for(int I=0;I!=MAX;++I)
#define FPM(I,P,MAX) for(int I=P;I!=MAX;++I)
#define MAX(x,y, z)(((MAX(x,y))>(z))?(((MAX(x,y)):(z)))
#define MIN(x,y, z)(((MIN(x,y))<(z))?(((MIN(x,y)):(z)))
#define MAX(x,y)(((x)>(y))?(x):(y))
#define MIN(x,y)(((x)<(y))?(x):(y))

using namespace std;

int searchNext(vector<char> &B, vector<int> &P, int pos, int l, char target)
{
    FPM(i,pos,l)
    {
        if(B[i] == target)return P[i];
    }
    return -1;
}

void botTrust()
{
    ifstream fin("C:\\Users\\jrying\\Downloads\\A-small-attempt0.in");
    ofstream fout("C:\\Users\\jrying\\Downloads\\A-small.out");

//    ifstream fin("C:\\Users\\jrying\\Downloads\\A-test.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\A-test.out");

    int N;
    fin >> N;
    F0M(i,N)
    {
        vector<char> B;
        vector<int> P;
        int L;
        fin >> L;
        B.resize(L);
        P.resize(L);
        F0M(j,L)
        {
            fin>>B[j]>>P[j];
        }
        int pb = 0, po = 0;
        int tb = searchNext(B, P, 0, L, 'B'), to = searchNext(B, P, 0, L, 'O');

        int result = 0;
        int press = 0;
        while(press != L)
        {
            char next = B[press];
            if(next =='O' && po == to){++press; to = searchNext(B, P, press, L, 'O');}
            else if(po != to)po+=po>to?-1:1;
            if(next =='B' && pb == tb){++press; tb = searchNext(B, P, press, L, 'B');}
            else if(pb != tb)pb+=pb>tb?-1:1;
            if(press != L)result++;
            //fout<<po<<" "<<pb<<endl;
        }
        fout<<"Case #"<<i+1<<": " <<result<<endl;

    }
}

int main()
{
    botTrust();

}
