#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int main() {
	long long count[3][3];
	int i, j;
	int teste, n, t;
	long long x0, y0, a, b, c, d, x, y, m;
	long long resp;
	int aux;
	
	scanf("%d\n", &teste);
	for (t=0; t<teste; t++){
		scanf("%d", &aux);
		n = aux;
		scanf("%d", &aux);
		a = aux;
		scanf("%d", &aux);
		b = aux;
		scanf("%d", &aux);
		c = aux;
		scanf("%d", &aux);
		d = aux;
		scanf("%d", &aux);
		x0 = aux;
		scanf("%d", &aux);
		y0 = aux;
		scanf("%d", &aux);
		m = aux;
		
		for (i=0; i<3; i++)
		{
			for (j=0; j<3; j++)
			{
				count[i][j] = 0;
			}
		}
        x = x0;
		y = y0;
			//printf("%I64d %I64d\n", x, y);
	   	   count[x%3][y%3]++;
		for (i = 1; i < n; i++)	{
		  	x = (a * x + b)%m;
		  	y = (c * y + d)%m;
			//printf("%I64d %I64d\n", x, y);
			count[x%3][y%3]++;
		}
		resp = 0;
		resp += count[0][0]*count[0][1]*count[0][2];
		resp += count[1][0]*count[1][1]*count[1][2];
		resp += count[2][0]*count[2][1]*count[2][2];
		resp += count[0][0]*count[1][0]*count[2][0];
		resp += count[0][1]*count[1][1]*count[2][1];
		resp += count[0][2]*count[1][2]*count[2][2];
		resp += (count[0][0]*(count[0][0]-1)*(count[0][0]-2))/6;
		resp += (count[0][1]*(count[0][1]-1)*(count[0][1]-2))/6;
		resp += (count[0][2]*(count[0][2]-1)*(count[0][2]-2))/6;
		resp += (count[1][0]*(count[1][0]-1)*(count[1][0]-2))/6;
		resp += (count[1][1]*(count[1][1]-1)*(count[1][1]-2))/6;
		resp += (count[1][2]*(count[1][2]-1)*(count[1][2]-2))/6;
		resp += (count[2][0]*(count[2][0]-1)*(count[2][0]-2))/6;
		resp += (count[2][1]*(count[2][1]-1)*(count[2][1]-2))/6;
		resp += (count[2][2]*(count[2][2]-1)*(count[2][2]-2))/6;
 	    resp += count[0][0]*count[1][1]*count[2][2];
		resp += count[0][0]*count[2][1]*count[1][2];
		resp += count[1][0]*count[0][1]*count[2][2];
		resp += count[1][0]*count[2][1]*count[0][2];
		resp += count[2][0]*count[0][1]*count[1][2];
		resp += count[2][0]*count[1][1]*count[0][2];
		printf("Case #%d: %I64d\n", t+1, resp);
    }
	return 0;

}

