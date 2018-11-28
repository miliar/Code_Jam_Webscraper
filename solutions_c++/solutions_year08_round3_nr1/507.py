#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Tv
{
    int i;
    long long k;
};

bool operator<(Tv a, Tv b)
{
    return a.k<b.k;
}

int main()
{
    int i,i_test,j;
    vector <Tv> a;
    vector <long long> res;
    long long N,P,L,K;
    Tv q;
    long long min;
    long long max;
    ifstream fin("a.in");
    ofstream fout("a.out");
    fin >> N;
    for(i_test=0;i_test<N;i_test++)
    {
        a.clear();
        res.clear();
        max=0;
        fin >> P >> K >> L;
        for(i=0;i<K;i++)
            res.push_back(0);
        for(i=0;i<L;i++)
        {
            fin >> q.k;
            q.i=i;
            a.push_back(q);
        }
        sort(a.begin(),a.end());
        for(i=a.size()-1;i>=0;i--)
        {
            min=0;
            for(j=1;j<res.size();j++)
            {
                if(res[j]<res[min]) min=j;
            }
            res[min]++;
            max+=res[min]*a[i].k;
        }
        fout << "Case #" << i_test+1 << ": " << max << endl;
    }
    
    return 0;
}
