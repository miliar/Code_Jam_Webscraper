#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <stdio.h>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back
#define mp make_pair

using namespace std;

int c,r,d;
int grid[505][505];

bool valid(int i, int j)	{
	return i >= 0 && i < r && j >= 0 && j < c;
}

bool cando(int k, int i, int j)	{
	int l = j - (k / 2);
	int r = j + (k / 2);
	
	if (k % 2 == 0)	{
		l += 1;
	}
	
	int t = i - (k / 2);
	int b = i + (k / 2);
	
	if (k % 2 == 0)	{
		t += 1;
	}
	
	double cx = i + (k % 2 == 0 ? 0.5 : 0);
	double cy = j + (k % 2 == 0 ? 0.5 : 0);
	double cmassx = 0;
	double cmassy = 0;
	
// 	if (k >= 0)	{
// 		printf("i %d j %d l %d r %d t %d b %d cx %lf cy %lf k %d\n", i,j,l,r,t,b,cx,cy, k );
// 	}
// 	
	forp(t,b+1,a)	{
		forp(l,r+1,z)	{
			
			if (!valid(a,z))	{
// 				cout << "not valid " << k << " i " << i << " j " << j << endl;
				return false;
			}
			
			if (z == l && a == t)
				continue;
			if (z == r && a == t)
				continue;
			if (z == l && a == b)
				continue;
			if (z == r && a == b)
				continue;
			
// 			printf("%lf %lf %lf\n", ((double)a - cx), ((double)z - cy), (double)(d + grid[a][z]));
			cmassx += ((double)a - cx) * (double)(d + grid[a][z]);
			cmassy += ((double)z - cy) * (double)(d + grid[a][z]);
		}
	}
	
//   	printf("Cmass %lf res %s\n", cmass, cmass == 0 ? "true" : "false");
	return cmassx == 0 && cmassy == 0;
}

bool cando2(int k, int i, int j)	{
	int l = j - (k / 2);
	int r = j + (k / 2);
	
	if (k % 2 == 0)	{
		l += 1;
	}
	
	int t = i - (k / 2);
	int b = i + (k / 2);
	
	if (k % 2 == 0)	{
		t += 1;
	}
	
	double cx = (double)i + (k % 2 == 0 ? 0.5 : 0);
	double cy = (double)j + (k % 2 == 0 ? 0.5 : 0);
	double centerx = cx;
	double centery = cy;
	
	cx = 0;
	cy = 0;
	double mx = 0;
	
// 		if (k >= 0)	{
// 		printf("i %d j %d l %d r %d t %d b %d cx %lf cy %lf k %d\n", i,j,l,r,t,b,cx,cy, k );
// 	}
	
	forp(t,b+1,a)	{
		forp(l,r+1,z)	{
			
			if (!valid(a,z))	{
// 				cout << "not valid " << k << " i " << i << " j " << j << endl;
				return false;
			}
			
			if (z == l && a == t)
				continue;
			if (z == r && a == t)
				continue;
			if (z == l && a == b)
				continue;
			if (z == r && a == b)
				continue;
			
			mx += grid[a][z];
			cx += grid[a][z] * z;
			cy += grid[a][z] * a;
		}
	}
	
	cx /= mx;
	cy /= mx;
	
// 	printf("center x %lf center y %lf cx %lf cy %lf\n", centerx, centery, cx, cy);
	return centerx == cx && centery == cy;
}

