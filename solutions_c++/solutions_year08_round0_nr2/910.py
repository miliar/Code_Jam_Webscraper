#include <iostream>
#include <fstream>
#include <algorithm>

#define LINE 128

using namespace std;

int sa[LINE];
int ra[LINE];
int sb[LINE];
int rb[LINE];

inline int convert2min(char* str)
{
  str[2] = '\0';
  int hour = atoi(str);
  int min = atoi(str+3);
  
  return hour * 60 + min;
}

int main(int argc, char* argv[])
{
  ifstream ifs("B-small.in");
  ofstream ofs("B-small.out");
  
  char line[LINE];
  memset(line, 0, sizeof(line));
  ifs.getline(line, LINE);
  int numCases = atoi(line);
  
  for(int i = 0; i < numCases; ++ i){
    memset(line, 0, sizeof(line));
    ifs.getline(line, LINE);
    int turn = atoi(line);
    
    int na;
    int nb;
    ifs>>na>>nb;
    ifs.getline(line, LINE);

    char temp[16];
    for(int j = 0; j < na; ++ j){
      ifs>>temp;
      sa[j] = convert2min(temp);
      ifs>>temp;
      ra[j] = convert2min(temp);
      ifs.getline(line, LINE);
      cout<<sa[j]<<" "<<ra[j]<<endl;
    }

    for(int j = 0; j < nb; ++ j){
      ifs>>temp;
      sb[j] = convert2min(temp);
      ifs>>temp;
      rb[j] = convert2min(temp);
      ifs.getline(line, LINE);
      cout<<sb[j]<<" "<<rb[j]<<endl;
    }

    sort(sb, sb+nb, less<int>());
    sort(sa, sa+na, less<int>());

    int ssa = 0;
    for(int j = 0; j < na; ++ j){
      for(int k = 0; k < nb; ++ k){
	if(sa[j] >= rb[k] + turn){
	  rb[k] = 24*60;
	  -- ssa;
	  break;
	}
      }
      ++ ssa;
    }
    
    int ssb = 0;
    for(int j = 0; j < nb; ++ j){
      for(int k = 0; k < na; ++ k){
	if(sb[j] >= ra[k] + turn){
	  ra[k] = 24*60;
	  -- ssb;
	  break;
	}
      }
      
      ++ ssb;
    }
    
    cout<<"Case #"<<i+1<<": "<<ssa<<" "<<ssb<<endl;
    ofs<<"Case #"<<i+1<<": "<<ssa<<" "<<ssb<<endl;    
  }
  
  return 0;
}
