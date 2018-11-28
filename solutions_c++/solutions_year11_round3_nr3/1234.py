//
//  code_jam
//
//  Created by Paul O'Neil on 5/20/11.
//  Copyright 2011 Paul O'Neil. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

unsigned long long gcd(unsigned long long a, unsigned long long b) {
  if( b == 0) {
    return a;
  }
  return gcd(b, a % b);
}

unsigned long long lcm( unsigned long long a, unsigned long long b) {
  return a * b / gcd(a, b);
}

void do_trial(istream & input) throw() {
  unsigned long long player_count, low_bound, high_bound;
  input >> player_count >> low_bound >> high_bound;
  
  vector<unsigned long long> other_freqs;
  other_freqs.reserve(player_count);
  for( unsigned long long i = 0; i < player_count; i++ ) {
    unsigned long long j;
    input >> j;
    other_freqs.push_back(j);
  }
  
  sort(other_freqs.begin(), other_freqs.end());
  
  // I must be a multiple of the lcm of all freqencies lower than me
  // and a factor of the gcd of all freqencies higher than me
  for( unsigned long long my_position = 0; my_position <= player_count; my_position++ ) {
    // compute lcm of all freqs lower than me
    unsigned long long the_lcm = 1;
    for( unsigned long long other = 0; other < my_position; other++ ) {
      the_lcm = lcm(the_lcm, other_freqs[other]);
    }
    // compute the gcd of all freqs higher than me
    if( my_position < other_freqs.size() ) {
      unsigned long long the_gcd = other_freqs.back();
      for( unsigned long long other = my_position; other < player_count; other++ ) {
        the_gcd = gcd(the_gcd, other_freqs[other]);
      }
      if( the_lcm > the_gcd ) {
        continue;
      }
      if( the_gcd % the_lcm == 0 ) {
        // since I must be a multiple of the lcm,
        // and a divisor of the gcd, then,
        // (a * lcm) * b = gcd, so lcm | gcd
        
        // make sure that I can play this...
        if( the_lcm <= high_bound && the_gcd >= low_bound ) {
          unsigned long long my_freq = the_lcm;
          while( my_freq < low_bound ) {
            my_freq += the_lcm;
          }
          while( my_freq <= high_bound ) {
            if( the_gcd % my_freq == 0 ) {
              cout << my_freq << endl;
              return;
            }
            my_freq += the_lcm;
          }
        }
      }
    }
    else {
      if( the_lcm <= high_bound ) {
        unsigned long long my_freq = the_lcm;
        while( my_freq < low_bound ) {
          my_freq += the_lcm;
        }
        cout << my_freq << endl;
        return;
      }
    }
  }
  
  cout << "NO\n";
}

int main (int argc, const char * argv[])
{
  unsigned long long trialCount;
  istream * in;
  if( argc == 1 ) {
    in = &cin;
  }
  else {
    in = new ifstream(argv[1]);
  }
  istream & input = *in;
  input >> trialCount;
  
  for( unsigned long long i = 1; i <= trialCount; i ++ ) {
    cout << "Case #" << i << ": ";
    do_trial(input);
  }
  
  if( argc > 1 ) {
    delete in;
  }
  return 0;
}
