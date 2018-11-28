#include<iostream>
#include<stdio.h>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

/*
 * This program reads from stdin and writes to stdout.
 * Run it with
 *     program < input.txt > output.txt
 */

class walk
{
public:
	int b , e , w;
	bool operator<(const walk &x) const
	{
		return w < x.w;
	}
};

walk IN[1000];

int main()
{
    int T;
    cin >> T;
    for(int t1 = 0 ; t1 < T ; t1++)
    {
        cerr << "Test " << t1 + 1 << "\n";
        int X , V1 , V2 , N;
        double TT;
        cin >> X >> V1 >> V2 >> TT >> N;
        int l = 0;
        for(int i = 0 ; i < N ; i++)
        {
        	cin >> IN[i].b >> IN[i].e >> IN[i].w;
        	l += IN[i].e - IN[i].b;
        }
        IN[N].b = 0; IN[N].e = X - l; IN[N].w = 0; N++;
        sort(IN , IN + N);
        double t = 0;
        for(int i = 0 ; i < N ; i++)
        {
        	if(IN[i].e - IN[i].b < TT * (IN[i].w + V2))
        	{
        		t += 1.0 * (IN[i].e - IN[i].b) / (IN[i].w + V2);
        		TT -= 1.0 * (IN[i].e - IN[i].b) / (IN[i].w + V2);
        	}
        	else
        	{
        		t += TT + (IN[i].e - IN[i].b - TT * (IN[i].w + V2)) / (IN[i].w + V1);
        		TT = 0;
        	}
        }
        printf("Case #%d: %.10lf\n" , t1 + 1 , t);
    }
}





