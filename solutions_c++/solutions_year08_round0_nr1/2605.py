#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int N, S, Q;
	cin >> N;
	for(int i=1; i<= N; i++)
	{
		cin >> S;
string dummy;
		vector<string> vs(S);
		getline(cin, vs[0]);
		for(int j=0; j<S; j++)
			getline(cin, vs[j]);
		cin >> Q;
		vector<string> vq(Q);
		getline(cin, dummy);
		for(int j=0; j<Q; j++)
			getline(cin, vq[j]);
		
		int ret = -1;
		string c = "-";
		int pos = 0;
		
		while(1)
		{
			ret++;
			int b1 = -1;
			for(int j=0; j<S; j++)
			{
				if(vs[j] == c)
					continue;
				
				int t = Q;
				for(int k=pos; k<Q; k++)
					if(vq[k] == vs[j])
					{
						t = k;
						break;
					}
				if(t>b1)
					b1=t;
			}
			pos = b1;
			if(pos < Q)
				c = vq[pos];
			else
				break;
		}
		cout << "Case #" << i << ": " << ret << endl;
	}
	return 0;
}
