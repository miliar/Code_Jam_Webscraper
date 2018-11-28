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
	ofstream cout("zhao.txt");
	int T, N, P, C;
	cin >> T;

	int score[100];

	for(int q = 1; q <= T; q++)
	{
		cin>>C>>N>>P;
		for(int i = 0; i < C; i++)
			cin >> score[i];
		int j, k=0;
		for(j = 0; j < C; j++)
	    {
			while(N){
			if(((score[j]<=(3*P-3))&&(score[j]>=(3*P-4)))&&(P>1))
			{	
				N--;
				k++;
			}
			break ;
			}
			if((score[j]>=(3*P-2)&&(P>1))||((P==0)||(score[j]>0&&P==1)))
			{
				k++;
			}			
		}	
		cout << "Case #" << q << ": " << k<< endl;
	}
	return 0;
}