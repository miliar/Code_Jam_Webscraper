#include <iostream>
#include <stack>
#include <utility>
#include <cstring>

using namespace std;

int T;

#define mx 60006

int pos[mx];
int len[mx];
int minh[mx];

int main()
{
	cin >> T;
	for(int ti = 1; ti <= T; ti++)
	{
		memset(minh, 0, sizeof(minh));
		bool ans = false;
		int n;
		cin >> n;
		for(int i=0; i<n; i++)
			cin >> pos[i] >> len[i];
		int D;
		cin >> D;
		minh[0] = pos[0];
		int l = 0;
		if(D-pos[0] <= minh[0]){	
			ans = true;
		}else{
			for(int i=1; i<n; i++)
			{
				while(pos[l]+minh[l] < pos[i])
					l++;
				if(l>= i){
					ans = false;
					break;
				}
				minh[i] = min(len[i], pos[i]-pos[l]);
				if(pos[i]+minh[i]>=D){
					ans = true;
					break;
				}	 
			}
		}
		
		if(ans)
			cout << "Case #"<<ti<<": " <<"YES"<<endl;
		else
			cout << "Case #"<<ti<<": " << "NO" <<endl;
	}	
	return 0;
}
