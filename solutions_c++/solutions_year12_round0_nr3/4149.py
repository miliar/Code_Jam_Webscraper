#include <iostream>
#include <set>
using namespace std;

const int MAXn=2e6+10;
int p[MAXn];

int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	p[0]=1;
	for(int i = 1; i <= MAXn; i++)
		p[i]=p[i/10]*10;
	for(int t = 1; t <= T; t++)
	{
		int a, b;
		cin >> a >> b;
		int count=0;
		for(int i = a; i <= b; i++)
		{
			int c=10;
			set<int> st; st.clear();
			while(c<i)
			{
				int r=i%c;
				if(r>=c/10)
				{
					int q=r*(p[i]/c)+i/c;
					if(q>i&&q<=b) st.insert(q);
				}
				c*=10;
			}
			count+=st.size();
		}
		cout << "Case #" << t << ": " << count << endl;
	}
	return 0;
}
