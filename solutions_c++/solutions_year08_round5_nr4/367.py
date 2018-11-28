#include<iostream>
#include<vector>

using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

const UL mod_val=10007;

const UL inv=numeric_limits<UL>::max();

int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL H, W, R;
		cin>>H>>W>>R;
		vector<vector<UL> >C(H, vector<UL>(W, inv));
		for(UL i=0; i<R; ++i)
		{
			UL r,c;
			cin>>r>>c;
			--r,--c;
			C[r][c]=0;
		}
		C[0][0]=1;
		for(UL i=0; i<H; ++i)
			for(UL j=0; j<W; ++j)
			{
				if(C[i][j]==0)
					continue;
				if(i !=0 || j!=0)
					C[i][j]=0;
				if(i>=2 && j>=1)
					(C[i][j]+=C[i-2][j-1])%=mod_val;
				if(i>=1 && j>=2)
					(C[i][j]+=C[i-1][j-2])%=mod_val;
			}
		cout<<"Case #"<<tt<<": "<<C[H-1][W-1]<<'\n';
	}

}
