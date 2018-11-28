// Hybryd-

#define FOR(I,A,B)        for(int (I)=(A); (I)<(B); ++(I) )
#define MINI(X,Y)         ( (X) < (Y) ? (X) : (Y) )
#define MAXI(X,Y)         ( (X) > (Y) ? (X) : (Y) )
#define COUT(X)           std::cout << (X) << std::endl;
#define PROGRESS(I,N)     fprintf(stderr,"%lf%%\r",(double)( (I) *100)/(N));

#define MAXINT std::numeric_limits<int>::max()

#include <algorithm>
#include <iostream>
#include <fstream>
#include <limits>
#include <vector>
#include <sstream>


using namespace std;


int main(int argc, char ** argv)
{
  if(argc > 1)
  {
    std::fstream inFile(argv[1],std::ios::in);
    if(inFile)
    {
      int t=1;
      std::string line;
      std::stringstream sline;
      int nbData;
      std::string word;
      inFile >> nbData;
      getline(inFile,line);

      std::vector<std::string> P;


      while(getline(inFile,line))
      {
        sline.clear();
        sline.str("");
        sline << line;
        
        int N;
        char robot;
        int b;
        int posO=1;
        int posB=1;

        std::vector<int> dispo;
        dispo.push_back(0);
        dispo.push_back(0);
        int deb=0;
        
        sline >> N;
        
        std::vector<std::pair<int,int> > sched;
        while(!sline.eof())
        {
          sline >> robot;
          sline >> b;
          
          std::pair<int,int> p;
          if(robot == 'O')
          {
            p.first = 0;
            p.second = abs(b-posO) + 1;
            posO = b;
          }
          else
          {
            p.first = 1;
            p.second = abs(b-posB) + 1;
            posB = b;
          }
          
          sched.push_back(p);
        }
        
        FOR(i,0,sched.size())
        {
//          std::cout << "robot : " << sched[i].first << ". Dispo : " << dispo[sched[i].first] << "  Deb : " << deb << "  Duree action : " << sched[i].second << std::endl;
          
          deb = MAXI(deb+1,dispo[sched[i].first]+sched[i].second);
          dispo[sched[i].first] = deb;
        }


        // Output
        std::cout << "Case #" << t << ": " << deb << std::endl ;
        ++t;
      }
      inFile.close();
    }
    else
      std::cerr << "Error, output file does not exist." << std::endl;
  }
  else
    std::cerr << "Error, please specify an output file." << std::endl;
  return 0;
}
