#include <iostream>
#include <map>
#include <cassert>
#include <fstream>
#include <functional>
#include <string>

/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up

*/

void googlerese(const char* input) {

   using namespace std;;

   typedef map<char,char> AbcMap;
   AbcMap to_english;
   AbcMap to_goog;

   string sample_goog = "ejp mysljylc kd kxveddknmc re jsicpdrysi "
      "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd "
      "de kr kd eoya kw aej tysr re ujdr lkgc jv "
      "y qee "
      "z"
      //
      ;

   string  sample_english = "our language is impossible to understand "
      "there are twenty six factorial possibilities "
      "so it is okay if you want to just give up "
      "a zoo "
      "q"
      //
      ;
   
   assert(sample_goog.size() == sample_english.size());
   for (int i=0; i<sample_goog.size(); ++i) {
      to_english[sample_goog[i]] = sample_english[i];
      to_goog[sample_english[i]] = sample_goog[i];

   }
   //to_english.erase(' ');
   //to_goog.erase(' ');

   ifstream file(input);
   ofstream ofile("output.txt");
   
   int numcases;
   file >> numcases>>ws;
   for(int icase = 1; icase <=numcases ; ++icase)
   {
      string line;
      getline(file, line);
      ofile << "Case #" << icase << ": ";
      for(int i=0;i<line.size(); ++i)
         if ( to_english.find(line[i])!=to_english.end() )
            ofile << to_english[line[i]];
      else
         std::cerr << "not in dict  [" <<line[i] <<"]\n";
      ofile << endl;
   }

}

int main(int argc, const char* argv[]) {
   googlerese(argv[1]);
   return 0;
}
