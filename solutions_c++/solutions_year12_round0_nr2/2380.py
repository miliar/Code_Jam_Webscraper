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
		int N,S,p;
		int ti[100];
		cin>>N>>S>>p;

		for(int e=0;e<N;e++){
			cin>>ti[e]; 

			int v = ti[e] / 3 ;
			int vr = ti[e] % 3;

			int num;
			num = v;

			if( num  >= p) result++;
			else if(vr>0 && vr<3 && num+1 >= p) result++;
			else if( S>0 && num+2>= p && vr==2){
				S--;
				result++;
			}else if(S>0 && num+1 >=p && vr==0 && ti[e] > 0 ){
				S--;
				result++;
			}
		}


		cout<<"Case "<<"#"<<i+1<<": "<<result;
		cout<<endl;

	}
	return 0;
}


