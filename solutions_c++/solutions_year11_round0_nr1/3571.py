#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
	int T;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	int count = 1;
	while ( T-- ){
		int N;
		cin>>N;
		int times = 0,pre = 0;
		char temp;
		int pos[120];
		int OB[120];
		int current[2] = {1,1};
		for (int i = 0; i < N; i++ ){
			cin>>temp>>pos[i];
			if ( temp == 'O' ) OB[i] = 0;
			else OB[i] = 1;
		}
		for ( int i = 0; i < N; i++ ){
			if ( i != 0 && OB[i] == OB[i-1] ){
				pre = abs(pos[i] - current[ OB[i] ]) + 1 + pre;
				times = times + abs(pos[i] - current[ OB[i] ]) + 1;
			}
			else{
				if ( pre > abs( pos[i] - current[ OB[i] ])){
					pre = 1;
					times+=pre;
				}
				else{
					pre = abs(pos[i] - current[ OB[i] ]) - pre + 1;
					times+=pre;
				}
			}
			current[ OB[i] ] = pos[i];
		}
		cout<<"Case #"<<count++<<": "<<times<<endl;
	}
	return 0;
}