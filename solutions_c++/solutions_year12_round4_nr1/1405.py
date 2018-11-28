#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <map>
using namespace std;

vector<int> indapos ;
vector<int> indahossz ;

map<pair<int, int>, int> memo ; // 1 : ok, 2 : nem ok
// num: inda sorszáma, amit elkaptunk
// dist: előző inda távolsága tőle
bool start(int num, int dist)
{
    pair<int, int> p = make_pair(num, dist) ;
    if (memo.find(p) != memo.end())
    {
        return memo[p]==1 ;
    }
 //   cout << num << " " << dist << endl ;
    if (num == indapos.size()-1)
    {
        memo[p] = 1 ;
        return true ;
    }
    for (int i = num+1; i < indapos.size(); ++i)
//    for (int i = indapos.size()-1; i >= num+1; --i)
    {
        if (indapos[i]-indapos[num] > dist)
        {
            memo[p] = 2 ;
            return false ;
        }
        if (start(i, min(indapos[i]-indapos[num], indahossz[i])))
        {
            memo[p] = 1 ;
            return true ;
        }
    }
    memo[p] = 2 ;
    return false ;
}

int main()
{
    ifstream bef("a.in") ;
    ofstream kif("a.out") ;
    int db ;
    bef >> db >> ws ;

    for (int testcase = 1; testcase <= db; testcase++)
    {
        memo.clear() ;
        int indaszam ;
        bef >> indaszam ;
        indapos.resize(indaszam+2) ;
        indahossz.resize(indaszam+2) ;
        indapos[0] = 0 ;
        indahossz[0] = 0 ; // nem számít
        for (int i = 0; i < indaszam; ++i)
        {
            bef >> indapos[i+1] ;
            bef >> indahossz[i+1] ;
        }
        bef >> indapos[indaszam+1] ; // lány
        indahossz[indaszam+1] = 0 ;
 //       cout << endl ;
        if (start(1, indapos[1]))
        {
            kif << "Case #" << testcase << ": " << "YES" << endl ;
        }
        else
        {
            kif << "Case #" << testcase << ": " << "NO" << endl ;
        }

    }
}
