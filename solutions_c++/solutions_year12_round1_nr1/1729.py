#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

int calc(int pattern, int numErase, double pA[], int A, int B)
{
	bool error = false;
	if(numErase == A + 1) return B + 2;
	for(int i = 0; i < A - numErase; i++)
		if(pattern >> i & 1)
			{
				error = true;
				break;
			}
	if(error) return (B - A + 2 * numErase + B + 2 );
	else return (B - A + numErase + 1 + numErase);
}


double solve(int A, int B, double pA[])
{
	double ans[A+2];
	int x = pow(2.000000, A);
	double attempt[x];
	for(int j = 0; j < x; j++)
		{
			attempt[j] = 1.000000;
			for(int k = 0; k < A; k++)
				{
					if((j >> k) & 1) attempt[j] *= (1-pA[k]);
					else attempt[j] *= pA[k];
				}
			//cout << attempt[j] << " ";
		}
	//cout << endl;
	for(int i = 0; i < A+2; i++)
		{
			int stroke[x];
			ans[i] = 0.000000;
			for(int j = 0; j < x; j++)
				{
					stroke[j] = calc(j, i, pA, A, B);
					ans[i] += stroke[j] * attempt[j];
					//cout << stroke[j] << " " << attempt[j] << endl;
				}
			//cout << ans[i] << endl;
		}
	return *min_element(ans, ans+A+2);
}

int main(){
	int T, A, B;
	fstream ps("statement.txt");
	fstream output("output.txt",fstream::trunc | fstream::out);
	ps>>T;
	int i=1;
	while(i!=T+1){
		string str;
		do {
			getline(ps,str);
		}while(str=="");
		stringstream ss(str);
		ss >> A >> B;
		//cout << A << " " << B << endl;
		getline(ps,str);
		stringstream ss1(str);
		double pA[A];
		for(int j = 0; j < A; j++)
			{		
				ss1 >> pA[j];
			}
		//cout << endl;
		double ans = solve(A, B, pA);
		printf("Case #%d: %f\n", i, ans);
		//cout<<"Case #"<<i<<": "<<solve(str,str1,N)<<endl;
		i++;	
	}
	return 0;
}	
