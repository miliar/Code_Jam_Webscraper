#include<iostream>
#include<vector>

using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

const UL pow2[]= {1UL<<0,1UL<<1,1UL<<2,1UL<<3,1UL<<4,1UL<<5,1UL<<6,1UL<<7,1UL<<8,1UL<<9,1UL<<10,1UL<<11,1UL<<12,1UL<<13,1UL<<14,1UL<<15,1UL<<16,1UL<<17,1UL<<18,1UL<<19,1UL<<20,1UL<<21,1UL<<22,1UL<<23,1UL<<24,1UL<<25,1UL<<26,1UL<<27,1UL<<28,1UL<<29,1UL<<30,1UL<<31};

bool get (const UL m, const int i) {return m & pow2[i];}
UL set1 (const UL m, const int i) {return m | pow2[i];}
UL set0 (const UL m, const int i) {return m & ~pow2[i];}

inline bool valid(const vector<char> &p, UL m)
{
	for(UL i=0; i<p.size(); ++i)
		if(p[i]=='x' && get(m, i))
			return false;
/*	for(UL i=0; i+1<p.size(); ++i)
		if(get(m, i) && get(m, i+1))
			return false;*/

	return true;
}

inline UL count(UL m, UL N)
{
	UL ans=0;
	for(UL i=0; i<N; ++i)
		if(get(m, i))
			++ans;
	return ans;
}

inline bool compat(UL b, UL f, UL N)
{
	for(UL i=0; i+1<N; ++i)
		if(get(b, i) && get(b, i+1))
			return false;
	for(UL i=0; i+1<N; ++i)
		if(get(f, i) && get(f, i+1))
			return false;
	for(UL i=0; i<N; ++i)
	{
		if(i>0 && get(b, i) && get(f, i-1))
			return false;
		if(i+1<N && get(b, i) && get(f, i+1))
			return false;
	}
	return true;
}

int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL M, N;
		cin>>M>>N;
		vector<vector<char> > z(M, vector<char>(N));
		for(UL i=0; i<M; ++i)
			for(UL j=0; j<N; ++j)
				cin>>z[i][j];
		vector<vector<UL> > C(M, vector<UL>(pow2[N]));
		for(UL m=0; m<pow2[N]; ++m)
			if(valid(z[0], m))
				C[0][m]=count(m, N);
			else
				C[0][m]=0;
		for(UL r=1; r<M; ++r)
		{
			for(UL mb=0; mb<pow2[N]; ++mb)
			{
				C[r][mb]=0;
				const UL cc=count(mb, N);
				if(valid(z[r], mb))
					for(UL mf=0; mf<pow2[N]; ++mf)
						if(valid(z[r-1], mf))
							if(compat(mb, mf, N))
								C[r][mb]=max(C[r][mb], C[r-1][mf] + cc);
			}
		}
		UL ans=0;
		for(UL m=0; m<pow2[N]; ++m)
			if(valid(z[M-1], m))
				ans=max(ans, C[M-1][m]);
		
		
		
		cout<<"Case #"<<tt<<": "<<ans<<'\n';
	}

}
