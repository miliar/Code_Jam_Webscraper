// SAI [ 9 Aug 2009 ]
#include <stdint.h>
#include <iostream>
#include <vector>
#include <InputReader.h>

typedef std::vector<std::string>           StringList;
typedef std::vector<std::string>::iterator StringListIterator;

void flow(InputReader::Map * map, uint32_t sRow, uint32_t sCol, uint32_t& fRow, uint32_t& fCol);
char getLabel(StringList& list, uint32_t r, uint32_t c);

int main(int argc, char * argv[])
{
  if (argc < 2) return 1;

  InputReader input(argv[1]);

  for (uint32_t i = 0; i < input.maps.size(); i += 1)
  {
    InputReader::Map * map = input.maps.at(i);
    std::cout << "Case #" << (i+1) << ":" << std::endl;
    StringList cList;
    for (uint32_t r = 0; r < map->height; r += 1)
    {
      for (uint32_t c = 0; c < map->width; c += 1)
      {
        uint32_t fr,fc;
        flow(map, r, c, fr, fc);
        map->label[r][c] = getLabel(cList, fr, fc);
        std::cout << map->label[r][c] << " ";
      }
      std::cout << std::endl;
    }
  }

  return 0;
}

char 
getLabel(StringList& list, uint32_t r, uint32_t c)
{
  char buff[1024];
  sprintf(buff, "%02d-%02d", r, c);
  for (uint32_t i = 0; i < list.size(); i += 1)
  {
    std::string str = list.at(i);
    if (str.compare(buff) == 0)
    {
      return ('a' + i);
    }
  }

  // a new one
  list.push_back(buff);
  return ('a' + list.size() - 1);
}

enum {NORTH = 0, WEST = 1, EAST = 2, SOUTH = 3};

class Position
{
public:
  uint32_t r;
  uint32_t c;
};

class Info
{
public:
  Position pos;
  int32_t  val;
};

Info * Cmp(Info * a, Info * b);
Info * getN(InputReader::Map * map, uint32_t dir, Info& cur, Info& ret);

void 
flow(InputReader::Map * map, uint32_t sRow, uint32_t sCol, uint32_t& fRow, uint32_t& fCol)
{
  Info curr;
  Info neighbor [4];
  curr.pos.r = sRow;
  curr.pos.c = sCol;
  curr.val   = map->altitude[sRow][sCol];

  while (true)
  {
    Info * nPtr[4] = {0, 0, 0, 0};
  
    nPtr[NORTH] = getN(map, NORTH, curr, neighbor[NORTH]);
    nPtr[SOUTH] = getN(map, SOUTH, curr, neighbor[SOUTH]);
    nPtr[WEST]  = getN(map, WEST,  curr, neighbor[WEST]);
    nPtr[EAST]  = getN(map, EAST,  curr, neighbor[EAST]);
  
    Info * lowest = 0;
    for (uint32_t i = 0; i < 4; i += 1)
    {
      lowest = Cmp(nPtr[i], lowest);
    }

    if (!lowest)
    {
      fRow = curr.pos.r;
      fCol = curr.pos.c;
      return;
    }

    // Handle tie
    if (nPtr[NORTH] && nPtr[NORTH]->val == lowest->val)
    {
      lowest = nPtr[NORTH];
    }
    else if (nPtr[WEST] && nPtr[WEST]->val == lowest->val)
    {
      lowest = nPtr[WEST];
    }
    else if (nPtr[EAST] && nPtr[EAST]->val == lowest->val)
    {
      lowest = nPtr[EAST];
    }
  
    curr.pos.r = lowest->pos.r;
    curr.pos.c = lowest->pos.c;
    curr.val   = lowest->val;
  }
}

Info * getN(InputReader::Map * map, uint32_t dir, Info& cur, Info& ret)
{
  int32_t r,c;
  r = (int32_t)cur.pos.r;
  c = (int32_t)cur.pos.c;

  switch(dir)
  {
    case NORTH:
      r -= 1;
      break;
    case SOUTH:
      r += 1;
      break;
    case EAST:
      c += 1;
      break;
    case WEST:
      c -= 1;
      break;
  }

  if ((c < 0 || r < 0) || (r >= map->height || c >= map->width))
  {
    return 0;
  }
  else
  {
    uint32_t val = map->altitude[r][c];
    if (cur.val <= val)
    {
      return 0;
    }

    ret.val = val;
    ret.pos.r = r;
    ret.pos.c = c;
    return &ret;
  }
}

Info * Cmp(Info * a, Info * b)
{
  if (b == 0) return a;
  if (a == 0) return b;
  if (a->val < b->val) return a;

  return b;
}
