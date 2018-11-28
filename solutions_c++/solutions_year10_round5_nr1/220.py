/*
 *  A.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۳/۲۲.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>

using namespace std;

const int MaxK= 10 +2;
int d, k, n, A, B, P, maxi;
int num[MaxK], tmp[MaxK];

inline bool isprime(int k){
	if (k == 1)
		return false;
	for (int i=2 ; i*i<=k ; i++)
		if (k%i == 0)
			return false;
	return true;
}
/*****************************/
inline int mod(int a, int m){
	return a%m>0 ? a%m : a%m+m;
}
/*****************************/
inline bool hasAns(int a){
	for (int i=0 ; i<k-1 ; i++)
		tmp[i]= num[i+1] - num[i]*a;
	if (k==2)
		return false;
	sort(tmp, tmp+k-1);
	int gcd= tmp[k-2] - tmp[0];
	if (gcd==1){
		for (int i=0 ; i<k-2 ; i++)
			if (tmp[i+1]==tmp[i])
				return false;
		int res= -1;
		for (int i=n ; i>=2 ; i--)
			if (isprime(i)){
				res= i;
				break;
			}
		if (res == -1)
			return false;
		A= a%res;
		B= 1;
		P= res;
		return true;
	}
	for (int i=1 ; i<k-1 ; i++)
		gcd= __gcd(gcd, tmp[i]-tmp[i-1]);
	if (gcd < 0)
		gcd= -gcd;
	for (int i=2 ; i*i<=gcd ; i++)
		if (gcd%i == 0){
			if (i > maxi){
				gcd= i;
				break;
			}
			while(gcd%i==0)
				gcd/= i;
		}
	
	if (gcd<=maxi || !isprime(gcd))
		return false;
	A= a%gcd;
	P= gcd;
	B= mod(tmp[0], P);
	return true;
}
/*****************************/
int pwr(int a, int b){
	int res= 1;
	for (int i=0 ; i<b ; i++)
		res*= a;
	return res;
}
/*****************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		cin >> d >> k;
		maxi= 0;
		for (int i=0 ; i<k ; i++){
			cin >> num[i];
			if (num[i] >maxi)
				maxi= num[i];
		}
		if (k == 1){
			printf("Case #%d: I don't know.\n", t);
			continue;
		}
		bool find= false;
		for (int i=0 ; i<k-1 ; i++)
			if (num[i] == num[k-1]){
				printf("Case #%d: %d\n", t, num[i+1]);
				find= true;
				break;
			}
		if (find)
			continue;
		n= pwr(10, d);
		int res= -1;
		for (int i=0 ; i<n ; i++)
			if (hasAns(i)){
				if (P <= n){
					if (res == -1 || res==(num[k-1]*A + B)%P)
						res= (num[k-1]*A + B)%P;
					else{
						res= -1;
						break;
					}
				}
			}
		printf("Case #%d: ", t);
		if (res == -1)
			cout << "I don't know." << endl;
		else
			cout << res << endl;
	}
	return 0;
}

