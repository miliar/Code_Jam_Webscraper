#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool check(int i, int j, char ta, vector<string>& table,int K,int n)
{
	if(table[i][j] != ta) return false;
	int ti = i;
	int tj = j;
	int cnt = 1;
	while(tj < n){
		tj++;
		ti++;
		if(ti >= n) break;
		if(table[ti][tj] == ta) cnt++;
		else break;
		if(cnt >= K)
			return true;
	}
	ti = i;
	tj = j;
	cnt = 1;
	while(tj < n){
		tj++;
		ti--;
		if(ti < 0) break;
		if(table[ti][tj] == ta) cnt++;
		else break;
		if(cnt >= K)
			return true;
	}
	return false;
}


int main(){
	ifstream in("input");
	ofstream out("output");
	int cases;
	in >> cases;
	int K,n;


	for(int i = 1; i <= cases; i++){
		cout << "case" << i << endl;
		out << "Case #" << i << ": ";
		in >> n >> K;
		//cout << K << " " << n << endl;
		string line;
		bool red = false;
		bool blue = false;
		vector<string> table;
		for(int k = 0; k < n; k++){
			in >> line;
			int point = line.length();
			for(int j = line.length(); j >= 0; j--)
			{
				if(line[j] == '.'){
					for(int jj = j - 1; jj >= 0; jj--){
						if(line[jj] != '.'){
							line[j] = line[jj];
							line[jj] = '.';
							break;
						}
					}
				}
			}
			//cout << line << endl;

			table.push_back(line);
		}
		int cnt = 0;
		for(int k = 0; k < n; k++)
		{
			if(!red){
				cnt = 0;
				for(int j = n-1; j >=0; j--)
				{
					if(table[k][j] == '.') continue;
					else if(table[k][j] == 'R') cnt++;
					else cnt = 0;
					if(cnt >= K){
						red = true;
						break;
					}
				}
			}
			if(!blue){
				cnt = 0;
				for(int j = n-1; j >=0; j--)
				{
					if(table[k][j] == '.') continue;
					else if(table[k][j] == 'B') cnt++;
					else cnt = 0;
					if(cnt >= K){
						blue = true;
						break;
					}
				}
			}
			if(!red){
				cnt = 0;
				for(int j = n-1; j >=0; j--)
				{
					if(table[j][k] == '.') continue;
					else if(table[j][k] == 'R') cnt++;
					else cnt = 0;
					if(cnt >= K){
						red = true;
						break;
					}
				}
			}
			if(!blue){
				cnt = 0;
				for(int j = n-1; j >=0; j--)
				{
					if(table[j][k] == '.') continue;
					else if(table[j][k] == 'B') cnt++;
					else cnt = 0;
					if(cnt >= K){
						blue = true;
						break;
					}
				}
			}
		}
		for(int ii = 0; ii < n; ii++)
			for(int jj = 0; jj < n; jj++)
			{
				if(!red)
					red = check(ii,jj,'R',table,K,n);
				if(!blue)
					blue = check(ii,jj,'B',table,K,n);
			}

		if(blue&&red) out << "Both" << endl;
		else if(blue) out << "Blue" << endl;
		else if(red) out << "Red" << endl;
		else out << "Neither" << endl;


	}	
	return 0;
}
