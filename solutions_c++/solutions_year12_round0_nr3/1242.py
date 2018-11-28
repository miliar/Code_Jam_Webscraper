# include <iostream>
# include <vector>
# include <map>
# include <deque>
# include <set>
# include <algorithm>
# include <memory>
# include <cstring>
# include <cstdio>
# include <cctype>
# include <cstdlib>
# include <cmath>
# include <utility>
# include <string>
# include <queue>

using namespace std;

# define I(n)   scanf("%d",&(n))
# define read(x) freopen(x,"r",stdin)
# define write(x) freopen(x,"w",stdout)

int nDigit(int x)
{
    int c=0;
    while( x ){
        x/=10;
        c++;
    }
    return c;
}

int rotate(int N,int d,int i){
    int p = N%((int)pow(10,i));
    N/=(int)pow(10,i);
    p*=(int)pow(10,d-i);
    return p+N;
}




int main()
{
	read("C-large.in");
	write("out.txt");
	int T,A,B;
	I(T);
	for(int cas=1;cas<=T;cas++)
	{
	    I(A);I(B);
	    int ans=0;
	    for(int i=A;i<=B;i++)
	    {
	        int d = nDigit(i);
	        set<int> m;
	        for(int j=1;j<d;j++){
	            int x = rotate( i , d , j );
	            if ( x > i && x <= B ) {
	                m.insert(x);
	            }
	        }
	        ans += m.size();
	    }
	    cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}
