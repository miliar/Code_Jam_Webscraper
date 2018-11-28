#include <iostream>
#include <fstream>

using namespace std;

class GrpNode
{
  public:
  int size;
  GrpNode *next;
};

int main()
{
  ifstream ifs;
  ifs.open("C-small-attempt0.in", ifstream::in);

  ofstream ofs;
  ofs.open("output.txt", ofstream::out);

  int nCases = 0;
  ifs>>nCases;

  for(int i=0; i < nCases; i++)
  {
    int trips = 0;
    int capacity = 0;
    int grps = 0;

    ifs>>trips>>capacity>>grps;

    GrpNode *head = NULL;
    GrpNode *prev = NULL;


    for(int j = 0; j < grps ; j++)
    {
      int size = 0;
      ifs>>size;

      GrpNode *newNode = new GrpNode;
      newNode->size = size;

      if(prev)
      {
	prev->next = newNode;
      }

      if(j == 0)
      {
	head = newNode;
      }

      if(j == grps-1)
      {
	newNode->next = head;
      }
      prev = newNode;
    }

    int money = 0;
    GrpNode *pos = head;

    for(int j = 0; j < trips ; j++ )
    {
      int currHops = 0;
      int currPpl = 0;

      while(currPpl + pos->size <= capacity && currHops < grps)
      {
	currPpl += pos->size;

	pos = pos->next;

	currHops++;
      }
       money += currPpl;
    }

    // Print out the output
    ofs<<"Case #"<<(i+1)<<": "<<money <<endl;
  }


  ofs.close();
  ifs.close();
  return 0;

}
