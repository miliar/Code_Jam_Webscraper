#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int T; 
	int N;
	cin >> T;
	for (int cas =0 ; cas < T; cas ++)
	{
		cin >> N;
		vector< pair<int,int> > AB;
		    for(int i=0; i< N; i++)
		    {
			    int a,b;
			    cin>> a >> b ;
			    AB.push_back(pair<int,int> (a,b));
		    }
			sort(AB.begin(), AB.end() );
			int cmpt =0;
		for(int i=0; i<N; i++)
			for(int j=i+1; j<N; j++) 
				if (AB[i].second > AB[j].second)
					cmpt++;
		cout << "Case #" << cas+1 <<  ": "<< cmpt << endl ;;
	}
	return 0;
}

