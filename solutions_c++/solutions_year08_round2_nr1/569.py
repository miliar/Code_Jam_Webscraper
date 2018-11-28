#include <iostream>
#include <vector>
#include <utility>

using namespace std;


void main()
{
    int N = 0;
    cin >> N;
    
    int i;
    for(i = 0; i < N; i++)
    {
		long n;
		cin >> n;
		long A;
		cin >> A;
		long B;
		cin >> B;
		long C;
		cin >> C;
		long D;
		cin >> D;
		long x0;
		cin >> x0;
		long y0;
		cin >> y0;
		long M;
		cin >> M;
        
		vector<pair<__int64, __int64> > trees(n);

		trees[0] = make_pair(x0, y0);

		__int64 x = x0;
		__int64 y = y0;

        int j;
        for(j = 1; j < n ; j++)
        {
			x = (A * x + B) % M;
			y = (C * y + D) % M;

			trees[j] = make_pair(x, y);
        }
        
		long count = 0;

		for(j = 0; j < trees.size(); j++)
		{
			int k;
			for(k = j + 1; k < trees.size(); k++)
			{
				int l;
				for(l = k + 1; l < trees.size(); l++)
				{
					if (((trees[j].first + trees[k].first + trees[l].first) % 3) == 0 &&
						((trees[j].second + trees[k].second + trees[l].second) % 3) == 0)
						count++;
				}
			}
		}
            
        cout << "Case #" << (i + 1) << ": " << count << endl;
    }
}

