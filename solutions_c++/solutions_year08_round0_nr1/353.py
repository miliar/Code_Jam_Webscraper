// QualA.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>

using namespace std;

int s, q;
string engines[101];
string queries[1001];

int optimize() {
	int change[1001][101];
	int min, next;
	for(int i=0; i<=q; i++) {
		next = 9999;
		for(int j=0; j<s; j++) {
			if(i == 0)
				change[i][j] = 0;
			else
				if(queries[i-1] == engines[j])
					change[i][j] = 9999;
				else {
					change[i][j] = change[i-1][j];
					if(min + 1 < change[i][j])
						change[i][j] = min + 1;
				}
			if(change[i][j] < next)
				next = change[i][j];
		}
		min = next;
	}
	return min;
}

int main(int argc, char* argv[])
{
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>s;
		cin.ignore();
		for(int j=0; j<s; j++)
			getline(cin, engines[j]);
		cin >>q;
		cin.ignore();
		for(int j=0; j<q; j++)
			getline(cin, queries[j]);

		cout <<"Case #" <<i+1 <<": " <<optimize() <<endl;
	}
	return 0;
}

