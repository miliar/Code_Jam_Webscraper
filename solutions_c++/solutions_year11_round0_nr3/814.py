#include <fstream.h>
ifstream in("/Users/SunKim/Desktop/Codejam4/p4.in");
ofstream out("/Users/SunKim/Desktop/Codejam4/p4.out");

int t;
int n;
int max;
int data[1001];
int lastxor;
int sum;
int m=9999999;
int main(){
	int i,j;
	in >> t;
	for(int z=0;z<t;z++){
		lastxor=0;
		sum=0;
		m=9999999;
		in >> n;
		for(i=0;i<n;i++){
			in >> data[i];
			sum+=data[i];
			if(data[i]<m) m=data[i];
			lastxor=lastxor^data[i];
		}
		if(lastxor!=0){
			out << "Case #" << z+1 << ": NO\n";
		}else{
			out << "Case #" << z+1 << ": " << sum-m << "\n";
		}
	}
	return 0;
}