#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>

using namespace std;

#define F(i,a,b) for(i=a;i<=b;++i)

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	long t,n,cs=1,i;
	long bp,bt,op,ot,times;
	long x; string s;

	cin >> t;

	while(t--){
		cin >> n;
		bp = op = 1;
		bt = ot = 0;
		long last = -1,lt=0,rem;
		times = 0;

		F(i,1,n){
			cin >> s >> x;
			if(s=="B"){
				if(last==1){
					
					// free
					rem = times - bt;
					if(rem>0){
						if(x<bp){
							bp -= rem;
							if(bp<x)
								bp = x;
						}
						else{
							bp += rem;
							if(bp>x)
								bp = x;
						}
					}
				}

				if(bp>x) times += bp-x+1;
				else times += x-bp+1;
					
				bt = times;
				bp = x;
				last = 0;
			}
			else{

				// free
				if(last==0){
					rem = times - ot;
					if(rem>0){
						if(x<op){
							op -= rem;
							if(op<x)
								op = x;
						}
						else{
							op += rem;
							if(op>x)
								op = x;
						}
					}
				}

				if(op>x) times += op-x+1;
				else times += x-op+1;
				
				ot = times;
				op = x;
				last = 1;
			}

			//printf("%d %d - %d %d @ %d\n",bp,bt,op,ot,times);
		}

		if(ot>bt) x = ot;
		else x = bt;

		cout << "Case #" << cs << ": "; ++cs;
		cout << times << endl;
	}

	return 0;
}