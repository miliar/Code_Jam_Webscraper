#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int ttt;	
int l, n, c;
long long t;

long long ttm[1000001];
int a[1000001];


int main()
{
	
    cin >> ttt;
    for(int tt=1; tt<=ttt; tt++)
    {
		cin >> l >> t >> n >> c;
		//cout << l << " " << t << " " << n << " " << c << endl;
		
		for(int i=0; i<c; i++) 
		{
			cin >> a[i];
		}
		
		for(int i=0; i<n; i++) 
		{
			ttm[i] = 2*a[i%c];
		}
		
		long long res = 0;
		
		int pos = 0;
		while (res+ttm[pos] <= t && pos < n)
		{
			res+=ttm[pos];
			pos++;
		}
	
		if (pos < n)
		{
			vector<long long> save;
			
			long long tmp = t - res;
			save.push_back(ttm[pos] - tmp);
			
			res = t;
			
			for(int i=pos+1; i<n; i++) 
			{
				save.push_back(ttm[i]);
			}
			
			sort(save.rbegin(), save.rend());		
			
			//for(int i=0; i<save.size(); i++) cout << save[i] << " "; cout << endl;
			//cout << res << endl;
			//cout << pos << " " << save.size() << endl;
			
			for(int i=0; i<save.size(); i++) 
			{
				if (i < l) res += save[i] / 2;
				else res += save[i];
				//res += save[i];
			}
		}
	
		cout << "Case #" << tt << ": " << res << endl;	
		
    }
    
    return 0;
}
