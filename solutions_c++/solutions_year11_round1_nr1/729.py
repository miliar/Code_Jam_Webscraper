#include <iostream>
using namespace std;
typedef long long big;
big gcd(big a,big b){
	if(b==0) return a;
	else return gcd(b,a%b);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("tt.out","w",stdout);
	big T,d,g,n,cases=1;;
	cin >>T;
	while (T--)
	{
		cin >>n>>d>>g;
		if((g==100 && d!=100)||(g==0 && d!=0))
		{
			cout <<"Case #"<<cases++<<": Broken"<<endl;
			continue;
		}
		d=100/gcd(100,d);
		if(n>=d){
			cout <<"Case #"<<cases++<<": Possible"<<endl;
			continue;;
		}
		else{
			cout <<"Case #"<<cases++<<": Broken"<<endl;
			continue;
		}
	}
	return 0;
}