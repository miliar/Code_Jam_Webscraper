#include <iostream>
#include <stdlib.h>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

string convertInt(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

int main()
{
   int T;

   cin >> T;

   for(int loop=0; loop<T; ++loop)
   {
      int num;
      
      cin >> num;
      
      char buf[30];
      
      //itoa(num, buf, 10);
      string str = convertInt(num);
      strcpy(buf, str.c_str());
      
      int digits = strlen(buf);
      int pos = -1;
//      cout << digits << endl;
      for(int i=digits-2; i>=0; --i)
      {
         for(int j=digits-1; j>i; --j)
         {
//           cout << buf[i] << "\t" << buf[j] << endl;
//           cout << (int)buf[i] << "\t" << (int)buf[j] << endl;
            if( buf[j] > buf[i] )
            {
               pos = i;
               
               int temp = buf[i];
               buf[i] = buf[j];
               buf[j] = temp;
               
               break;
            }
            
         }

         if( pos != -1 )
            break;
         
      }
      
//      cout << buf << endl;
//      cout << pos << endl;
      if( pos != -1 )
      {
  //    cout << "sorting" << endl;
         sort(buf+pos+1, buf+digits);
      }
      else
      {
         int pos1 = digits-1;
         
         while( buf[pos1] == '0' )
            --pos1;
            
//         cout << "pos1" << pos1 << endl;
            
         int temp = buf[0];
         buf[0] = buf[pos1];
         buf[pos1] = temp;
         
         buf[digits] = '0';
         buf[digits+1] = '\0';
         
         sort(buf+1, buf+digits+1);
      }
      
      
      cout << "Case #" << loop+1 << ": " << buf << endl;

   }

   return 0;

}