bool cando3(int k, int i, int j)	{
	
	double cx = (double)i + (k % 2 == 0 ? 0.5 : 0);
	double cy = (double)j + (k % 2 == 0 ? 0.5 : 0);
	double centerx = (double)i + (double)k / 2;
	double centery = (double)j + (double)k / 2;
	
	cx = 0;
	cy = 0;
	double mx = 0;
	
		if (k >= 0)	{
		printf("i %d j %d k %d\n", i , j ,k);
	}
	
	forp(i,i+k,a)	{
		forp(j,j+k,z)	{
			
			if (!valid(a,z))	{
				return false;
			}
			
			if (z == i && a == j)
				continue;
			if (z == i+k-1 && a == j+k-1)
				continue;
			if (z == i && a == j)
				continue;
			if (z == i+k-1 && a == j+k-1)
				continue;
			
			mx += grid[a][z];
			cx += grid[a][z] * z;
			cy += grid[a][z] * a;
		}
	}
	
	cx /= mx;
	cy /= mx;
	
 	printf("center x %lf center y %lf cx %lf cy %lf\n", centerx, centery, cx, cy);
	return centerx == cx && centery == cy;
}

bool istopconer(int i, int j, int l, int r, int t, int b)	{
	if (i == t)
		if (j == r || j == l)
		return true;
	if (i == b)
		if (j == r || j == l)
			return true;
	return false;
}

bool can(int k, int i, int j)	{

	int left = j + k/2 ;
	int right = j + k;
	int t = i + k/2;
	int b = i + k;
	
	int masl = 0;
	int masr = 0;
	forp(j,left,c)	{
		forp(i,b,r)	{
			if (!valid(r,c))	{
				return false;
			}
			if (istopconer(r,c,j,right-1,i,b-1)) continue;
 			cout << "row col " << r << " " << c << " " << b << endl;
// 			cout << grid[r][c] << " " ;
			masl += grid[r][c];
		}
	}
// 	cout << endl;
	forp(left+(k % 2 == 0 ? 0 : 1),right,c)	{
		forp(i,b,r)	{
			if (!valid(r,c))	{
				return false;
			}
			if (istopconer(r,c,j,right-1,i,b-1)) continue;
			cout << "row col " << r << " " << c << " " << b << endl;
// 			cout << grid[r][c] << " " ;
			masr += grid[r][c];
		}
	}
// 	cout << endl;
	int mast = 0;
	int masb = 0;
	forp(i,t,r)	{
		forp(j,right,c)	{
			if (!valid(r,c))	{
				return false;
			}
			if (istopconer(r,c,j,right-1,i,b-1)) continue;
			cout << "row col " << r << " " << c << endl;
// 			cout << grid[r][c] << " " ;
			mast += grid[r][c];
		}
	}
// 	cout << endl;
	forp(t+(k % 2 == 0 ? 0 : 1),b,r)	{
		forp(j,right,c)	{
			if (!valid(r,c))	{
				return false;
			}
			
			if (istopconer(r,c,j,right-1,i,b-1)) continue;
			cout << "row col " << r << " " << c << endl;
// 			cout << grid[r][c] << " " ;
			masb += grid[r][c];
		}
	}
// 	cout << endl;
	
   	printf("masl %d masr %d mast %d masb %d %d %d %d\n", masl, masr, mast, masb, i ,j, k);
	
	return masl == masr && mast == masb;
}

void solve(int kase)	{

// 	cout << r << " " << c << " " << d << endl;
	
	int k = 3;
	int minwidth = min(r,c) - 3;
	int maxk = -1;
	forp(0,minwidth+1,i)	{
		forp(0,r,j)	{
			forp(0,c,l)	{
				
				if (cando(k+i, j, l))	{
					maxk = max(maxk, k+i);
// 					cout << "here " << endl;
				}
			}
		}
	}
	
//   	can(4,0,0);
	
	if (maxk != -1)	{
		printf("Case #%d: %d\n", kase, maxk);
	} else	{
		printf("Case #%d: IMPOSSIBLE\n", kase);
	}
}

int main()	{

	int kases;
	cin >> kases;
	forp(0,kases,z)	{
	
		cin >> r >> c >> d;
// 		cout << r << " " << c << " " << d << endl;
		forp(0,r,i)	{
			forp(0,c,j)	{
				char c;
				cin >> c;
				grid[i][j] = c - '0';
			}
		}
		
		solve(z+1);
	}
}