#include <fstream>
#include <exception>
#include <vector>

typedef unsigned int uint;
typedef long ssize_t;

typedef std::vector<uint> Nums;
Nums freq;

ssize_t getMax( Nums const & nums )
{
   uint max = 0;
   ssize_t pos = -1;
   for( size_t i = 0; i < nums.size(); ++i )
   {
      if( nums[i] > max )
      {
         pos = i;
         max = nums[i];
      }
   }
   return pos;
}

unsigned long long solve( size_t p, size_t k )
{
   Nums freq_copy( freq );
   
   std::vector<uint> keys;
   keys.resize( freq.size() );
   
   size_t currKey = 0;
   size_t numOfPress = 1;
   while( true )
   {
      ssize_t pos = getMax( freq );
      if( pos == -1 )
      {
         break;
      }
      keys[pos] = numOfPress;
      freq[pos] = 0;
      ++currKey;
      if( currKey >= k )
      {
         currKey = 0;
         ++numOfPress;
      }
   }
   
   unsigned long long result = 0;
   for( size_t i = 0; i < keys.size(); ++i )
   {
      result += (keys[i]*freq_copy[i]);
   }

   return result;
}

int main()
{
   std::ifstream ifile( "input.txt" );
   if( !ifile )
   {
      throw std::runtime_error( "Could not open input file" );
   }
   std::ofstream ofile( "output.txt" );
   
   size_t testsCount;
   ifile >> testsCount;
   
   for( size_t testNo = 0; testNo < testsCount; ++testNo )
   {
      ofile << "Case #" << testNo + 1 << ": ";
      
      size_t p, k, l;
      ifile >> p >> k >> l;
      freq.clear();
      for( size_t i = 0; i < l; ++i )
      {
         uint letter;
         ifile >> letter;
         freq.push_back( letter );
      }
      
      unsigned long long result = solve( p, k );
      {
         ofile << result;
      }
      ofile << std::endl;
   }
}