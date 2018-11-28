#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define Pi acos(-1.0)
#define Eps (1e-9)
#define pb push_back
#define mp make_pair
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define sqr(a) ((a)*(a))
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
string arr[30]={"","027","143","751","935","607","903","991","335","047","943","471","055","447","463","991","095","607","263","151","855","527","743","351","135","407","903","791","135","647"};
int main()
{
	freopen("F.in","r",stdin);
	freopen("F.out","w",stdout);
	int T,ind=0;
	cin>>T;

	while(T)
	{
		T--;
		ind++;
		int n;
		cin>>n;
		cout<<"Case #"<<ind<<": "<<arr[n-1]<<endl;
	}
	return 0;
}

