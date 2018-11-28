#include<iostream>
#include<limits>



using namespace std;

typedef unsigned long UL;

const UL max_k=51;

const UL inv=numeric_limits<UL>::max();


UL d[max_k][max_k];
UL k;

UL entry(const UL ox, const UL oy, const UL i, const UL j)
{
	if(ox <= i && i < ox+k && oy <= j && j < oy+k)
		return d[i-ox][j-oy];
	else return inv;
}

bool possible(UL z) //can d be fit in a doubly symmetric z \times z matrix?
{
	if(z < k)
		return false;
	for(UL ox=0; ox<=z-k; ++ox)
	for(UL oy=0; oy<=z-k; ++oy) //try to fit with this offset
	{
		//for all entries (i,j) of the z \times z matrix, the following entries must be equal: (i,j), (j,i), (z-1-j, z-1-i), (z-1-i,z-1-j)
		//Check only for i<=z/2+2
		for(UL i=0; i<=min(z/2+2, z-1); ++i)
		for(UL j=0; j<z; ++j)
		{
			UL q = entry(ox,oy,i,j);
			UL tmp = entry(ox,oy,j,i);
			if(q != inv && tmp != inv && q != tmp) goto NEXT_OFFSET;
			if(q == inv) q = tmp;
			
			tmp = entry(ox,oy,z-1-j,z-1-i);
			if(q != inv && tmp != inv && q != tmp) goto NEXT_OFFSET;
			if(q == inv) q = tmp;
			
			tmp = entry(ox,oy,z-1-i,z-1-j);
			if(q != inv && tmp != inv && q != tmp) goto NEXT_OFFSET;
			if(q == inv) q = tmp;
			
		}
		return true; //all checks passed, offset (ox,oy) works
		NEXT_OFFSET:
		;
	}
	return false; //could not find any good offset
}

int main()
{
	UL ntests;
	cin>>ntests;
	for(UL tt=1; tt<=ntests; ++tt)
	{
		//cerr<<"CASE "<<tt<<" BEGIN\n";
		cin>>k;
		for(UL s=0; s<=2*k-2; ++s)
			for(UL i=0; i<k; ++i)
				if(i<=s && s<i+k)
					cin>>d[i][s-i];
		//(L,U]
		UL L = (k-1)/2, U = (4*k+3)/2;
		while(U-L > 1)
		{
			const UL mid = (U+L)/2;
			if(possible(2*mid) || possible(2*mid+1))
				U=mid;
			else
				L=mid;
		}
		UL ans = (possible(2*U)? (2*U) : 2*U+1);
		if(k==1)
			ans=1;
		cout<<"Case #"<<tt<<": "<<(ans*ans - k*k)<<'\n';
	}
}
