#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;


bool win(int a, int b){
	

	
	
	int temp;
	if (a==b)
		return false;
	
	// so b is always bigger than a
	if (b<a){
		temp = a;
		
		a = b;
		b = temp;
		
	}
	
	bool Aturn=true;
	
	while (1){
		
		if ((a==1 || b ==1) && !(a==1 && b==1) && Aturn)
			return true;
		
		if (a%b==0 && a!=b && Aturn)
			return true;
		else if (a%b==0 && a==b && Aturn)
			return false;

		
		int q=b/a;

		if (q>=2 && Aturn)
			return true;
		else if (q>=2 && !Aturn)
			return false;
	
	
		b=b-q*a;
		temp=b;
		b=a;
		a=temp;
		
		
		Aturn=!Aturn;
		
	}
	
	
}

int main()
{
	int line;
	cin >> line;
	
	int count, A1, A2, B1, B2;

	for (int z=0; z<line; z++){
		count=0;
		cin>>A1>>A2>>B1>>B2;
		
		for (int i=A1; i<=A2; i++)
			for (int j=B1; j<=B2; j++){
				if (win(i, j)){
					count++;
				}
					
			}
		
		printf("Case #%d: %d\n", z + 1, count);

			
	}
	


	 

	
	return 0;
}
