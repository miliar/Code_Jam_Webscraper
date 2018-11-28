#include <iostream>
#include <vector>
using namespace std;
#define pb push_back
#define LL long long

LL area(int x1,int y1,int z1,int x2,int y2,int z2)
  {
    LL x11=(y1*z2-z1*y2);
    LL y11=(-x1*z2+z1*x2);
    LL z11=(x1*y2-x2*y1);
    //cerr<<" Area ="<<(x11*x11+y11*y11+z11*z11)<<"\n";
    return (x11*x11+y11*y11+z11*z11);
  }

LL ar(int x[3], int y[3])
{
	return area(x[1]-x[0],y[1]-y[0],0,x[2]-x[0],y[2]-y[0],0);
}


int main()
{
	int T;
	scanf("%d",&T);
	int c=0;
	while(T--)
	{
		int N,M,A;
		scanf("%d %d %d",&N,&M,&A);
		N++;M++;
		bool found = false;
			for(int j=0;j<N*M;j++)
				for(int k=0;k<N*M;k++)
				{
					//cout<<"Here\n";
					int x[3];
					int y[3];
					x[0] = 0;
					y[0] = 0;
					x[1] = j%N;
					y[1] = j/N;
					x[2] = k%N;
					y[2] = k/N;
					if( ar(x,y) == (LL) A * (LL) A)
					{
						cout<<"Case #"<<++c<<":";
						for(int h=0;h<3;h++)
							cout<<" "<<x[h]<<" "<<y[h];
						cout<<"\n";
						goto end;
					}

				}
		cout<<"Case #"<<++c<<": IMPOSSIBLE\n";
end:;
	}
	return 0;
}
