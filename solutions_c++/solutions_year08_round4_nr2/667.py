#include <iostream>
using namespace std;

int main(){

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out.txt","w",stdout);

	int C;
	cin>>C;
	int cases;

	for(cases = 1; cases<=C; ++ cases ){
	
		int N,M,A;
		cin>>N>>M>>A;
		int x1,y1,x2,y2;
		int ans[4];
		bool ok=false;
		
		for(x1=0;x1<=N&&!ok;++x1)
			for(x2=0;x2<=N&&!ok;++x2)
				for(y1=0;y1<=M&&!ok;++y1)
					for(y2=0;y2<=M&&!ok;++y2){
					
						int AB=x1*x2+y1*y2;
						
						int Am=x1*x1+y1*y1;
						int Bm=x2*x2+y2*y2;
						if(A*A==Am*Bm-AB*AB)
						{
							ok=true;
							ans[0]=x1;
							ans[1]=y1;
							ans[2]=x2;
							ans[3]=y2;

						}

					}
					
					x1=ans[0];
					y1=ans[1];
					x2=ans[2];
					y2=ans[3];
		if(ok)
			cout<<"Case #"<<cases<<": 0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
		else
			cout<<"Case #"<<cases<<": IMPOSSIBLE"<<endl;

	}


	return 0;
}