#include<iostream>
using namespace std;


int N;
int n;
char mm[200][200];
int zeros[200];
int ones[200];
double WP[200];
double OWP[200];
double OOWP[200];

void dealOWP()
{
	double result;
	for (int i = 0 ; i < n; i ++) {
		result = 0;
		for (int j = 0; j < n; j ++) {
			if(mm[i][j] != '.') {
				if(mm[j][i] == '0') {
					result = result + ((double)ones[j]) / ((double)(ones[j] + zeros[j] - 1));
				} else if( mm[j][i] == '1') {
					result = result + ((double)(ones[j] - 1)) / ((double)(ones[j] + zeros[j] - 1));
				}
			}
		}

		OWP[i] = result / ((double)(ones[i] + zeros[i]));
	}
}


void dealOOWP()
{
	double result;
	for (int i = 0 ; i < n; i ++) {
		result = 0;
		for (int j = 0; j < n; j ++) {
			if(mm[i][j] != '.') {
				result = result + OWP[j];
			}
		}

		OOWP[i] = result / ((double)(ones[i] + zeros[i]));
	}
}


void deal()
{

	for (int i = 0; i < n; i ++) {
		double result = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
		cout <<result<<endl;
	}
}


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out.txt", "w", stdout);

	cout.setf(ios::fixed);
	cout.precision(8);


	cin>>N;
	for (int cases = 1; cases <= N; cases ++) {
		cin>>n;
		cout<<"Case #"<<cases<<":"<<endl;

		memset(mm, 0, sizeof(mm));
		memset(zeros, 0, sizeof(zeros));
		memset(ones, 0, sizeof(ones));

		for (int i = 0; i < n ; i ++) {
			for (int j = 0; j < n; j ++) {
				cin >> mm[i][j];
				if(mm[i][j] == '0') {
					zeros[i] ++;
				} else if(mm[i][j] == '1') {
					ones[i] ++;
				}
			}

			WP[i] = (double)ones[i]/(double)(zeros[i] + ones[i]);
		}
		
		dealOWP();
		dealOOWP();
		deal();
	}

	return 0;
}

/*

  Input 
   
Output 
   
2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.
 Case #1:
0.5
0.5
0.5
Case #2:
0.645833333333
0.368055555556
0.604166666667
0.395833333333

 


  */