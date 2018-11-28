#include<iostream>
#include<algorithm>
#include<functional>
#include<sstream>
#include<set>
using namespace std;

#define MAXN 31

int T, A ,B;

int ans;

char buf[MAXN];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d\n", &T);
	for(int te=1;te<=T;++te)
	{
		scanf("%d %d", &A, &B);
		ans = 0;
		for(int n=A;n<=B;++n)
		{
			stringstream ss;
			ss<<n;
			if(n>=10)
			{
				ss<<(n/10);
			}
			string exten = ss.str();
			int len = exten.length()/2 + 1;
			for(int j=0;j<len-1;++j)
			{
				set<int> mset;
				stringstream parser;
				parser<<ss.str().substr(j+1, len);
				int m;
				parser>>m;
				if(n<m && m<=B && mset.find(m)==mset.end())
				{
					//cout<<n<<','<<m<<endl;
					mset.insert(m);
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", te, ans);
	}
	return 0;
}
