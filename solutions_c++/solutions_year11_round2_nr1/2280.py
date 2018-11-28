#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

class Team
{
private:
  static vector<Team*> *allTeams;
  char *otherTeams;
  double WP, OWP, OOWP;
  int teamPlayed;
public:
  Team();
  ~Team();
  double getRPI();
  
  double getWP();
  double getOWP();
  double getOOWP();
  
  int getTeamsPlayed();
  
  friend istream &operator>>(istream &in, Team *t);
  
  static void clearTeams();
};

istream &operator>>(istream &in, Team *t);

int main()
{
  int T;
  cin >> T;
  for(int c=0; c < T; c++) {
    int N;
    cin >> N;
    vector<Team*> allTeams;
    for(int i=0; i < N; i++) {
      allTeams.push_back(new Team());
    }
    //cout << "OK" << endl;
    for(int i=0; i < N; i++) {
      cin >> allTeams[i];
      //cout << "Done with " << i+1 << endl;
    }
    printf("Case #%d:\n", c+1);
    for(vector<Team*>::iterator i = allTeams.begin();
	i != allTeams.end(); i++) {
      cout << (*i)->getRPI() << endl;
    }
    Team::clearTeams();
  }
  return 0;
}

vector<Team*> *Team::allTeams = new vector<Team*>();

Team::Team()
{
  this->allTeams->push_back(this);
  this->otherTeams = NULL;
  
  WP=-1; OWP=-1; OOWP=-1;
}

Team::~Team()
{
  for(vector<Team*>::iterator i = this->allTeams->begin(); 
      i != allTeams->end(); i++) {
    if(*i == this) {
      allTeams->erase(i);
      break;
    }
  }
  delete this->otherTeams;
}

double Team::getRPI()
{
  //printf("WP: %f\tOWP: %f\tOOWP: %f\n", 
  //	 this->getWP(), this->getOWP(), this->getOOWP());
  return this->getWP() * .25 + this->getOWP() *.5 + this->getOOWP() *.25;
}

double Team::getWP()
{
  return WP;
}
double Team::getOWP()
{
  if(this->OWP >= 0)
    return this->OWP;
  int j=0, totalOtherTeams=0;
  double totalOtherTeamsWP = 0;
  for(vector<Team*>::iterator i = this->allTeams->begin(); 
      i != allTeams->end(); i++) {
    if(this->otherTeams[j] != '.' && this != *i) {
      totalOtherTeams++;
      double t = (*i)->getWP();
      t *= (*i)->getTeamsPlayed();
      if(otherTeams[j] == '0')
	t--;
      t = t / ((*i)->getTeamsPlayed()-1);
      totalOtherTeamsWP += t;
    }
    j++;
  }
  this->OWP = totalOtherTeamsWP / totalOtherTeams;
  return this->getOWP();
}
double Team::getOOWP()
{
  if(this->OOWP >= 0)
    return this->OOWP;
  int j=0, totalOtherTeams=0;
  double totalOtherTeamsWP = 0;
  for(vector<Team*>::iterator i = this->allTeams->begin(); 
      i != allTeams->end(); i++) {
    if(this->otherTeams[j] != '.') {
      totalOtherTeams++;
      totalOtherTeamsWP += (*i)->getOWP();
    }
    j++;
  }
  this->OOWP = totalOtherTeamsWP / totalOtherTeams;
  return this->getOOWP();
}

int Team::getTeamsPlayed()
{
  return this->teamPlayed;
}

istream &operator>>(istream &in, Team *t)
{
  int totalWins=0, totalTeams = 0;
  if(t->otherTeams != NULL)
    delete t->otherTeams;
  t->otherTeams = new char[t->allTeams->size()];
  for(int i=0; i < t->allTeams->size(); i++) {
    char c;
    //cout << "Taking in char " << i+1 << endl;
    in >> c;
    t->otherTeams[i]= c;
    if(c != '.')
      totalTeams++;
    if(c == '1')
      totalWins++;
  }
  t->WP = (double)totalWins / totalTeams;
  t->teamPlayed = totalTeams;
  return in;
}

void Team::clearTeams()
{
  while(Team::allTeams->size() > 1) {
    //delete Team::allTeams->back();
    //cout << "OK" << endl;
    Team::allTeams->pop_back();
  }
  Team::allTeams->pop_back();
}