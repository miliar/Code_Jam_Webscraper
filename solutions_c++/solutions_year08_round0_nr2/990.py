#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

struct Ttrip
{
    int t1,t2;
};

struct Ttime
{
    int time,k,d;
};

bool TimeCompare(Ttime a, Ttime b)
{
    if(a.time<b.time)
        return true;
    if(a.time>b.time)
        return false;
    if(a.d>b.d)
        return true;
    else
        return false;
}

int main()
{
    int i_test,n_test;
    int i,j,t,NA,NB;
    vector <int> trains;
    vector <Ttrip> tA,tB;
    vector <Ttime> time;
    int res[3],A,B;
    Ttrip q;
    Ttime w;
    int h1,m1,h2,m2;
    char c;
    ifstream fin("b.in");
    ofstream fout("b.out");
    fin >> n_test;
    for(i_test=0;i_test<n_test;i_test++)
    {
        tA.clear();
        tB.clear();
        time.clear();
        fin >> t >> NA >> NB;
        for(i=0;i<NA;i++)
        {
            fin >> h1 >> c >> m1 >> h2 >> c >> m2;
            m1+=h1*60;
            m2+=h2*60;
            q.t1=m1;
            q.t2=m2;
            tA.push_back(q);
            w.time=m1;
            w.k=1;
            w.d=-1;
            time.push_back(w);
            w.time=m2+t;
            w.k=2;
            w.d=1;
            time.push_back(w);
        }
        for(i=0;i<NB;i++)
        {
            fin >> h1 >> c >> m1 >> h2 >> c >> m2;
            m1+=h1*60;
            m2+=h2*60;
            q.t1=m1;
            q.t2=m2;
            tB.push_back(q);
            w.time=m1;
            w.k=2;
            w.d=-1;
            time.push_back(w);
            w.time=m2+t;
            w.k=1;
            w.d=1;
            time.push_back(w);
        }
        
        // sort vector time by time
        sort(time.begin(),time.end(),TimeCompare);
        
        res[0]=0;
        res[1]=0;
        res[2]=0;
        A=0;
        B=0;
        for(i=0;i<time.size();i++)
        {
            res[time[i].k]+=time[i].d;
            if(res[1]<A) A=res[1];
            if(res[2]<B) B=res[2];
        }
        fout << "Case #" << i_test+1 << ": " << abs(A) << " " << abs(B) << endl;
    }
    cout << "END";
//    cin >> i;
    return 0;
}
