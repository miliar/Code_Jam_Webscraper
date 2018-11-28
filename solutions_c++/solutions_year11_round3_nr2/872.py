#include <fstream>
#include <algorithm>
using namespace std;

void main(){
	ifstream in;
	ofstream out;
	in.open("A-small.in");
	out.open("A-small.out");
	long long T;
	in>>T;
	for(long long cases=0;cases<T;cases++){
		long long L,t,N,C;
		in>>L>>t>>N>>C;
		long long a[1000];
		for(long long parsecs=0;parsecs<C;parsecs++) in>>a[parsecs];
		//Initialize distance list
		long long distance[1001];
		long long distCount=0;
		long long pointCount=0;
		long long limitpoint=-1;
		for(long long stars=0;stars<N;stars++){
			if(distCount<(t/2)){
				if((distCount+a[(stars%C)])>(t/2)){
					distance[pointCount]=(t/2)-distCount;
					long long remainder=(distCount+a[(stars%C)])-(t/2);
					distCount+=distance[pointCount];
					pointCount++;
					distance[pointCount]=remainder;
					limitpoint=pointCount;
					distCount+=distance[pointCount];
					pointCount++;
				}else{
					distance[pointCount]=a[(stars%C)];
					distCount+=distance[pointCount];
					pointCount++;
				}
			}else if(distCount==(t/2)){
				distance[pointCount]=a[(stars%C)];
				limitpoint=pointCount;
				distCount+=distance[pointCount];
				pointCount++;
			}else{
				distance[pointCount]=a[(stars%C)];
				distCount+=distance[pointCount];
				pointCount++;
			}
		}
		//Sort
		long long timeGain=0;
		if(limitpoint!=-1){
			sort(distance+limitpoint,distance+pointCount);
			for(long long boosters=0;boosters<L;boosters++){
				if(boosters<(pointCount-limitpoint)){
					timeGain+=distance[(pointCount-1-boosters)];
				}
			}
		}
//		for(int i=0;i<pointCount;i++) out<<distance[i]<<" ";
		out<<"Case #"<<(cases+1)<<": "<<((distCount*2)-timeGain)<<endl; 
	}
	in.close();
	out.close();
}