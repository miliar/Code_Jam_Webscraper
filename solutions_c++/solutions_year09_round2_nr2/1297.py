#include <fstream>
#include <algorithm>
using namespace std;
int main(){
	int n,j,x,min,nom;
	char numbers[22];
	ifstream f("input.txt");
	ofstream f2("output.txt");
	f>>n;
	for(int i=0;i<n;i++){
		f>>numbers;
		for(j=0;j<20;j++){
			if (!numbers[j]) break;
		}
		x=j--;
		for(;j>-1;j--){
			if(numbers[j]<numbers[j+1]) break;
		}
		if (j!=-1){
			min=numbers[j+1];
			nom=j+1;
			for(int g=j+2;g<x;g++){
				if (numbers[g]>numbers[j] && min>numbers[g]){
					min=numbers[g];
					nom=g;
				}
			}
			numbers[nom]=numbers[j];
			numbers[j]=min;
			sort(&numbers[j+1],&numbers[x]);
			f2<<"Case #"<<i+1<<": "<<numbers<<endl;
		} else {
			sort(&numbers[0],&numbers[x]);
			if (numbers[0]=='0'){
				for(int f=0;f<x;f++){
					if (numbers[f]!='0'){
						numbers[0]=numbers[f];
						numbers[f]='0';
						break;
					}
				}
			}
			for(int g=x;g>0;g--){
				numbers[g]=numbers[g-1];
			}
			numbers[1]='0';
			numbers[x+1]=0;
			f2<<"Case #"<<i+1<<": "<<numbers<<endl;
		}
	}
	f2.close();
	f.close();
	return 0;
}
