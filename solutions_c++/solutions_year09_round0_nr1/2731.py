#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main(void) {
   int l, d, m;
   int i, j, k,vez, flag, flag2, resp;
   int num;
   string pal;
   vector<string>::iterator it;
   vector<string> dic;
   string est;
   cin >> l >> d >> m;
   for(i=0; i<d; i++) {
      cin >> pal;
      dic.push_back(pal);
   }
   sort(dic.begin(),dic.end());

   for (i=0;i<m;i++) {
      resp=0;
      cin >> est;
      for (it=dic.begin(); it!=dic.end(); ++it) {
            pal=*it;
            flag=1;
            num=0;
            for(j=0; j<est.size();j++) {
               if (est[j]==pal[num]) {
                  num++;
               } else {
                  if(est[j]=='(') {
                     flag2=1;
                     while(est[j]!=')') {
                        j++;
                        if(est[j]==pal[num] && flag2) {
                           num++;
                           flag2=0;
                        }
                     }
                     if (flag2) {
                        flag=0;
                        break;
                     }
                  } else {
                     flag=0;
                     break;
                  }
               }
            }
            if (flag)
               resp++;
      }
      cout << "Case #" << i+1 << ": " << resp <<endl;
   }

/*   for (it=dic.begin(); it!=dic.end(); ++it)
      cout << *it << " ";
   cout << endl;
  */ 
   return 0;
}
