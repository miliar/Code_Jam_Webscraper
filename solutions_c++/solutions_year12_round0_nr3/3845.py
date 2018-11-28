#include <iostream>
#include <fstream>
#define input "C-large.in"
#define output "C-large.out"
using namespace std;
typedef pair <int,int> ii;
ifstream in(input);
ofstream out(output);
int T,A,B;
int H[3000000];
int rotate(int data,int t){
	data*=10;
	return data%t+data/t;
}
void read()
{
	int i,j,data,s=0,x,t,ind=0;
	in >> T;
	for(i=1;i<=T;i++){
		in >> A >> B;
		for(j=A;j<=B;j++){
			ind++;
			data=x=j;
			t=1;
			while(x){
				x/=10;
				t*=10;
			}
			x=j;
			while(x){
				data=rotate(data,t);
				if(data >= A && data <= B && data > j && H[data]!=ind){
					s++;
					H[data]=ind;
				}
				x/=10;
			}
		}
		out << "Case #" << i << ": " << s << endl;
		s=0;
	}
}
int main()
{
	read();
	return 0;
}
