#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main()
{
	map<long long, long long> m;
	m[1]=1;
	m[2]=3;
	m[3]=7;
	m[4]=15;
	m[5]=31;
	m[6]=63;
	m[7]=127;
	m[8]=255;
	m[9]=511;
	m[10]=1023;
	m[11]=2047;
	m[12]=4095;
	m[13]=8191;
	m[14]=16383;
	m[15]=32767;
	m[16]=65535;
	m[17]=131071;
	m[18]=262143;
	m[19]=524287;
	m[20]=1048575;
	m[21]=2097151;
	m[22]=4194303;
	m[23]=8388607;
	m[24]=1677215;
	m[25]=33554431;
	m[26]=67108863;
	
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++){
		long long n,k;
		cin>>n>>k;
		long long c=m[n];
		if(n>26){
			cout<<"Case #"<<ii<<": OFF"<<endl;
		} else {
			if(k==c){
				cout<<"Case #"<<ii<<": ON"<<endl;
			} else if( (k-c)>0 && (k-c)%(c+1)==0){
				cout<<"Case #"<<ii<<": ON"<<endl;
			} else {
				cout<<"Case #"<<ii<<": OFF"<<endl;
			}
		}
	}
	return 0;
}

