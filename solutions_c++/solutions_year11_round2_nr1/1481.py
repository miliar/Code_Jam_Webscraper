
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
#define SOUT(v) copy(v.begin(), v.end(), ostream_iterator<string>(cout, " "));
#define DOUT(v) copy(v.begin(), v.end(), ostream_iterator<double>(cout, " "));
#define IOUT(v) copy(v.begin(), v.end(), ostream_iterator<int>(cout, " "));

using namespace std;

void sol()
{
    ifstream fin("C:\\Users\\jrying\\Downloads\\A-large.in");
    ofstream fout("C:\\Users\\jrying\\Downloads\\A-large.out");

//    ifstream fin("C:\\Users\\jrying\\Downloads\\A-small-attempt0.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\A-small.out");

//    ifstream fin("C:\\Users\\jrying\\Downloads\\A-test.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\A-test.out");

    int N;
    fin >> N;
    F0M(i,N)
    {
        int L;
        fin >> L;
        vector<string> rec;
        vector<int> opp;
        vector<int> win;
        vector<double> wp;
        vector<double> owp;
        vector<double> oowp;

        fout<<"Case #"<<i+1<<":" <<endl;

        F0M(j,L)
        {
            string str;
            fin>>str;
            rec.PB(str);
            opp.PB(L-(int)count(str.begin(),str.end(),'.'));
            win.PB((int)count(str.begin(),str.end(),'1'));
            wp.PB((double)win[j]/opp[j]);
        }

        F0M(t, L)
        {
            double temp = 0;
            F0M(o, L)
            {
                if(rec[o][t] != '.')temp+=((double)win[o]-rec[o][t]+'0')/(opp[o]-1);
            }
            owp.PB(temp/opp[t]);
        }
        F0M(t, L)
        {
            double temp = 0;
            F0M(o, L)
            {
                if(rec[o][t] != '.')temp+=(owp[o]);
            }
            oowp.PB(temp/opp[t]);
            fout<<setprecision(12)<<wp[t]*0.25+owp[t]*0.5+oowp[t]*0.25<<endl;
        }
//        DOUT(wp);
//        cout<<endl;
//        DOUT(owp);
//        cout<<endl;
//        IOUT(opp);
//        cout<<endl;

    }
}



int main()
{
    sol();
}

//
//2
//3
//.10
//0.1
//10.
//4
//.11.
//0.00
//01.1
//.10.
