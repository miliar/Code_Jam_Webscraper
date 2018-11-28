		#include <string>
		#include <iostream>
		#include <cstdio>
		#include <cstdlib>
		using namespace std;

		int l[10000], r[10000], ul[10000], dl[10000], ur[10000], dr[10000], 
			n, rep[2000], i, j, k;
		string s[2000];
		int dx[4] = {0, 1, 0, -1};
		int dy[4] = {1, 0, -1, 0};
		int cx, cy, areaarea, d, nx, ny, tot, ts, o;

		main() {
			   freopen("a.in", "r", stdin);
			   freopen("a.out", "w", stdout);
			   
			   for (cin >> ts; ++o <= ts; ) 
				{
				   cin >> n;
				   for (i=0; i<n; i++)
					   cin >> s[i] >> rep[i];
				   cx = cy = 5000; 
				   areaarea = d = tot = 0;
				   for (i=9001; i; i--) r[i] = 0, l[i] = 10000;
				   for (i=0; i<n; i++)
					   for (j=0; j<rep[i]; j++)
						   for (k=0; k<s[i].length(); k++) {
							   if (s[i][k] == 'L') { d = d+3&3; continue; }
							   if (s[i][k] == 'R') { d = d+1&3; continue; }
							   if (!dx[d]) {
								  if (d == 2) ny = cy-1; else ny = cy;
								  l[ny] <?= cx; r[ny] >?= cx;
							   }
							   nx = cx + dx[d]; ny = cy + dy[d];
							   areaarea += nx*cy - ny*cx;
							   cx = nx; cy = ny;
						   }
				   dl[0] = ul[9001] = 10000;
				   for (i=1; i<9000; i++) 
					   {
					   dl[i] = dl[i-1] <? l[i];
					   dr[i] = dr[i-1] >? r[i];
				   }
				   for (i=9000; i; i--) 
					   {
					   ul[i] = ul[i+1] <? l[i];
					   ur[i] = ur[i+1] >? r[i];
					   l[i] <?= dl[i] >? ul[i];
					   r[i] >?= dr[i] <? ur[i];
				   }
				   for (i=9000; i; i--) 
					   {
					   tot += r[i]-l[i] >? 0;
				   }
				   cout << "Case #" << o << ": ";
				   cout << tot - abs(areaarea)/2 << endl;
			   }
			   return 0;
		}
