#include <iostream>
#include <vector>
#include <stdexcept>
#include <algorithm>

class Set
{
private:
   typedef std::vector<bool> Entries;

public:
   typedef std::vector<std::string> Names;

public:
   explicit Set( Names const & names ):
      m_names( names),
      m_count( names.size() ),
      m_resets( 0 )
   {
      m_entries.resize( m_names.size(), true );
      std::sort( m_names.begin(), m_names.end() );
   }

   size_t count() const { return m_count; }
   size_t size() const { return m_entries.size(); }
   size_t resets() const { return m_resets; }

   bool remove( std::string const & name )
   {
      Names::iterator it = std::lower_bound( m_names.begin(), m_names.end(), name );
      if( it == m_names.end() )
      {
         throw std::runtime_error( "No entry: " + name );
      }
      return remove( it - m_names.begin() );
   }

private:
   bool remove( size_t pos )
   {
      bool wasReset = false;
      if( m_entries[ pos ] )
      {
         --m_count;
         if( m_count == 0 )
         {
            ++m_resets;
            m_count = m_names.size() - 1;
            m_entries.clear();
            m_entries.resize( m_names.size(), true );
            wasReset = true;
            //std::cout << "reseting" << std::endl;
         }
      }
      m_entries[ pos ] = false;
      return wasReset;
   }

private:
   size_t    m_count;
   size_t    m_resets;
   Entries   m_entries;
   Names     m_names;
};

int main()
{
   typedef std::vector<std::string> SearchEngines;

   size_t testCasesCount;
   std::cin >> testCasesCount;

   for( size_t tcNo = 0; tcNo < testCasesCount; ++tcNo )
   {
      // Fill engines
      size_t enginesCount;
      std::cin >> enginesCount;

      Set::Names names;

      {
         size_t engNo = 0;
         while( engNo < enginesCount )
         {
            std::string engine;
            std::getline( std::cin, engine );
            if( !engine.empty() )
            {
               //std::cout << "'" << engine << "'" << std::endl;
               names.push_back( engine );
               ++engNo;
            }
         }
      }

      Set engines( names );

      // Process queries
      size_t queriesCount;
      std::cin >> queriesCount;

      size_t qNo = 0;
      while( qNo < queriesCount )
      {
         std::string query;
         std::getline( std::cin, query );

         if( !query.empty() )
         {
            //std::cout << "Processing query: " << query << std::endl;

            bool result = engines.remove( query );
            engines.remove( query );
            //std::cout << "Removing " << query << " " << result << std::endl;

            ++qNo;
         }
      }

      std::cout << "Case #" << tcNo+1 << ": " << engines.resets() << std::endl;
   }
	return 0;
}

