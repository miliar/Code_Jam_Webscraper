#include<iostream>
#include<fstream>
#include<cmath>
#include<cstring>
#include<cstdlib>

using namespace std;

int main(){
    int t;
    char x[10];
    char tmp[10];
    ofstream fout;
    cin >> t;
    fout.open("output.txt");
    for (int i=0; i<t; i++) {
        int a, b, z, bit, len, ans = 0, last[10];
        cin >> a >> b;
        for (int j=a; j<=b; j++) {
            itoa(j, x, 10);
            len = strlen(x);
            bit = len-1;
            int num = 0;
            while (bit > 0){
                  for (int k=0; k<len-bit; k++)
                      tmp[k] = x[k+bit];
                  for (int k=len-bit; k<len; k++)
                      tmp[k] = x[k-len+bit];
                  tmp[len]='\0';
                  z = atoi(tmp);
                  if (tmp[0]!=0 && z>j && z<=b && z>=a) {
                     bool find=false;
                     for (int l=0; l<num; l++)
                         if (last[l]==z) find=true;
                     if (!find) {
                        ans++;
                        last[num] = z;
                        num++; 
                     }
                  }
                  bit--;
            }
        }
        fout << "Case #" << i+1 << ": " << ans << endl; 
    }
    fout.close();
    return 0;
}
