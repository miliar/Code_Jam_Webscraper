#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
bool is(vector<vector<char> > a){
	int cnt ;
	for(int i=0;i < a.size();i++){
		cnt = 0;
		for(int j=0;j<a[i].size();j++)
			if(a[i][j] == '#') cnt++;

		if(cnt % 2 == 1) return false;
	}

	for(int i=0;i < a[0].size();i++){
		cnt = 0;
		for(int j=0;j<a.size();j++)
			if(a[j][i] == '#') cnt++;

		if(cnt % 2 == 1) return false;
	}

	return true;
}
int main()
{
	freopen("output.txt","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for(int testero = 1; testero <= testcase;testero++)
	{
		printf("Case #%d:\n",testero);
		int n,m;
		
		scanf("%d%d", &n, &m);

		vector<vector<char> > maj(n,vector<char> (m));
		for(int i=0;i<n;i++){
			getchar();
			for(int j =0;j<m;j++){
				maj[i][j] = getchar();
			}
		}
		if(!is(maj)){
			puts("Impossible");
			continue;
		}

		for(int i=0;i<maj[0].size() -1 ;i++){
			if(maj[0][i] == '#' && maj[0][i+1] == '#'){
				 maj[0][i]= '/'; maj[0][i+1] = '\\';
				 maj[1][i]= '\\'; maj[1][i+1] = '/';
				 i++;
			}
		}


		for(int i=1;i<maj.size()-1;i++)
		{
			for(int j=0;j<maj[i].size()-1;j++){
				if(maj[i][j] == '#'){
						maj[i][j]= '/'; maj[i][j+1] = '\\'; 
						maj[i+1][j]= '\\'; maj[i+1][j+1] = '/'; 
					
					j++;
				}
			}
		
		}
		for(int i=0;i<maj.size();i++){
			for(int j=0;j<maj[i].size();j++)
				putchar(maj[i][j]);
			putchar('\n');
		
		}

	}

	
	return 0;
} 