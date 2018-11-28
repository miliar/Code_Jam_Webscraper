#include <vector>

// utility function, makes a vector<t> broken up into segments by any single t into distinct vectors
template<typename t>
std::vector< std::vector<t> > vector_break (std::vector<t> input, t delim)
{
   std::vector< std::vector<t> > output;
   std::vector<t> temp;
   
   for ( int i = 0; i < input.size(); i ++ )
   {
      if ( input[i] == delim )
      {
         if ( temp.size() > 0 ) { output.push_back(temp); } // do not add empty vectors (i.e. if there is more than one space)
         temp.clear();
      }
      else { temp.push_back(input[i]); }
   }
   if ( temp.size() > 0 ) { output.push_back(temp); } // if there is an extra vector, grab it
   
   return output;
}
