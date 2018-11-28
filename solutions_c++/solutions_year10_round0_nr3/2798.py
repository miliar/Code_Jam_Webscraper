#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<map>
//#include<conio.h>

using namespace std;

//------------------------------------------------------------------------------------------
#if defined(_MSC_VER) && (_MSC_VER <= 1200)

// Overwrite global operators << and >> for MSVC 6.0 with 64-bit integer type.
inline std::ostream& operator<<(std::ostream& os, const __int64& n)
{
	char c[20];
	::_i64toa(n, c, 10);
	return os << c;
}

inline std::istream& operator>>(std::istream& is, __int64& n)
{
	char c[20];
	is >> c;
	n = ::_atoi64(c);
	return is;
}

#endif // IOstream fix for MSVC6
//------------------------------------------------------------------------------------------



#define MAX(A,B) (((A)>(B))?(A):(B))
#define MIN(A,B) (((A)<(B))?(A):(B))
#define SZ 1000
#define all(c) (c).begin(),(c).end()

typedef __int64 I64;

typedef struct 
{
	int ind,cost;
}type;

type my_arr[SZ];

int main()
{
	freopen("C-small-attempt0.in","r+",stdin);
	freopen("C.out","w+",stdout);
	
	vector<int> V;
	int i,j;
	int arr[SZ];

	int T,cse=1,R,K,N;
	
	cin >> T;
	while(T--)
	{
		cin >> R >> K >> N;
		for(i=0;i<N;i++) { cin >> arr[i]; my_arr[i].ind=0; }
		
		int cost,ind=1,grps;
		i=0;
		while(my_arr[i].ind == 0)
		{
			my_arr[i].ind=ind++;
			for(grps=0,cost=0,j=i%N;grps<N && (cost+arr[j])<=K;j=(j+1)%N)
			{
				cost+=arr[j];
				grps++;
			}
			my_arr[i].cost=cost;
			V.push_back(i);
			i=j;
		}
		
		int first,last,iter;
		first=my_arr[i].ind;
		last=ind-1;
		iter=ind-first;

		I64 sum=0;
		if(R<=(first-1))
		{
			for(i=0;i<R;i++)
				sum+=my_arr[V[i]].cost;	
			cout << "Case #" << cse++ << ": " << sum << endl;
			V.erase(all(V));
			continue;
		}
		else if((first-1)<R && R<=last)
		{
			for(i=0;i<(first-1);i++)
				sum+=my_arr[V[i]].cost;
			for(i=first-1;i<R;i++)
			{
				sum+=(((R-my_arr[V[i]].ind)/iter + 1)*my_arr[V[i]].cost);
			}	
			cout << "Case #" << cse++ << ": " << sum << endl;
			V.erase(all(V));
			continue;
		}
		else
		{
			for(i=0;i<(first-1);i++)
			sum+=my_arr[V[i]].cost;
			for(i=first-1;i<last;i++)
			{
				sum+=(((R-my_arr[V[i]].ind)/iter + 1)*my_arr[V[i]].cost);
			}
			cout << "Case #" << cse++ << ": " << sum << endl;

			V.erase(all(V));	
		}
	}


	
	return 0;
}

