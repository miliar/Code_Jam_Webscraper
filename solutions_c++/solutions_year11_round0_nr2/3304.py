//
//  magicka.cpp
//  code_jam
//
//  Created by Paul O'Neil on 5/7/11.
//  Copyright 2011 Paul O'Neil. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
using namespace std;

#define min(a, b) ( (a) < (b) ? (a) : (b) )


struct element_pair {
  char elements[2];
  
  explicit element_pair(char first, char second) throw() {
    if( first <= second ) {
      elements[0] = first;
      elements[1] = second;
    }
    else {
      elements[0] = second;
      elements[1] = first;
    }
  }
  
  explicit element_pair(string str) throw() {
    *this = element_pair(str[0], str[1]);
  }

  bool operator==(const element_pair& other) const throw() {
    return elements[0] == other.elements[0] && elements[1] == other.elements[1];
  }
  
  bool operator<(const element_pair& other) const throw() {
    if( elements[0] == other.elements[0] ) {
      return elements[1] < other.elements[1];
    }
    else {
      return elements[0] < other.elements[0];
    }
  }
  
  bool contains(char ch) const throw() {
    return elements[0] == ch || elements[1] == ch;
  }
};

ostream & operator<<(ostream& output, const element_pair& pair) {
  return output << pair.elements[0] << ", " << pair.elements[1];
}

class list_t : public string {
public:
  
  bool contains_pair(const element_pair pair) const throw() {    
    return find(pair.elements[0]) != npos && find(pair.elements[1]) != npos;
  }
  
  element_pair last_pair() const throw() {
    if( size() < 2 ) {
      return element_pair(0, 0);
    }
    return element_pair(at(size()-1), at(size()-2));
  }
};

ostream & operator<<(ostream& output, const list_t& list) {
  output << "[";
  int i;
  for( i = 0; list.size() && i < list.size() - 1; i++ ) {
    output << list[i] << ", ";
  }
  if( i < list.size() ) {
    output << list[i];
  }
  output << "]";
  return output;
}

class composite : public pair<element_pair, char> {
public:
  explicit composite(string threeString) :
    pair<element_pair, char>(element_pair(threeString[0], threeString[1]), threeString[2])
  { }
  
  bool operator<(const composite & other) const throw() {
    if( first == other.first ) {
      return second < other.second;
    }
    return first < other.first;
  }
};

typedef map<element_pair, char> combo_map_t;
typedef combo_map_t::const_iterator combo_iter_t;

typedef set<element_pair> enemy_set_t;
typedef enemy_set_t::const_iterator enemy_iter_t;

list_t do_trial(istream & input) throw() {
  combo_map_t combos;
  enemy_set_t enemies;
  
  string astring;
  
  int combo_count = 0;
  input >> combo_count;
  for( int i = 0; i < combo_count; i++ ) {
    input >> astring;
    combos.insert(composite(astring));
  }
  
  int enemy_count = 0;
  input >> enemy_count;
  for( int i = 0; i < enemy_count; i++ ) {
    input >> astring;
    enemies.insert(element_pair(astring));
  }
  enemy_iter_t enemy_end = enemies.end();
  
  int list_len = 0;
  input >> list_len;
  input >> astring;
  list_t list;
  for( int i = 0; i < astring.size() && i < list_len; i++ ) {
    list += astring[i];
    
    // check for combos
    element_pair last_pair = list.last_pair();
    if( combos.count(last_pair) ) {
      list.erase(list.size()-2);
      list += combos[last_pair];
    }
    
    // check for enemies, and obliterate the list
    char last = list[list.size() - 1];
    for( enemy_iter_t iter = enemies.begin(); iter != enemy_end; iter++ ) {
      if( iter->contains(last) ) {
        if( list.contains_pair(*iter) ) {
          list.erase();
          break;
        }
      }
    }
  }
  
  return list;
}

int main (int argc, const char * argv[])
{
  int trialCount;
  istream * in;
  if( argc == 1 ) {
    in = &cin;
  }
  else {
    in = new ifstream(argv[1]);
  }
  istream & input = *in;
  input >> trialCount;
  
  for( int i = 1; i <= trialCount; i ++ ) {
    list_t result = do_trial(input);
    cout << "Case #" << i << ": " << result << endl;
  }
  
  if( argc > 1 ) {
    delete in;
  }
  return 0;
}
