// <-------------------[sWitCHcAsE]---------------------->
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<cstring>
#include<cassert>
#include<queue>

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORS(i,a,n) for(i=a;i<n;i++)
#define ERR(x) cerr<<#x<<" "<<x<<endl
#define pb push_back
using namespace std;
typedef vector<int> VI;
typedef long long ll;
typedef long double ld;
 
int primes[]={2,3,5,7, 11, 13, 17, 19, 23, 29 , 31,37, 41, 43, 47, 53, 59, 61, 67, 71 , 73, 79, 83, 89, 97,101,103,107,109,113 ,127,131,137,139,149,151,157,163,167,173 ,179,181,191,193,197,199,211,223,227,229 ,233,239,
241,251,257,263,269,271,277,281 ,283,293,307,311,313,317,331,337,347,349 ,353,359,367,373,379,383,389,397,401,409 ,
419,421,431,433,439,443,449,457,461,463 ,467,479,487,491,499,503,509,521,523,541 ,547,557,563,569,571,577,587,593,
599,601 ,607,613,617,619,631,641,643,647,653,659 ,661,673,677,683,691,701,709,719,727,733 ,739,743,751,757,761,769,
773,787,797,809 ,811,821,823,827,829,839,853,857,859,863 ,877,881,883,887,907,911,919,929,937,941 ,947,953,967,971,977,983,991,997}; 

int gcd(int a,int b) {
	if(b==0)return a;
	else return gcd(b,a%b);
}
int main(int argc,char** args)
{

 	int N,T;
 	int n=sizeof(primes)/4;
 	//cerr<<"SIZE IS "<<n<<endl;
 	scanf("%d",&T);
 	FOR(kase,T) {
 		cout<<"Case #"<<kase+1<<": ";
 		scanf("%d",&N);
 		if(N==1) {
 			cout<<"0\n";
 			continue;
 		}
 		int large=1;
 		int small=0;
 		ll curr=1;
 		int g;
 		int ans=1;
 		FOR(i,n) {
 			if(N>=primes[i]) {
 				int lg=log(N)/(log(primes[i]));
 				ans+=(lg-1);
 			}
 		}
 		
 		//cerr<<"LARGE "<<large<<endl;

 		FOR(i,n) {
			if(N>=primes[i]) {
				small++;
			}
			
 		}
 		cout<<ans<<endl;
 	}
 	
}
