#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
#include<numeric>
using namespace std;
#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef vector<int> vi;
int main(){
	int T;
	cin>>T;
	REP(i,T){
		int N;
		cin>>N;
		vi v(N);
		REP(j,N) cin>>v[j];
		long long int total;
		total = accumulate(v.begin(),v.end(),0);
		//cout<<total<<" ";
		long long int x=0,high=-1;
		REP(j,N) x^=v[j];
		if(x) high = -1;
		else{
			high = total - (*min_element(all(v)));			
			}
		cout<<"Case #"<<i+1<<": ";
		if(high == -1)	cout<<"NO";
		else	cout<<high;
		cout<<endl;
		}
		
	return 0;
	}