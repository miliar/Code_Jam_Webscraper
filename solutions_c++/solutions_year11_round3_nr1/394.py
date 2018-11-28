
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
//copy(v.begin(), v.end(), ostream_iterator<string>(cout, "\n"));

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
        int H, W;
        fin >> H >> W;
        vector<string> floor;
        F0M(j,H)
        {
            string s;
            fin>>s;
            floor.PB(s);
        }

        bool posb = 1;
        F0M(h,H)
        {
            F0M(w,W)
            {
                if(floor[h][w] == '#')
                {
                    if(h == H-1 || w == W-1){posb = 0;break;}
                    else if(floor[h+1][w] == '#' && floor[h][w+1] == '#' && floor[h+1][w+1] == '#')
                    {
                        floor[h][w] = '/';
                        floor[h+1][w] = '\\';
                        floor[h+1][w+1] = '/';
                        floor[h][w+1] = '\\';
                    }
                    else {posb = 0;break;}
                    //SOUT(floor);
                }
            }
            if(!posb)break;
        }

        fout<<"Case #"<<i+1<<": " <<endl;
        if(!posb)fout<<"Impossible"<<endl;
        else TOUT(floor);

    }
}



int main()
{
    sol();
}
