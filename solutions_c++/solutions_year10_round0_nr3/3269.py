#include <iostream>
#include <string>
#include <math.h>

using namespace std;

long int GetSum(int *ar, long int r, long int k,int n)
{
	long int sum = 0;
	
	int last_in=-1; //последний влезжий
	
	for (int i=0; i<r; i++) {//заезд
		int in_k = 0;//внутри
		int first_in = last_in; // первый кто влез
		while(1) 
		{
			if ((ar[last_in+1]+in_k)<=k)// влезает
			{
				in_k += ar[last_in+1]; //  сажаем
				last_in++;
				sum+=ar[last_in];
				if ((last_in +1)==n) // сначала очередьи
					last_in = -1;
				if (last_in == first_in) // все катаются
					break;
				continue;
			}
			break;
		}
	}
	return(sum);
}


int main (int argc, char * const argv[]) {
	int t,i = 0;
    cin >> t;
	int r,k,n; // r заезды; k влезает; n количество групп
	int ar[1000]; // буфер для группы
	while (t--) {
		cin>>r>>k>>n;
		i++;
		int i2 = 0;
		while (i2<n) {
			cin>>ar[i2];
			i2++;
		}
		
		cout<<"Case #"<<i<<": "<<GetSum(ar, r, k, n)<<endl;
	}
    return 0;
}
