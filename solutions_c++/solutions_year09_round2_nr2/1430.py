 #include <iostream>
 #include <string>
 #include <boost/lexical_cast.hpp>



 using namespace std;
 using namespace boost;

 int main()
 {

     int caseNo;
     int num;
     cin >> caseNo;
     for(int curCase = 1; curCase <= caseNo; curCase++)
     {
         cin >> num;
         std::string numString(lexical_cast<string>(num));
         std::string original(numString);
         if ( next_permutation( numString.begin() , numString.end() ) )
             cout << "Case #" << curCase << ": " << numString << endl;
         else
         {
             original = "0" + original;
             next_permutation( original.begin() , original.end() );
             cout << "Case #" << curCase << ": " << original << endl;
         }
     }
     return 0;
 }