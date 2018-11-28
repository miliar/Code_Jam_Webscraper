#include<iostream>
#include<fstream>
#include<string>

using namespace std;

const double PI=3.14159265358979323846264338327950288;
ifstream fin;
ofstream fout;

int N,D;
int d[10001],l[10001];

int larger(int a, int b){
    if(a>b) return a;
    else return b;
}

bool swing(int pos, int vine){
	int max = d[vine]-pos + d[vine];
	if(D<=max) return 1;
	else if(d[vine+1]>max && vine+1<N) return 0;
	else{
		int index = vine+1;
		while(max>=d[index] && index<N){
			int start = larger(d[vine],d[index]-l[index]);
			if(swing(start,index)) return 1;
			else index++;
		}
		return 0;
	}
}

void _main(){
	int i,j,k;
	int index;
	fin>>N;
	for(i=0;i<N;i++) fin>>d[i]>>l[i];
	fin>>D;
	
	if(swing(0,0)) fout<<"YES";
	else fout<<"NO";
}

int main(){
    fin.open("sample.in");
    fout.open("result.out");
    int T;
    fin>>T;
    for(int i=0;i<T;i++){
            fout<<"Case #"<<i+1<<": ";
            cout<<"Case #"<<i+1<<" is runing"<<endl;
            _main();
            fout<<endl;
    }
}
