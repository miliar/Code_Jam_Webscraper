#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <map>
#include <set>

int size(int n)
{
  int ret = 0;
  do { n/=10; ret++; } while(n>0);
  return ret;
}

const char* read_number( const char *p, int &n )
{
  if(!*p)
    return NULL;

  n = atoi(p);
  p += size(n)+1;

  if(!*p)
    return NULL;
  return p;
}

class Magicka
{
public:
  Magicka( const std::set<int> & pfizzle_combos,
	const std::map<int, char> &pmutate_combos )
	: fizzle_combos(pfizzle_combos),
	  mutate_combos(pmutate_combos) {};

  void add_element( char el );

  void print_contents();

private:
  // returns combo to push back, or original
  char try_eol_combo( char el );

  std::vector<char> elements;
  std::map<char, int> elements_present;
  std::set<int> fizzle_combos;
  std::map<int, char> mutate_combos;
};

void Magicka :: print_contents()
{
	printf( "[" );
	int i;
	if( !elements.empty() )
	{
		for( i=0; i<elements.size()-1; i++ )
			printf( "%c, ", elements[i] );

			printf("%c", elements[i] );
	}
	printf("]");
}

void Magicka :: add_element( char el )
{
	char el2 = try_eol_combo( el );

	if( el2 != el ) // eol combo
	{
		elements_present[el2]++;
		elements.push_back( el2 );
		return;
	}

	// for all elements present, try to annihilate list 
	// if element already exists, do not try
	if(1) // elements_present.find(el) == elements_present.end() )
	{
		bool fizzled = false;
		std::map<char, int>::const_iterator i;
		for( i=elements_present.begin(); i != elements_present.end(); i++ )
		{
			if( (*i).second <1 )
				continue;

			// TODO: get fizzle combo
			int combo1 = (*i).first + (el<<8);
			int combo2 = ((*i).first<<8) + el;
			if( fizzle_combos.find(combo1) != fizzle_combos.end() )
				fizzled = true;
			if( fizzle_combos.find(combo2) != fizzle_combos.end() )
				fizzled = true;

			if( fizzled )
				break;
		}

		if( fizzled )
		{
			elements.clear();
			elements_present.clear();
			return;
		}
	}

	elements_present[el]++;
	elements.push_back( el );
}

char Magicka :: try_eol_combo( char el )
{
	// try end of line combo
	if( elements.empty() )
	{
		return el;
	}

	int back_el = elements.back();
	int combo1 = el + (back_el<<8);
	int combo2 = (el<<8) + back_el;
	if( mutate_combos.find(combo1) != mutate_combos.end() )
	{
		elements_present[back_el]--;
		elements.erase( elements.end()-1 );
		return mutate_combos[combo1];
	}
	else if( mutate_combos.find(combo2) != mutate_combos.end() )
	{
		elements_present[back_el]--;
		elements.erase( elements.end()-1 );
		return mutate_combos[combo2];
	}

	// no eol combo
	return el;
}

void solve( const char *string )
{
  std::set<int> fizzle_combos;
  std::map<int, char> mutate_combos;
  
  int n_mutate = 0;
  int n_fizzle = 0;

  const char *p = read_number(string, n_mutate);
  for( int i=0; i<n_mutate; i++ )
  {
     char first, second, result;
     first = *p++;
     second = *p++;
     result = *p++;
     p++;
     mutate_combos.insert( std::pair<int,char>( (first<<8)+second, result ) ); 
     mutate_combos.insert( std::pair<int,char>( (second<<8)+first, result ) ); 
  }

  p = read_number(p, n_fizzle);
  for( int i=0; i<n_fizzle; i++ )
  {
     char first, second;
     first = *p++;
     second = *p++;
     p++;
     fizzle_combos.insert( (first<<8)+second );
     fizzle_combos.insert( (second<<8)+first );
  }


  Magicka m( fizzle_combos, mutate_combos );

  int n_elements =0;
  p = read_number(p, n_elements);
  for( int i=0; i<n_elements; i++ )
  {
	m.add_element( *p++ );
  }

  m.print_contents();
}

int main(void)
{
  char buf[2048];
  fgets(buf, 2048, stdin);
  int count;
  read_number(buf, count);
  for( int i=0; i<count; i++ )
  {
    fgets(buf, 2048, stdin);
    printf( "Case #%d: ", i+1 );
    solve(buf);
    printf( "\n" );
  }

  return 1;
}
