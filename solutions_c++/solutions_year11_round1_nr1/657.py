#include<iostream>
#include<cstdio>

using namespace std;

long long int gcd(long long int a, long long int b) {
    long long int max;
    long long int min;
    long long int tmp;
    if (a==0 ) return 0;
    max = (a>b)?a:b;
    min = (a<b)?a:b;
    do {
	tmp = max % min;
	max = min;
	min = tmp;
    }while (min!=0);
    return max;
}

int main(int artc, char* argv[]) {

    int TIME;// number of test
    int answer;// Final answer
    cin >> TIME;
    long long int N, PD, PG;
    long long int fad,fag;
    int flag;

    for (int t = 0 ; t < TIME; t++) {
	cin >> N >> PD >> PG;
	fad = gcd(PD,100);
	if ((fad!=0) && 100/fad > N) {
	    flag = 0;
	}
	else 
	    flag = 1;
//	fag = gcd(PG,100);
	//output
//	cout << fad << "\t" << fag << endl;
	if ((PG==100 && PD!=100)|| (PD!=0 && PG==0) || flag == 0)
	    printf("Case #%d: Broken\n",t+1);
	else
	    printf("Case #%d: Possible\n",t+1);
    }
    return 0;
}
