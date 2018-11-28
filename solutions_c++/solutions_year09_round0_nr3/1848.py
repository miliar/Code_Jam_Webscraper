#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <stdio.h>
 
using namespace std;
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second


int main() {
	int t;
	string pal;
	cin >> t;
	getline(cin,pal);
	
	for (int k=1;k<=t;k++) {
	
		int mat[505][10] = {};
				
		getline(cin,pal);
		for (int x=0;x<int(pal.sz());x++)
			if (pal[x] == 'w')
				mat[x][0] = 1;
		for (int x=0;x<int(pal.sz());x++) {
			for (int y=0;y<x;y++) {
				if (pal[y] == 'w' && pal[x] == 'e')
					mat[x][0] = (mat[x][0] + mat[y][0]) % 10000;
				
					
				if (pal[y] == 'e' && pal[x] == 'l')
					mat[x][0] = (mat[x][0] + mat[y][0]) % 10000;
					
				if (pal[y] == 'l' && pal[x] == 'c')
					mat[x][0] = (mat[x][0] + mat[y][0]) % 10000;
					
				if (pal[y] == 'c' && pal[x] == 'o')
					mat[x][0] = (mat[x][0] + mat[y][0]) % 10000;
					
				if (pal[y] == 'o' && pal[x] == 'm')
					mat[x][0] = (mat[x][0] + mat[y][0]) % 10000;
					
				if (pal[y] == 'm' && pal[x] == 'e')
					mat[x][1] = (mat[x][1] + mat[y][0]) % 10000;
					
				if (pal[y] == 'e' && pal[x] == ' ')
					mat[x][0] = (mat[x][0] + mat[y][1]) % 10000;
					
					
					
				if (pal[y] == ' ' && pal[x] == 't')
					mat[x][0] = (mat[x][0] + mat[y][0]) % 10000;
					
				if (pal[y] == 't' && pal[x] == 'o')
					mat[x][1] = (mat[x][1] + mat[y][0]) % 10000;
					
				if (pal[y] == 'o' && pal[x] == ' ')
					mat[x][1] = (mat[x][1] + mat[y][1]) % 10000;
					
				if (pal[y] == ' ' && pal[x] == 'c')
					mat[x][1] = (mat[x][1] + mat[y][1]) % 10000;
					
					
				if (pal[y] == 'c' && pal[x] == 'o')
					mat[x][2] = (mat[x][2] + mat[y][1]) % 10000;
					
				if (pal[y] == 'o' && pal[x] == 'd')
					mat[x][0] = (mat[x][0] + mat[y][2]) % 10000;
					
				if (pal[y] == 'd' && pal[x] == 'e')
					mat[x][2] = (mat[x][2] + mat[y][0]) % 10000;
					
				if (pal[y] == 'e' && pal[x] == ' ')
					mat[x][2] = (mat[x][2] + mat[y][2]) % 10000;
					
										
					
				if (pal[y] == ' ' && pal[x] == 'j')
					mat[x][0] = (mat[x][0] + mat[y][2]) % 10000;
					
				if (pal[y] == 'j' && pal[x] == 'a')
					mat[x][0] = (mat[x][0] + mat[y][0]) % 10000;
					
				if (pal[y] == 'a' && pal[x] == 'm')
					mat[x][1] = (mat[x][1] + mat[y][0]) % 10000;
					
			
			
			}
		}
		
		int num = 0;
		for (int x=0;x<int(pal.sz());x++) {
			//cout << pal[x] << "   - " << mat[x][0] << " " << mat[x][1] << " " << mat[x][2] << endl;
			if (pal[x] == 'm')
				num = ((num%10000) + (mat[x][1]%10000)) % 10000;
		}
		
		cout << "Case #" << k << ": ";
		printf("%.4d\n",num);

	}
	return 0;
}

