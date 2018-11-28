#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#define f(x,y) for(int x=0;x<y;x++)
#define pb push_back
#define mp make_pair
#define All(x) x.begin(),x.end()
using namespace std;

typedef long long int LL;
typedef vector<int> vi;

int main()
{
    //FILE *fin=fopen("A-small.in","w");
	//FILE *fout=fopen("A-small.out","w");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	LL T=0,N=0,K=0;
	fin>>T;
	cout<<T<<endl;
	f(i,T)
	{
        fin>>N>>K;
        LL p=(int)round(pow(2.0,double(N)));
        //cout<<N<<" "<<K<<" "<<(int)round(pow(2.0,double(N)))<<endl;
        if(K%p==p-1)
        {
            cout<<"Case #"<<i+1<<": ON"<<endl;
            fout<<"Case #"<<i+1<<": ON"<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": OFF"<<endl;
            fout<<"Case #"<<i+1<<": OFF"<<endl;
        }
    }
	
    cout<<"End."<<endl;
	cin.get();
	return 0;
}
