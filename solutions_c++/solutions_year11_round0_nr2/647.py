#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

bool find(vector<char> &list, char c)
{
	for(int i=0;i<list.size();i++) if(list[i] == c) return true;
	return false;
}

int main()
{
  int T;
	cin >> T;
	int case_num = 1;
	while(T>0)
	{
	  int C, D, N;
		cin >> C;
		vector<char> b1(C), b2(C), b3(C);
		for(int i=0;i<C;i++) cin >> b1[i] >> b2[i] >> b3[i];
		cin >> D;
		vector<char> op1(D), op2(D);
		for(int i=0;i<D;i++) cin >> op1[i] >> op2[i];
		vector<char> list;
		cin >> N;
		string s; cin >> s;
		
		for(int i=0;i<N;i++)
		{
			if(list.size() == 0) list.push_back(s[i]);
			else
			{
				int jj = 0; bool done = false; int kk = 0;
				while(!done && jj < C)
				{
				  if( (list.back() == b1[jj] && s[i] == b2[jj]) || (list.back() == b2[jj] && s[i] == b1[jj]) )
					{
					  list.pop_back(); list.push_back(b3[jj]);
						done = true;
					}
				  jj++;
				}
				while(!done && kk < D)
				{
				  if(s[i] == op1[kk] && find(list, op2[kk]))
					{
					  list.clear(); done = true; 
					}
					else
					{
					  if(s[i] == op2[kk] && find(list, op1[kk]))
						{
						  list.clear(); done = true;
						}
					}
					kk++;
				}
				if(!done) list.push_back(s[i]);
			}
			//for(int j=0;j<list.size();j++) cout << list[j] << "|"; cout << endl; //debug
		}
	  cout << "Case #" << case_num << ": [";
		if(list.size() > 1) for(int i=0;i < (list.size()-1); i++) cout << list[i] << ", ";
		if(list.size() != 0) cout << list[list.size()-1];
		cout << "]" << endl;
	 
	  T--; case_num++;
	}

  return 0;
}
