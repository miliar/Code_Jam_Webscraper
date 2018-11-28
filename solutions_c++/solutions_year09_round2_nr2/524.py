using namespace std;
#import <iostream>
#import <algorithm>

char number[22];
char temp[22];

int main()
{
   int t; // number of test cases
   cin >> t;
   int c = 0;
   while (c++ < t)
   {
      cin >> number;
      strcpy(temp, number);
      next_permutation(temp, temp+strlen(temp));
      
      cout << "Case #" << c << ": ";
      if (strcmp(temp, number) <= 0)
      {
         strcpy(temp, "0");
         strcat(temp, number);
         next_permutation(temp, temp+strlen(temp));
         cout << temp << endl;
      }
      else cout << temp << endl;
   }
   return 0;
}
