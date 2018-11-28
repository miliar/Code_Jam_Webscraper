#include <stdio.h>
#include <stdlib.h>

#include <set>
#include <vector>

#define ABS(x) ((x)>=0?(x):-(x))

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

class team;

team *teams;
double owps[100];

class team
{
public:
	void add_win( int opponent ) { wins.insert( opponent ); opponents.insert( opponent );  };
	void add_loss( int opponent ) { opponents.insert( opponent ); };

	double get_wp() const { return wins.size()/(double)opponents.size(); };

	double get_owp(int opponent) const { 
		int wincnt = wins.size();
		int opcnt = opponents.size();
		std::set<int>::iterator f = wins.find(opponent); 
		if( f !=wins.end() )wincnt--; 
		f = opponents.find(opponent); 
		if( f!= opponents.end() )opcnt--;
		return wincnt/(double)opcnt;
	};

	const std::set<int>& get_opponents() const { return opponents; };

private:
	std::set<int> wins;
	std::set<int> opponents;
};

double get_owp( int team )
{
	if( owps[team] >-1 )
	{
		//printf( "o!\n" );
		return owps[team];
	}

	const std::set<int>& opponents = teams[team].get_opponents();
	std::set<int>::const_iterator i;
	double sum = 0;
	for( i=opponents.begin(); i!=opponents.end(); i++ )
	{
		double owp = teams[*i].get_owp(team);		
		//printf( "Team %d: owp of team %d is %f\n", team, *i, owp );
		sum += owp;
	}

	double ret = sum / opponents.size();
	owps[team] = ret;
	return ret;
}

double get_oowp( int team )
{
	const std::set<int>& opponents = teams[team].get_opponents();
	std::set<int>::const_iterator i;
	double sum = 0;
	
	for( i=opponents.begin(); i!=opponents.end(); i++ )
		sum += get_owp(*i);

	return sum / opponents.size();
}

double get_score( int team )
{
	double wp = teams[team].get_wp();
	double owp = get_owp(team);
	double oowp = get_oowp(team);

	//printf( "team %d: wp=%f, owp=%f, oowp=%f\n", team, wp, owp, oowp );
	return 0.25*teams[team].get_wp() + 0.5*get_owp(team) + 0.25*get_oowp(team);
}

void solve( int nteams, FILE *f )
{
  int n = 0;
  char buf[2048];

  teams = new team[nteams];

  for( int i=0; i<nteams; i++ )
	owps[i]=-1;

  for( int i=0; i<nteams; i++ )
  {
    fgets(buf, 2048, f);
    for( int j=0; j<nteams; j++)
    {
      switch(buf[j])
      {
        case '.': break;
	case '0': teams[i].add_loss(j); break;
	case '1': teams[i].add_win(j); break;
      }
    }
  }

  for( int i=0; i<nteams; i++ )
 	printf( "%.12g\n", get_score(i) );

  delete[] teams;
}

int main(void)
{
  char buf[2048];
  fgets(buf, 2048, stdin);
  int count;
  read_number(buf, count);
  int nteams;
  for( int i=0; i<count; i++ )
  {
    fgets(buf, 2048, stdin);
    read_number(buf, nteams);
    printf( "Case #%d:\n", i+1 );
    solve(nteams, stdin);
  }

  return 1;
}
