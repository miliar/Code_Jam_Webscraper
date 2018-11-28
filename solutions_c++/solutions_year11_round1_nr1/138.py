#include<cstdio>
#include<cstdlib>

unsigned long int gcd(unsigned long int a, unsigned long int b) {
       return (b == 0 ? a : gcd(b, a % b));
}

unsigned long int T,N,PD,PG;
bool possible() {
    if((PG == 0 || PG == 100) && (PG != PD))
        return false;
    if(N < 100/gcd(PD,100))
        return false;
    return true;
}

int main(int argc, char* argv[]){
    if(argc < 3)
        return 1;
    FILE* in = fopen(argv[1], "r");
    FILE* out = fopen(argv[2], "w");
    fscanf(in, "%ld", &T);
    for(unsigned long int t=1; t<=T; t++){
        fscanf(in ,"%ld %ld %ld", &N, &PD, &PG);
        fprintf(out, "Case #%ld: %s\n", t, possible()?"Possible":"Broken");
    }
    return 0;
}
