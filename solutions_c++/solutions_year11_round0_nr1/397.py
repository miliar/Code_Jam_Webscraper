#include <iostream>
#include <cmath>
using namespace std;

int main(){
	freopen("A-Large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T,N;
	cin>>T;

	for(int t = 0; t < T; ++ t)
	{
		cin>>N;
		int begino = 1, beginb = 1;
		int s = 0;
		int on = 0,bn = 0,odata[100][2],bdata[100][2];
		for(int n = 0; n < N; ++ n)
		{
			char ch;
			int p;
			cin>>ch>>p;
			if (ch == 'O'){
				odata[on][0] = p;
				odata[on][1] = n;
				++ on;
			}
			else{
				bdata[bn][0] = p;
				bdata[bn][1] = n;
				++ bn;
			}
		}

		int res = 0;
		int con = 0,cbn = 0,cn = 0;
		int po = 1,pb = 1;
		while(true){
			bool pushbutton = false;
			if (con < on)
			if (po < odata[con][0]) ++ po;
			else if (po > odata[con][0]) --po;
			else{
				if (odata[con][1] == cn){
					++ cn;
					++ con;
					pushbutton = true;
				}
			}
			if (cbn < bn)
			if (pb < bdata[cbn][0]) ++pb;
			else if (pb > bdata[cbn][0]) --pb;
			else{
				if (bdata[cbn][1] == cn && !pushbutton){
					++ cn;
					++ cbn;
				}
			}
			++ res;
			if (cn == N) break;
		}
		cout<<"Case #"<<t + 1<<": "<<res<<endl;
	
	}
	return 0;
}