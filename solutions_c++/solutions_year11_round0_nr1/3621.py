// SAI [ 8 May 2010 ]

#include <string>
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <cmath>

typedef struct
{
  int val;
}Btn;

typedef std::vector<Btn*>           BtnList;
typedef std::vector<Btn*>::iterator BtnListIterator;
typedef BtnList         TurnList;
typedef BtnListIterator TurnListIterator;

typedef struct
{
  int      btnRequired;
  TurnList turnList;
  BtnList  oList; 
  BtnList  bList;
}Input;

typedef std::vector<Input*>           InputList;
typedef std::vector<Input*>::iterator InputListIterator;

int  Jamstart(InputList& list);
void ReadData(InputList& list, std::string fileName);

typedef enum
{
  RS_WAIT, 
  RS_DONE,
  RS_EMPTY
}RobotState;

RobotState move(BtnList& list, int& pos, bool myturn);

bool CHANGE_TURN(Input* &input, bool& turnO, bool& turnB) 
{ 
  if (input->turnList.size() == 0) 
  {
    return true;
  }

  if ((input->turnList.front())->val == 'O') 
  { 
    turnO = true; 
    turnB = false; 
  } 
  else 
  { 
    turnO = false; 
    turnB = true; 
  } 
  return false;
}

int 
Jamstart(InputList& list)
{
  unsigned int cases = 0;
  InputListIterator iter;
  for (iter  = list.begin();
       iter != list.end();
       iter ++)
  {
    Input * input = *iter;
    
    int start = (input->turnList.front())->val;

    int moves = 0;
    int oPos = 1;
    int bPos = 1;
    bool turnO = start == 'O' ? true : false;
    bool turnB = start == 'B' ? true : false;
    bool brk;
    for (moves = 1; moves < 1000000; moves += 1)
    {
      RobotState oRet, bRet; 

      if (CHANGE_TURN(input, turnO, turnB)) break;
      oRet = move(input->oList, oPos, turnO);
      if (CHANGE_TURN(input, turnO, turnB)) break;
      if (oRet == RS_DONE)
      { 
        turnB = false; 
        input->turnList.erase(input->turnList.begin()); }

      bRet = move(input->bList, bPos, turnB);
      if (bRet == RS_DONE) 
      { 
        input->turnList.erase(input->turnList.begin()); }

      if (CHANGE_TURN(input, turnO, turnB)) break;
    }

    std::cout << "Case #" << ++cases << ": " << moves << std::endl;
  }
}

RobotState 
move(BtnList& list, int& pos, bool myturn)
{
  if (list.size() == 0) return RS_EMPTY;

  Btn * btn = list.front();
  if (btn->val == pos)
  {
    if (myturn)
    {
      list.erase(list.begin());
      return RS_DONE;
    }

    return RS_WAIT;
  }

  if (btn->val > pos) // move
  {
    pos += 1;
  }
  else if (btn->val < pos)
  {
    pos -= 1;
  }
  return RS_WAIT;
}

int main(int argc, char * argv[])
{
  	InputList list;
	switch(argc)
	{
	case 2:
		ReadData(list, argv[1]);
		break;
	default:
		std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
		return 1;
	}

        Jamstart(list);

	Input * input = 0;
	while (list.size() > 0)
	{
		input = list.front();
		list.erase(list.begin());
		delete input;
	}

	return 0;
}

// Read data from file
typedef enum
{
  GET_NUM,
  CHANGE_RBT,
  GET_BTN
}State;

void
ReadData(InputList& list, std::string fileName)
{
  std::ifstream fin(fileName.c_str());
  const unsigned int MAX_LINE_LENGTH = 2048;
  char line[MAX_LINE_LENGTH];

  // get number of test case
  fin.getline(line, MAX_LINE_LENGTH);
  unsigned int cases = atoi(line);

  for (unsigned int i = 0; i < cases; i += 1)
  {
    Input * input = new Input();
    BtnList * lst = 0;

    fin.getline(line, MAX_LINE_LENGTH);

    State state = GET_NUM;
    char * ptr = strtok(line, " ");
    while (ptr != 0)
    {
      switch (state)
      {
        case GET_NUM:
          input->btnRequired = atoi(ptr);
          state = CHANGE_RBT;
          break;
        case CHANGE_RBT:
          if (ptr[0] == 'O')
          {
            lst = &(input->oList);

            Btn * btn = new Btn();
            btn->val = 'O';
            input->turnList.push_back(btn);
          }
          else if (ptr[0] == 'B')
          {
            lst = &(input->bList);

            Btn * btn = new Btn();
            btn->val = 'B';
            input->turnList.push_back(btn);
          }
          else
          {
            abort();
          }
          state = GET_BTN;
          break;
        case GET_BTN:
          {
            Btn * btn = new Btn();
            btn->val = atoi(ptr);
            lst->push_back(btn);
            state = CHANGE_RBT;
          }
          break;
      }
      ptr = strtok (0, " ");
    }
    list.push_back(input);
  }

  fin.close();
}
