#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>

#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i=0; i<(int)(n); i++)

using namespace std;
typedef long long int tint;

int main(){
	ifstream in("a.in");
	ofstream out("a.out");
	
	int T, k=0;
	tint a, b, c;
	in>>T;
	while(k<T)
	{
	k++;
	in>>a>>b>>c;
	int res=1;
	out<<"Case #"<<k<<": ";
	if((c==100 && b!=100) || (c==0 && b!=0))res=0;
	//if(((a%100)*b)%100!=0)res=0;
	int i=1;
	while((b*i)%100!=0)i++;
	if((i>a) )res=0;
	if(res==0)out<<"Broken"<<endl;
	else out<<"Possible"<<endl;
	}
}
