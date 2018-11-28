#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool array[20000005];
int num[10000];
int dig[8];

int main(){
	int i,a,b;
	ifstream input;
	ofstream output;
	input.open("C-small-attempt0.in");
	output.open("C-small-attempt0.out");
	input>>i;
	int h=0;
	while (i--){
		input>>a>>b;
		int t=0;
		memset(array,0,sizeof(array));
		memset(num,0,sizeof(num));
		int c = 0;
		for (int s=a;s<=b;++s){
			if (array[s]) continue;
			else {
				num[c++] = 1;
				array[s] = true;
			}
			int temp = s,t = 0;
			while (temp>0){
				dig[t++] = temp%10;
				temp/=10;
			}
			for (int n=t-2;n>=0;--n){
				int j,m,sum = 0;
				if (!dig[n]) continue;
				for (m = n,j = t-1;j>=0;--m,--j){
					sum+=dig[(m+t)%t]*(int)pow(10.0,j);
					if (sum >b)break;
				}
				if (j<0) {
					if (sum>=a && !array[sum]){
						array[sum] = true;
						++num[c-1];
					}
				}
			}
			if (num[c-1] ==1|| num[c-1] == 0) num[--c] =0;
		}
		int result = 0;
		for (int s=0;s<c;++s)
			result += num[s]*(num[s]-1)/2;
		if (i >0) output<<"Case #"<<++h<<": "<<result<<endl;
		else output<<"Case #"<<++h<<": "<<result;
	}
	input.close();
	output.close();
	return 0;
}