# include <iostream>
# include <vector>
# include <algorithm>
# include <cmath>
# include <cstdio>
# include <map>
# include <cassert>
# include <fstream>
# include <queue>
# include <stack>

using namespace std;

void useGravity(vector<string> &vs)
{
	for(int i = vs[0].size()-1;i>=0;i--)
	{
		for(int j = 0;j<vs.size();j++)
		{
			int t = i;
			while(t+1 < vs[0].size() && vs[j][t+1]=='.')
			{
				vs[j][t+1]=vs[j][t];
				vs[j][t]='.';
				t++;				
			}
		}	
	}

}

char getWinner(vector<string> &vs,int K,char c)
{
	for(int i = 0;i<vs.size();i++)
	{
		for(int j = 0;j<vs[i].size();j++)
		{
			int flag = 0;
			//horizontal
			int k;
			for(k = 1;k<K;k++)
			{
				if(j+k-1 < vs[i].size() && j+k<vs.size()){
					if( vs[i][j+k-1] != vs[i][j+k]){
						flag = 1;	
					}
				}		
				else {
					break;
				}
			}	
			
			if(!flag  && k==(K) && vs[i][j]==c){
				return vs[i][j];
			}

			flag = 0;

			//vertical
			for(k = 1;k<K;k++)
			{
				if(i+k-1 < vs.size() && i+k<vs.size()){
					 if(vs[i+k-1][j] != vs[i+k][j]){
						flag = 1;	
					}
				}		
				else{
					break;
				}
			}	
			
			if(!flag && k==(K) && vs[i][j]==c){
				return vs[i][j];
			}

			flag = 0;
			//right
			for(k = 1;k<K;k++)
			{
				if(i+k-1 < vs.size() && i+k<vs.size() && j+k-1<vs[i].size() && j+k<vs[i].size()){
					if(vs[i+k-1][j+k-1] != vs[i+k][j+k]){
						flag = 1;	
					}
				}		
				else{
					break;
				}
			}	
			
			if(!flag && k==(K) && vs[i][j]==c){
				return vs[i][j];
			}
		
			flag = 0;	
			//left
			for(k = 1;k<K;k++)
			{
				if(i+k-1 < vs.size() && i+k<vs.size() && j-k+1>=0 && j-k>=0){
					if(vs[i+k-1][j-k+1] != vs[i+k][j-k]){
						flag = 1;	
					}
				}		
				else{
					break;
				}
			}	
			
			if(!flag && k==(K) && vs[i][j]==c){
				return vs[i][j];
			}

		}
	}	
	
	return ' ';	
}

int main(int argc,char * argv[])
{

	ifstream in(argv[1]);
	ofstream out(argv[2]);
	
	int t,cas = 0;
	in>>t;

	while(t--)
	{	
		int N,K;
		in>>N>>K;
		
		vector<string> vs;
		string inp;
		
		for(int i = 0;i<N;i++)
		{
			in>>inp;
			vs.push_back(inp);
		}	

		useGravity(vs);
	
		char winner1 = getWinner(vs,K,'R');	
		char winner2 = getWinner(vs,K,'B');	
	
		out<<"Case #"<<++cas<<": ";

		if(winner1 != ' ' && winner2 != ' ')
			out<<"Both";
		else if(winner1==' ' && winner2==' ')
			out<<"Neither";
		else if(winner1=='R')
			out<<"Red";
		else if(winner2=='B')
			out<<"Blue";
		
		out<<endl;
	}
	
	return 0;
}

