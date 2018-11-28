#include <iostream>
#include <fstream.h>
using namespace std;
int main (int argc, char const *argv[]){
	ifstream in("input.txt");
	ofstream out("output.txt");
	int N;
	in>>N;
	for(int casenr = 1; casenr <= N; casenr++){
		int R, k, N;
		in>>R>>k>>N;
		int i;
		int arr[2*N];
		for(i=0;i<N;i++)
			in>>arr[i];
		for(i=0;i<N;i++)
			arr[i+N]=arr[i];
		int m1[N], m2[N];
		for(i=0;i<N;i++){
			int s=0;
			int j=i-1;
			while((j-i<N)&&s<=k)
				s+=arr[++j];
			
			m1[i]=(j+1)%N;
			if(!m1[i])
				m1[i]=N;
			m1[i]--;
			m2[i]=s-arr[j];

			// cout << m1[i]<<m2[i]<<endl;
		}
		int tmp1=0;
		long int sum=0;
		for(i=1;i<=R;i++){
			sum+=m2[tmp1];
			tmp1=m1[tmp1];
		}
		out<<"Case #"<<casenr<<": "<<sum<<endl;
	}
	return 0;
}