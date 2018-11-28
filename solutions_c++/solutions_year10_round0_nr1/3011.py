#include <limits.h>
#include <iostream>
#include <stdio.h>
#include <bitset>
#include <string>
  
using namespace std;
	
template < typename T > inline T highbit(T& t)
{
	return t = (((T)(-1)) >> 1) + 1;
}

template < typename T >
string bin(T& value, string res)
{
	for ( T bit = highbit(bit); bit; bit >>= 1 )
	{
		res+=  ( ( value & bit ) ? '1' : '0' );
	}
	return res;
}


int main()
{


	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int cases;
	scanf("%d\n",&cases);
	int n;
	unsigned int k;
	string bi="";
	string result="";	
	for(int i=0;i<cases;i++){

		bi="";
		result="";
		scanf(" %d %d\n",&n,&k);
		
		
		result = bin(k, bi);
		
		int flag=0;
		
		if(k>=n && n){
			flag=1;
			for(int j=result.size()-1;j>result.size()-1-n;j--){	
					if(result[j]=='0'){
						flag=0;
						break;
					} 
			}
		}else{
			
			flag=0;
		}
		
		if(flag){
	
				printf("Case #%d: ON\n",i+1);
			
		}else{
				printf("Case #%d: OFF\n",i+1);
		}




	}

	

	


	return 0;
}


