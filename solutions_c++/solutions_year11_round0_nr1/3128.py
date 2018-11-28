#include <numeric>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;
struct Button
{
char color;
int pos;
Button(char c, int p):color(c), pos(p){}
Button(){}
Button(const Button& b){color = b.color;pos = b.pos;}
};
struct Robot
{
	static int lastAction;
	int time;
	int pos;
	Robot (): time(0), pos(1){}
	void pushButton(int newPos)
	{
    //move
    time += abs(newPos -pos);
    pos = newPos;
	  //push
    if (time>lastAction) 
	  {
		time += 1;
	  }
	  else 
	  {
		time =lastAction + 1;
	  }
	  lastAction = time;  
	}
};
int Robot::lastAction = 0;
int Robots(const vector<Button>& v)
{
  Robot::lastAction = 0;
  Robot orange;
  Robot blue;
  int time;
  for(auto it = v.begin();it !=v.end();it++)
  {
    if(it->color == 'O')
    {
      orange.pushButton(it->pos);
    }
    else
    {
      blue.pushButton(it->pos);
    }
  }
  return Robot::lastAction;
}

int main(int argc, char** argv)
{
  if (argc!=2) return -1;
  ifstream f(argv[1]);
  int lines;
  f >> lines;
  //cout << lines << endl;
  for(int i=0;i<lines;i++)
  {
    int buttons;
    f >> buttons;
    vector<Button> v;
    v.reserve(buttons);
    for (int j=0;j<buttons;j++)
    {
      char c;
      int pos;

      f >> c >> pos;
      
      v.push_back(Button(c, pos));
    }
    
    //for_each(v.begin(), v.end(), [](Button b){ cout << b.color << " " << b.pos;});
    //cout << endl;
    int time = Robots(v);
    cout <<"Case #"<< i + 1 <<": "<< time << endl;
  }
}