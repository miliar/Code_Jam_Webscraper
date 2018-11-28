#include <iostream>
#include <cmath>
using namespace std;

int main () {

       int  t,n;
       long long r, k, g;
       // read t
       cin >> t;
       long long sum = 0;
       for (int i = 0; i< t; i++) {
        
           sum  = 0;
           cin >> r >> k >> n;
           long long group[n];
           long long people =0;
           for (int j = 0; j < n; j++) {
           
               cin >> group[j];
               people += group[j];
           }

           if (people == k) {
                sum = r * people;
           } else {
         
               int pos = 0;
               bool flagpos = false;;
               long long posi[n];
               long long posriders[n];
               int count = 0;
               for (int ride = 0; ride < r; ride++) {
                
                   int riders = 0;
                   int plecare = pos;
                   bool flag = true;
                   while (flag) {
                   
                       riders += group[pos];
                       pos++;
                       if (pos ==n) pos = 0;
                       if (pos == plecare) flag = false;
                       if ((riders+group[pos]) > k) flag = false;
                   }
                   sum += riders;
                   if (!flagpos) {
                   posi[count] = plecare;
                   posriders[count] =riders;
                   bool findpos = false;
                   int foundposition;
                   for (int q = 0; q<count; q++) {
                       if (posi[count] == posi[q]) {
                           findpos = true;
                           foundposition = q;
                           break;
                       }
                   }
                   //found position 
                    if (findpos) {
                        int start = foundposition;
                        int stop = count-1;
                        int length = stop- start;
                        long long  poeple = 0;
                        sum -=posriders[count];
                     //   cout << "start: "<<start <<endl;
                      //  cout << "stop: " <<stop <<endl;
                       // cout << "length: "<<length <<endl;
                        for (int w = start;w<=stop;w++) {
                            poeple += posriders[w];
                        }
                        length++;
                       int ridesleft = r- ride;
                       long long  aux = ridesleft / length;
                       sum += aux*poeple;
                       ridesleft = ridesleft%length;
                      // cout<<"aux: " <<aux<<endl;
                     //  cout <<"ridesleft: "<<ridesleft<<endl;
                        while (ridesleft>0) {
                            sum +=posriders[start];
                            start++;
                            ridesleft--;
                        }
                        break;
                    }
                    count++;
                   }
               }
           }
           cout <<"Case #" <<i+1<<": " <<sum <<endl;
       }
}
