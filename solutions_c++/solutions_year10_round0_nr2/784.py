#include <iostream>
using namespace std;

int N;
long t[10];
long r[10];
long ans;
long Minum;
long Maxnum;

int main()
{
	freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
	int Test;
	cin>>Test;
	
	for (int cas = 1; cas <= Test; ++cas) {
		cout <<"Case #"<<cas<<": ";
		cin>>N;
		for (int i = 0; i < N; ++i) {
			cin>>t[i];
			if (i == 0) {
				Minum = t[i];
				Maxnum = t[i];
				continue;
			}
			if (t[i] < Minum) {
				Minum = t[i];
			}
			if (t[i] > Maxnum) {
				Maxnum = t[i];
			}
		}
		int i;
		
		while (1) {
			for ( i = 0; i < N; ++i) {
				r[i] = t[i]%Maxnum;
			}
			for ( i = 1; i < N; ++i) {
				if (r[i] != r[i-1])
					break;
			}
			if (i == N)
				break;
			--Maxnum;
		}
		
		if (Maxnum == Minum || Maxnum == 1) {
			cout<<0<<endl;
		}
		else
			//t[0]%T==0?0:T-t[0]%T
			cout<<( ((t[0]%Maxnum)==0)?0:(Maxnum-(t[0]%Maxnum)) )<<endl;
	}
	return 0;
}
