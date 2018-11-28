#include<iostream>
   #include <gmpxx.h>

#include<vector>
#include<algorithm>

//Uses the (I think standard) Gnu multiple precision library: http://gmplib.org/
//compile with g++ a.cpp -lgmpxx -lgmp


mpz_class gcd(mpz_class p, mpz_class q){

	if (q > p) return gcd(q,p);
	if (q == 0) return p;
	//std::cout<<p<<' '<<q<<' '<<p%q<<std::endl;
	return gcd( q, p%q);
}


mpz_class bgcd(std::vector < mpz_class >& nums){
	if (nums.size()==1) return nums[0];
// std::cout<<"e"<<std::endl;
	mpz_class res=gcd(nums[0],nums[1]);
   	// std::cout<<"e"<<std::endl;
	for (int i=2; i<nums.size(); i++)
		res=gcd(res, nums[i]);

	return res;
}

int main(){
	int numcases;
	std::cin>>numcases;
	for (int c=1; c<=numcases; c++){
		int n;
		std::cin>>n;
		
		std::vector<  mpz_class > numbers(n);
		//cout<<numbers[0]<<endl;
		for (int i=0; i< n; i++){
			std::cin>>numbers[i];
		}
		std::sort(numbers.begin(), numbers.end());
		std::vector< mpz_class > differences(n-1 + (n==1));
		if (n==1) differences[0]=numbers[0];
		else
		for (int i=0; i<n-1; i++) differences[i]=numbers[i+1]-numbers[i];

		std::sort(differences.begin(), differences.end());

		mpz_class T=bgcd(differences);

		std::cout<<"Case #"<<c<<": "<<(T-numbers[0]%T)%T<<std::endl;
		
	}
	return 0;
}