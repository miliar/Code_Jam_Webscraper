#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int n;
int lB[1000];
int rB[1000];

int IntCount()
{
	int j = 0;
	int i = 0;
	int k = 0;
	while (i<n){
		j=0;
		while (j<n) {
			//cout<<lB[j]<<" "<<rB[j]<<endl;
			
			if ((lB[i]>lB[j])&&(rB[i]<rB[j]))
				k++;
			j++;
		}
		i++;
	}
	return(k);
}

int main (int argc, char * const argv[]) {
	int t,i = 0;
    cin >> t;
	
	string strRes;
	
	while (t--) {
		cin>>n;
		i++;
		int j = 0;
		while (j<n) { // грузим
			cin >> lB[j] >> rB[j];
			j++;
		}
		cout<<"Case #"<<i<<": "<<IntCount()<<endl;
	}
    return 0;
}
