#include <string>
#include <iostream>

using namespace std;

main()
{
int pom,pomv,T,n,x[1000],y[1000],i,j;
double sum;
cin >> T;
for (i=1;i<=T;i++) 
{
sum = 0;
cin >> n;


for (j=0;j<n;j++) {
cin >> x[j];
}

for (j=0;j<n;j++) {
cin >> y[j];
}
pom = 1;
while (pom == 1) {
pom = 0;
for (j=1;j<n;j++) {
	if (x[j] < x[j-1]) { 
		pomv = x[j]; 
		x[j] = x[j-1];
		x[j-1] = pomv;
		pom = 1;		
		}	
	}
}

pom = 1;
while (pom == 1) {
pom = 0;
for (j=1;j<n;j++) {
	if (y[j] > y[j-1]) { 
		pomv = y[j]; 
		y[j] = y[j-1];
		y[j-1] = pomv;
		pom = 1;		
		}	
	}
}

for (j=0;j<n;j++) {
sum = sum + (x[j]*y[j]);
}
cout.precision(0);
cout << "Case #" << i << ": " << fixed << sum << endl ;


} //for i
} //main()
