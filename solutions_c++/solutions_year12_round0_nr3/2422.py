#include <iostream>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>

#define ASCII_SPACE 32
#define ASCII_NEWLINE 10


using namespace std;




#define PRINT_TOKEN(token)\
	do{\
		cout<<#token<<" is "<<token<<endl; \
	}while(0)


#define READ(arg)\
	do{\
		long long arg;\
		cin>>arg;\
	}while(0)

//#define PRINT_ARR()
typedef long long ll;

int main()
{
	long long T;

	cin>>T;
	
	for(long long i=0;i<T;i++){

		long long result=0 ;
		ll A,B;
		cin>>A>>B;
	
		char temp[16];
		sprintf(temp,"%lld",A);

		int len=0;
		while(temp[len] != '\0') len++;
	//	cout <<"len="<<len<<endl;
		for(ll r=A;r<=B;r++){
			char val[16];

			sprintf(val,"%lld",r);
			
			vector <ll> record;
			for(int s=1;s<len;s++){
				
				char val2[16];
				val2[len] = '\0';
				for(int ss=0;ss<len;ss++){
					val2[ss] = val[ (s+ss)%len ];
				}
				ll co = atoi(val2);

				bool found=false;
				for(int f=0;f<record.size();f++){
					if(record[f] == co){
						found=true;
						break;
					}
				}
				if(co <= B && co > r &&!found){
					record.push_back(co);
	//				cout<<result+1<<":"<<val<<","<<val2<<endl;
					result++;
				}
			}
		}
		cout<<"Case "<<"#"<<i+1<<": "<<result;
		cout<<endl;

	}
	return 0;
}


