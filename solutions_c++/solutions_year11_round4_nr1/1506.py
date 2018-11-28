#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main()
{
   int T;
   cin >> T;
   for(int i = 0; i < T; i++)
   {
      map< pair< int, int >, int > segmentsToSpeeds;
      int X, S, R, N;
      float t;
      cin >> X >> S >> R >> t >> N;
      for(int j = 0; j < N; j++)
      {
         int B, E, W;
         cin >> B >> E >> W;
         segmentsToSpeeds.insert( make_pair( make_pair( B, E ), W ) );
      }

      double results = 0;
      int distance = 0;
      map< pair< int, int>, int >::iterator itr;
      itr = segmentsToSpeeds.begin();
      while(distance < X)//tiem without running
      {
         int distanceNext = 0;
         if( itr == segmentsToSpeeds.end() )
         {
            distanceNext = X - distance;
            results += distanceNext / (double) S;
            distance = X;
         }
         else
         {
            distanceNext = itr->first.first - distance;
            results += distanceNext / (double) S;
            results += (itr->first.second - itr->first.first) / (double) (S + itr->second);
            distance += distanceNext + (itr->first.second - itr->first.first);
            ++itr;
         }
      }
     // std::cout << "Distance traveled: " << distance << std::endl;   

      multimap< double, pair<double,double> > benefitToLength;
      int start = 0;
      for( itr = segmentsToSpeeds.begin(); itr != segmentsToSpeeds.end(); itr++)
      {
         benefitToLength.insert(make_pair(R / (double) S, make_pair((R - S) / (double) S, (itr->first.first - start) / (double) R)));
         benefitToLength.insert(make_pair(((double) R + itr->second) / ((double) S + itr->second), make_pair((((double) R + itr->second) - ((double) S + itr->second)) / (((double) S + itr->second)),(itr->first.second - itr->first.first) / ((double)R + itr->second))));
         start = itr->first.second;
      }
      benefitToLength.insert(make_pair(R / (double) S, make_pair((R - S) / (double) S, (distance - start) / (double) R)));

     // std::cout << "Time without running: " << results << std::endl;

      for(multimap< double, pair<double, double> >::reverse_iterator ritr = benefitToLength.rbegin(); ritr != benefitToLength.rend(); ritr++)
      {
       //  std::cout << ritr->first << " " << ritr->second.first << " " << ritr->second.second << std::endl;
      }
     //std::cout << std::endl;

      for(multimap< double, pair<double, double> >::reverse_iterator ritr = benefitToLength.rbegin(); ritr != benefitToLength.rend(); ritr++)
      {
         // std::cout << ritr->first << " " << ritr->second.first << " " << ritr->second.second << std::endl;
         if( t >= ritr->second.second )
         {
       //     std::cout << "full" << std::endl;
            //std::cout << ritr->first << " " << ritr->second.first << " " << ritr->second.second << std::endl;
            results -= ritr->second.first * ritr->second.second;
            t -= ritr->second.second;
         }
         else
         {
         //   std::cout << "half" << std::endl;
            //std::cout << ritr->second.first << " " << t << " " << ritr->second.second << std::endl;
            results -= ritr->second.first * t;
            break;
         }
      }
      cout.precision(10);
      std::cout << "Case #" << i+1 << ": " << results << std::endl;;
   }
}