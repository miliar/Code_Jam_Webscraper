#include <iostream>
#include <fstream>
using namespace std;

typedef unsigned long long ll;


struct POINT  {
	int x, y;
};

int multiply(const POINT& p1, const POINT& p2)
{
	return (p1.x*p2.y - p1.y*p2.x);
}

POINT p[1000];

int main()
{
	ofstream out("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\a.out");
	int N, otest;
    ll n, A, B, C, D, X0, Y0, M, X, Y;
    int i, j, k, s;
    cin >> N;
    for(otest = 0; otest < N;)  {
		s = 0;
		cin >> n >> A >> B >> C >> D >> X0 >> Y0 >> M;
		p[0].x = X0;  p[0].y = Y0;
 		for(i = 1; i < n; i++)  {
 	 		p[i].x = (A*p[i-1].x + B)%M;
     	 	p[i].y = (C*p[i-1].y + D)%M;
		}
		for(i = 0; i < n; i++)     {
		 	for(j = i+1; j < n; j++)    {
			   	for(k = j+1; k < n; k++)  {
    	  		  	POINT v1, v2;
                    v1.x = p[j].x - p[i].x;
                    v1.y = p[j].y - p[i].y;
                    v2.x = p[k].x - p[i].x;
                    v2.y = p[k].y - p[i].y;
                    //if(multiply(v1, v2) == 0)   continue;
					if(((p[i].x + p[j].x + p[k].x)%3 == 0) && ((p[i].y + p[j].y + p[k].y)%3 == 0))
						s++;
				}
   			}
   		}
   		out << "Case #" << ++otest << ": " << s << endl;
	}
	return 0;
}
                            
