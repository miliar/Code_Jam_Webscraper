# include <iostream>
# include <cstdio>
# include <map>
# include <string>
# include <sstream>

using namespace std;

int num_digits(int num) {
 int c = 0;
 
 while (num > 0) {
      num /= 10;
      c++;
       }

       return c;
}

int main()
{
 freopen("C-small-attempt0.in", "r", stdin);   
 freopen("output.txt", "w", stdout);
 
 int T, cas = 0;
 cin>>T;
 
 while (T--) {
       int A, B;
       cin>>A>>B;
       
       map<pair<string, string>, bool> used;
       
       int c = 0;
       for (int i = A; i <= B; ++i) {
           stringstream ss;
           ss<<i;
           
           string num_str;           
           ss>>num_str;
           
           for (int j = 0; j < num_str.size(); ++j) {
               if (j + 1 < num_str.size() && num_str[j + 1] != '0'){
                              string recycled_num = num_str.substr(j + 1) + num_str.substr(0, j + 1);
                              int rec_num;
                              sscanf(recycled_num.c_str(), "%d", &rec_num);
                              pair<string, string> p(num_str, recycled_num);
                              pair<string, string> rp(recycled_num, num_str);
                                                            
                              if (!used[p] && !used[rp] && num_str != recycled_num && rec_num >= A && rec_num <= B && num_digits(rec_num) == num_digits(i)) {
                                    c++;                                   
                                    used[p] = true;                                    
                                    used[rp] = true;
                                    }
                              }               
               }
           }    
           cout<<"Case #"<<++cas<<": "<<c<<endl; 
           }
}
