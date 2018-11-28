#include <bits/stdc++.h>

using namespace std;

bool valid(string &s, char ch)
{
	int cnt1 = 0, cnt2 = 0;
	for(int i=0; i<4; i++)
		if(s[i] == ch) cnt1++;
		else if(s[i] == 'T') cnt2++;
	return (cnt1 == 4 || (cnt1 == 3 && cnt2 == 1));
}

bool check(vector <string> &M, char ch)
{
	for(int i=0; i<4; i++)
		if(valid(M[i], ch))
			return 1;
	
	string s;
	
	for(int j=0; j<4; j++)
	{
		s = "";
		s += M[0][j];
		s += M[1][j];
		s += M[2][j];
		s += M[3][j];
		
		if(valid(s, ch))
			return 1;
	}
	
	string s1 = "", s2 = "";
	for(int i=0; i<4; i++)
	{
		s1 += M[i][i];
		s2 += M[i][3-i];
	}
	 
	if(valid(s1, ch)) return 1;
	if(valid(s2, ch)) return 1;
	
	return false;
}

int main()
{
	int T;
	cin>>T;
	
	for(int caso=1; caso<=T; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		vector <string> M(4);
		for(int i=0; i<4; i++)
			cin>>M[i];
		
		if(check(M, 'X')) cout<<"X won"<<endl;
		else if(check(M, 'O')) cout<<"O won"<<endl;
		else
		{
			int cnt = 0;
			for(int i=0; i<4; i++)
				for(int j=0; j<4; j++)
					cnt += (M[i][j] == '.');
			
			if(cnt == 0) cout<<"Draw"<<endl;
			else cout<<"Game has not completed"<<endl;
		}
	}
  
	return 0;
}
