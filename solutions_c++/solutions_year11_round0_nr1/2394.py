#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

int abs(int k)
{
	if(k > 0)
		return k;
	return k*(-1);
}

int sign(int k)
{
	if(k > 0)
		return 1;
	return -1;
}

int main()
{
	int tests;
	cin >> tests;
	for(int i = 0; i < tests; i++)
	{
		int N;
		cin >> N;
		vector <int> R_o;
		vector <int> R_b;
		vector <int> order;
		for(int j = 0; j < N; j++)
		{
			char R;
			int P;
			cin >> R >> P;
			if(R == 'O') {
				R_o.push_back(P);
				order.push_back(0);
			}
			else{
				R_b.push_back(P);
				order.push_back(1);
			}
		}
		for(int k = 0; k < R_o.size(); k++)
			cerr << R_o[k] << " " ;
		cerr << endl;
		for(int k = 0; k < R_b.size(); k++)
			cerr << R_b[k] << " " ;
		cerr << endl;
		for(int k = 0; k < order.size(); k++)
			cerr << order[k] << " " ;
		cerr << endl;
		
		int c_o = 0;
		int c_b = 0;
		int pos_o = 1;
		int pos_b = 1;
		int ans = 0;
		for(int j = 0; j < N; j++)
		{
			int move;
			if(order[j]==0){
				move = abs(pos_o-R_o[c_o]);
				ans += move + 1;
				pos_o = R_o[c_o];
				if(c_b < R_b.size())
					pos_b += sign(R_b[c_b]-pos_b)*min(abs(R_b[c_b]-pos_b),move+1);
				c_o++;
			}
			else{
				move = abs(pos_b-R_b[c_b]);
				ans += move + 1;
				pos_b = R_b[c_b];
				if(c_o < R_o.size())
					pos_o += sign(R_o[c_o]-pos_o)*min(abs(R_o[c_o]-pos_o),move+1);
				c_b++;
				
			}
			cerr<< "Move: " << move << ", Ans: " << ans << ", B: " << pos_b << ", O: " << pos_o << endl;
		}
		
		cout << "Case #" << i+1 << ": " << ans  << endl; 
	}
}