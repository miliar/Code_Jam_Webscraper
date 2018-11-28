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
#define o(x) cout<<x<<endl
#define All(x) x.begin(),x.end()
using namespace std;

typedef long long int LL;
typedef vector<int> vi;

bool intersect(int a1,int b1,int a2,int b2)
{
    if((a1-a2>0)&&(b1-b2<0))return 1;
    if((a1-a2<0)&&(b1-b2>0))return 1;
    return 0;
};

int main()
{
	ifstream fin("a-large.in");
	ofstream fout("a-large.out");
	
	int T,N;
	fin>>T;
	f(i,T)
	{
        fin>>N;
        vector<int> a(N,0),b(N,0);
        f(j,N)fin>>a[j]>>b[j];
        
        int res=0;
        
        f(x,N-1)for(int y=x+1;y<N;y++)
        if(intersect(a[x],b[x],a[y],b[y]))res++;
        
        cout<<"Case #"<<i+1<<": "<<res<<endl;
        fout<<"Case #"<<i+1<<": "<<res<<endl;
    }
	
    cout<<"End."<<endl;
	cin.get();
	return 0;
}
