using namespace std;

#include <iostream>
#include <string>
#include <map>
#include <list>
#include <iostream>
#include <set>


int solvecase( int curcase )
{
    int nExistingDirs, nDirsToCreate, ii, jj, kk; 

    std::set< string > existing; 
    std::set< string > tocreate; 

    std::cin >> nExistingDirs;
    std::cin >> nDirsToCreate; 

    string existingDir;
    string newDir; 

    for( ii = 0; ii < nExistingDirs; ++ii ){
        std::cin >> existingDir; 
        existing.insert( existingDir ); 
    }

    for( ii =0; ii < nDirsToCreate; ++ii ){
        std::cin >> newDir; 
        tocreate.insert( newDir ); 
    }

    std::set<string>::iterator exist_it, create_it; 
    
    int mkDirsNeeded = 0;
    int lastBar = 0; 
    create_it = tocreate.begin(); 
    while( create_it != tocreate.end() ){
         newDir = *create_it; 
         while( newDir != "/" && 
                newDir != "" && 
                existing.find( newDir ) == existing.end() )
         {
            ++mkDirsNeeded;
            lastBar = newDir.find_last_of( "/" );
            existing.insert( newDir ); 
            newDir = newDir.substr( 0, lastBar );  
         }
         
         create_it++;
         // TODO remove the newDir from tocreate 

    }

    std::cout << "Case #" << (curcase +1) << ": " << mkDirsNeeded << std::endl;  
}


int main( int argc, char* argv[] )
{

    int ncases, curcase;

    std::cin >> ncases; 

    for( curcase = 0; curcase < ncases; ++curcase ){
        solvecase( curcase ); 
    }

    return 0;
}
