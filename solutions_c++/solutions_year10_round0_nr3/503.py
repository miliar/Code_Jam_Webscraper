#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long Int;

int get(const vector<int>& vi, int idx)
{
    return vi[idx%vi.size()];
}

int main(void)
{
    int T;
    
    cin >> T;
    for(int c=1;c<=T;c++){
	int R, k, N;
	
	cin >> R >> k >> N;
	
	vector<int> g(N);
	vector<int> av(N);
	vector<int> pe(N);
	for(int i=0;i<N;i++){
	    cin >> g[i];
	}
	
	for(int i=0;i<N;i++){
	    pe[i] = 0;
	    int j = i;
	    while( pe[i] + get(g, j) <= k && j - i < N ){
		pe[i] += get(g, j);
		j++;
	    }
	    av[i] = j - i;
	    //cout << "pe: " << i << " " << pe[i] << endl;
	    //cout << "av: " << i << " " << av[i] << endl;
	    
	}

	Int ans = 0;
	int p = 0;
	for(int i=0;i<R;i++){
	    ans += pe[p];
	    p = (p + av[p]) % N;
	}
	cout << "Case #" << c << ": " << ans << endl;
    }
}
