#include <cstdio>
#include <cmath>
using namespace std;

int flop(int orig) {
    return (orig/10) + ((orig%10)*(pow(10,floor(log10(orig)))));
}

int length(int n) {
    return(floor(log10(n)));
}

int flopten(int orig) {

    return (orig/10) + ((orig%10)*(pow(10,floor(log10(orig))+1)));
                    // 490 turned into 049 which is 49
                    // need to make it become 904 - HOW DO>!@#KL!@
                    //
                    // 12340 turns into 01234 which is 1234
                    // need to become 40123 -> 
                        // keep last digit -> 4
                        // divide by ten -> 123
                        // multiply last digit by the thing times ten -> 40000
                        // add togeter -> 40123
}

int main() {

    int numc;
    scanf("%d", &numc);
    for(int casen=0; casen<numc; casen++) {
        
        int start, end;
        scanf("%d %d", &start, &end);

        int count = 0;

        for(int i=start; i<=end; i++) {
            int upto = i;
            for(int j=0; j<length(i); j++) {
                upto = flop(upto);
                if(length(upto)<length(i)) {
                    upto=flopten(upto);
                }
                if(upto >= start && upto <= end && upto > i) {
                    count++;
                }
            }
        }
        printf("Case #%d: %d\n", casen+1, count);
    }
}
