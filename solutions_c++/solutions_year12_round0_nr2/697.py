long long gcd(long long a, long long b) {
     if( a<0 || b<0) 
         cerr << "Attempt to take gcd of -ve number (" << a << "," << b <<")\n";

    if (b==0) return a;
    else if (a==0) return b;
    else if (a > b) return gcd(a%b,b);
    else return gcd(a,b%a);
}

long long lcm(long long a, long long b) { 
     return (a*b)/gcd(a,b);
}

bool isPrime(long long num) {
     if (num <=1) return false;
     else if(num ==2) return true;
     
     long long sq = sqrt(num);
     for (long long i = 2 ; i <= sq ; i++) {
         if (num % i == 0) return false; 
     }
     return true;
}

int* getSieve(int n) {
     if (n<0) {
        cerr << "getSieve: input is -ve number " << n << endl;
        return NULL;
     }

     int* ans = new int[n+1];
     for (int i=0;i<=n;i++) {
         ans[i] = 1; // means true
     }

     ans[0] = 0;
     if (n>0) ans[1] = 0;
     int sq = sqrt(n);

     for (int i=2;i<=sq;i++) {
         if (ans[i]) {
            for (int j=i*2 ; j <=n ; j=j+i)
                ans[j] = 0;
         }
     }

     return ans;
}


long long fib(int n) {
     if(n<0) {
             cerr<< "fib: -ve input " << n << endl;
             return 0;
     }

     if(n==0) return 0;
     else if(n==1) return 1;

     long long x = 0;
     long long y = 1;
     for (int i=2;i<=n;i++) {
         long long temp = x+y;
         x = y;
         y = temp;
     }
     
     return y;
}


