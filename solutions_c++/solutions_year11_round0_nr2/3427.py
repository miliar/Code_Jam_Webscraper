#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	
	int N,C,D,cur=0;
	char t1,t2,t3;
	cin >> N;
	bool org[26];
	char l[100];
		char comb[26][26];
		bool opp[26][26];
	for(int testcase = 0; testcase<N;testcase++)
	{
		cur =0;
		for(int i =0;i<26;i++) org[i] = 0;
		for(int i=0;i<26;i++) for(int j =0;j<26;j++) comb[i][j]=0;
		for(int i=0;i<26;i++) for(int j =0;j<26;j++) opp[i][j]=0;
		cin >> D;
		for(int com = 0;com<D;com++)
		{
			cin >> t1 >> t2 >> t3;
			org[t1 - 'A'] = 1;
			org[t2 - 'A'] = 1;
			comb[t1 - 'A'][t2 - 'A'] = t3 - 'A' + 1;	
			comb[t2 - 'A'][t1 - 'A'] = t3 - 'A' + 1;			
		}
		cin >> C;
		for(int i = 0;i<C;i++)
		{
			cin >> t1 >> t2;
			opp[t1 - 'A'][t2 - 'A'] = 1;		
			opp[t2 - 'A'][t1 - 'A'] = 1;			
		}
		cin >> C;
		for(int i = 0;i<C;i++)
		{
			cin >> t1;
			if (cur==0)
			{
				l[0] = t1;
				cur++;
			}
			else
			{
				char cres = comb[l[cur-1] - 'A'][t1 - 'A'];
				if (cres != 0)
				{
					l[cur-1] = 'A' + cres - 1;
				}
				else
				{
					char cl = 0;
					for(int ind=0;ind<cur;ind++)
						if (opp[t1 - 'A'][l[ind] - 'A']) 
						{
							cl = 1;
							break;
						}
						if (cl)
						cur = 0;
						else
						{
					cur++;
					l[cur-1] = t1;
				}
					
				}
				
			}	
		}
		cout << "Case #" << testcase+1 << ": [";
		for(int ind=0;ind<cur;ind++)
		if (ind==0) cout << l[ind];
		else cout << ", " << l[ind];
		
		cout << "]" <<endl;
		
	}
	
	
	fcloseall();
return 0;
}
