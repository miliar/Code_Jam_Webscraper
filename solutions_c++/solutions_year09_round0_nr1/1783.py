#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cmath>
 
using namespace std;
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)

#define MAX  5001
#define MAXL 16

string dic[MAX];
int main() {
	int l,d,n;
	cin >> l >> d >> n; 
	for (int k=0;k<d;k++)
		cin >> dic[k];
	//sort(dic,dic+d);
	
	
	for (int k=1;k<=n;k++) {
		string pal;
		cin >> pal;
		
		int mat[MAX][MAXL] = {}, pos = 0;
		for (int l=0;l<int(pal.sz());l++,pos++) {
			int v[300]={}; 
			if (pal[l] == '(') {
				for (l++;l<int(pal.sz());l++) {
					v[int(pal[l])] = 1;
					if (pal[l] == ')') {
						break;
					}
				}
			}
			else
				v[int(pal[l])] = 1;
				
			
			for (int r=0;r<d;r++) {
				if (v[ int(dic[r][pos]) ] == 1) {
					if (pos == 0)
						mat[r][pos] = 1;
					else
						if (mat[r][pos-1])
							mat[r][pos] = 1;	
				}		
			}
		}
		
		int count = 0;
		pos--;
		for (int l=0;l<d;l++) {
			count += mat[l][pos]; 
		}
		cout << "Case #" << k << ": " << count << endl;
	}
	return 0;
}

