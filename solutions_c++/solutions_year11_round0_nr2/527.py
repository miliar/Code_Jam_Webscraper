#include <iostream>
#include <memory>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	int C,D,N;
	int sta[26][26];
	int sta2[26][26];
	cin >> T;
	for(int i=0;i<T;i++)
	{
		memset(sta,0,sizeof(sta));
		memset(sta2,0,sizeof(sta2));
		char com[40];
		int p=1;
		char res[105];
		int rlenth=1;
		char a,b,co;
		cin >> C;
		for(int j=0;j<C;j++)
		{
			cin >> a >> b >> co;
			sta[int(a)-'A'][int(b)-'A'] = p;
			sta[int(b)-'A'][int(a)-'A'] = p;
			com[p] = co;
			p++;
		}
		cin >> D;
		for(int j=0;j<D;j++)
		{
			cin >> a >> b;
			sta2[int(a)-'A'][int(b)-'A'] = -1;
			sta2[int(b)-'A'][int(a)-'A'] = -1;
		}
		cin >> N;
		cin >> a;
		res[0] = a;
		int x;
		for(int j=1;j<N;j++)
		{
			cin >> a;
			if(rlenth > 0)
			{
				x = sta[int(res[rlenth-1])-'A'][int(a)-'A'];
				if(x > 0)
				{	
					res[rlenth-1] = com[x];
					continue;
				} else {
					bool f = false;
					for(int q=0;q<rlenth;q++)
						if(sta2[int(res[q])-'A'][int(a)-'A'] == -1)
						{
							f = true;
							break;
						}
					if(f == true)
					{
						rlenth = 0;
						continue;
					}
				}
			}
			res[rlenth] = a;
			rlenth++;
		}
		cout << "Case #" << i+1 << ": [";
		for(int j=0;j<rlenth;j++)
		{
			if(j == rlenth-1)
				cout << res[j];
			else cout << res[j] << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
