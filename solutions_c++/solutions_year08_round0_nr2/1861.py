#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

#define FOR( i, n ) for( int (i) = 0; (i) < (n); ++(i) ) 
#define FORR( i, n, m ) for(int (i) = (n); (i) <= (m); ++(i) ) 
#define FOREACH(_it,_l) for(__typeof((_l).begin()) _it=((_l).begin());(_it)!=(_l).end();(_it)++) 
#define ALL(x) (x).begin(),(x).end() 
#define eatDel( ifs, del ) while( ifs.peek() == del ) ifs.ignore(); 
#define isMaped( m, element ) ((m).find( (element) ) != (m).end()) 

#define max( a, b ) (a)<(b)?(b):(a)
#define min( a, b ) (a)<(b)?(a):(b)

using namespace std;


vector<string> expand( const string & input, char delimiter )
{
     vector<string> out;
     int begin = 0;
     int i;
     for( i = 0; i < input.length( ); i++ )
     {
          if( i > 0 && input[i] == delimiter && input[i-1] != delimiter ) 
          { 
              out.push_back( input.substr( begin, i - begin ) ); 
              begin = i+1 ;
          }
          else
          {
              if( input[i] == delimiter ){ begin = i+1; }
          }
     }
     if( begin < i )
     {
         out.push_back( input.substr( begin ) );
     }
     return out;
}

struct Time
{
       int hours;
       int min;
       bool operator < ( const Time & b ) const 
       {
            if( hours == b.hours ) return min < b.min;
            else return hours < b.hours;            
       }
       
       
       bool operator == ( const Time & b ) const
       {
            return hours == b.hours && min == b.min;
        }
        
        bool operator > ( const Time & b ) const
        {
             return !( *this == b ) && !( *this < b );
         }
         
         bool operator <= ( Time & b ) const
         {
              return *this < b || *this == b;
          }
       
       void operator += ( int m )
       {
            if( min + m > 59 )
            {
                hours++;
                min = min + m - 60;
            }
            else min += m;
           
        }
        
        void print( )const { cout<<hours<<":"<<min; }
       
};

struct Trip
{
       pair< Time, Time > trip_t;
       bool operator < ( const Trip & b ) const
       {
            return trip_t.first < b.trip_t.first;
        }
        
        void operator = ( const Trip & t )
        {
             trip_t = t.trip_t;
         }
        
        void parse( const string & a )
        {
             vector<string> v = expand( a, ' ' );
             vector< string > s = expand( v[0], ':' );
             vector< string > f = expand( v[1], ':' );
             
             trip_t.first.hours = atoi( s[0].c_str() );
             trip_t.first.min = atoi( s[1].c_str() );
             
             trip_t.second.hours = atoi( f[0].c_str() );
             trip_t.second.min = atoi( f[1].c_str() );
             
         }
         
         void print() const
         {
              trip_t.first.print();
              cout<<" ";
              trip_t.second.print();
              cout<<endl;
          }
};

pair<int,int> solve( vector<Trip> & NAT, vector<Trip> & NBT, int turn_around_time )
{
            pair<int,int> ret;
            ret.first = ret.second = 0;
            if( NAT.size() == 0 )
            {
                ret.second = NBT.size();
                return ret;
            }
            if( NBT.size() == 0 )
            {
                ret.first = NAT.size();
                return ret;
            }
            
            
            while( NAT.size() != 0 && NBT.size() != 0 )
            {
                   Time av_time;
                   vector<Trip> *station;
                   bool working_a = true;
                   if( NAT[0] < NBT[0] )
                   {
                       ret.first++;
                       av_time = NAT[0].trip_t.second;
                       station = & NBT;
                       NAT.erase( NAT.begin() );
                   }
                   else
                   {
                       ret.second++;
                       av_time = NBT[0].trip_t.second;
                       station = & NAT;
                       NBT.erase( NBT.begin() );
                       working_a = false;
                   }
                   // track train
                   bool track_train = true;
                   Time tracking_time = av_time;
               
                   tracking_time += turn_around_time;
                   
                   tracking_time.print();
                   cout<<endl;
                   while( track_train )
                   {
                          Time prev_t_time = tracking_time;
                          FOREACH( el, *station )
                          {
                                   if( tracking_time <= el->trip_t.first )
                                   {
                                       
                                       tracking_time = el->trip_t.second;
                                       tracking_time += turn_around_time;
                                       station->erase( el );
                                       if( station == &NAT ) station = &NBT;
                                       else station = &NAT;
                                       break;
                                   }
                          }
                          if( tracking_time == prev_t_time ) track_train = false;
                   }
                   
            }
            if( NAT.size() != 0 ) ret.first += NAT.size();
            if( NBT.size() != 0 ) ret.second += NBT.size();
            return ret;
              
              
}

int main()
{
    ifstream ifs( "B-large.in" );
    ofstream ofs( "b.out" );
    
    int num_cases;
    ifs>>num_cases;
    
    for( int case_num = 1; case_num <= num_cases; ++ case_num )
    {
         int turn_around_time;
         ifs>>turn_around_time;
         
         vector<Trip> NAT, NBT;
         
         int NA, NB;
         ifs>>NA>>NB;
         for( int i = 0; i < NA; ++i )
         {
              eatDel( ifs, '\n' );
              string trip;
              getline( ifs, trip );
              Trip NA_trip;
              NA_trip.parse( trip );
              //NA_trip.print();
              NAT.push_back( NA_trip );
              
          }
          for( int i = 0; i < NB; ++i )
         {
              eatDel( ifs, '\n' );
              string trip;
              getline( ifs, trip );
              Trip NB_trip;
              NB_trip.parse( trip );
              //NB_trip.print();
              NBT.push_back( NB_trip );
              
          }
          sort( ALL( NBT ) );
          sort( ALL( NAT) );
          /*
          cout<<"===================="<<endl;
          FOREACH( el, NAT ) el->print();
          cout<<"==="<<endl;
          FOREACH( el, NBT ) el->print();
          */
          pair<int,int> solution = solve( NAT, NBT, turn_around_time );
          ofs<<"Case #"<<case_num<<": "<<solution.first<<" "<<solution.second<<endl;
         
         
    }
    
    cout<<"DONE"<<endl;
    
    ifs.close();
    ofs.close();
    
    system( "pause" );
    
}
