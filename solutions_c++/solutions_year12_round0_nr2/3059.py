#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <list>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <fstream>
using namespace std;



int main()
{
	ifstream cin("B-large.in");
	ofstream cout("b.txt");
	int n, l, m,c;
	cin >> n;

	int score[100];

	for(int q = 1; q <= n; q++)
	{
		cin>>c>>l>>m;
		for(int i = 0; i < c; i++)
			cin >> score[i];
		int j, k=0;

		for(j = 0; j < c; j++)
	    {
			while(l){
			if(((score[j]<=(3*m-3))&&(score[j]>=(3*m-4)))&&(m>1))
			{	
				l--;
				k++;

			}
			break ;
			}

			if((score[j]>=(3*m-2)&&(m>1))||((m==0)||(score[j]>0&&m==1)))
			{
				k++;
				//continue;
			}
			
				
					//continue;
				
		}
	
		
		cout << "Case #" << q << ": " << k<< endl;
	}

	return 0;
}