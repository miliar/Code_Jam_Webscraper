// AlienLanguage.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

void addQueue(short& queue, std::vector<std::pair<short, short> >& data, short pos)
{
  if(data[pos].second != -1)
    throw std::exception();
  data[pos].second = queue;
  queue = pos;
}

short popQueue(short& queue, std::vector<std::pair<short, short> >& data)
{
  short res = queue;
  queue = data[queue].second;
  data[res].second = -1;
  return res;
}

int W, H;
void check(short& queue, std::vector<std::pair<short, short> >& data, std::vector<short>& labs, short j)
{
  if(labs[j] != -1)
    return;
  int basin = j;
  if(j/W > 0 && data[j-W].first < data[basin].first)
    basin = j-W;
  if(j%W > 0 && data[j-1].first < data[basin].first)
    basin = j-1;
  if(j%W < W-1 && data[j+1].first < data[basin].first)
    basin = j+1;
  if(j/W < H-1 && data[j+W].first < data[basin].first)
    basin = j+W;
  if(labs[basin] == -1)
    return;
  labs[j] = labs[basin];
  addQueue(queue, data, j);
}

int main(int argc, char* argv[])
{
  int T;
  std::cin >> T;
  for(int i = 0; i < T; ++i)
  {
    std::cin >> H >> W;
    std::vector<std::pair<short, short> > data;
    std::vector<short> labs(W*H, -1);
    data.reserve(W*H);
    for(int j = 0; j < W*H; ++j)
    {
      short alt;
      std::cin >> alt;
      data.push_back(std::pair<short, short>(alt, -1));
    }
    short queue = -1;
    short basinID = 0;
    for(int j = 0; j < W*H; ++j)
    {
      short alt = data[j].first;
      bool basin = true;
      if(j%W > 0 && data[j-1].first < alt)
        basin = false;
      if(j%W < W-1 && data[j+1].first < alt)
        basin = false;
      if(j/W > 0 && data[j-W].first < alt)
        basin = false;
      if(j/W < H-1 && data[j+W].first < alt)
        basin = false;
      if(basin != true)
        continue;
      labs[j] = (basinID++);
      addQueue(queue, data, j);
    }
    while(queue != -1)
    {
      short j = popQueue(queue, data);
      if(j%W > 0)
        check(queue, data, labs, j-1);
      if(j%W < W-1)
        check(queue, data, labs, j+1);
      if(j/W > 0)
        check(queue, data, labs, j-W);
      if(j/W < H-1)
        check(queue, data, labs, j+W);
    }
    std::cout << "Case #"<<(i+1)<<": ";
    std::map<short, char> idmap;
    char curid = 'a';
    for(int j = 0; j < W*H; ++j)
    {
      if(j%W == 0)
        std::cout << "\n";
      if(idmap.find(labs[j]) == idmap.end())
        idmap[labs[j]] = (curid++);
      std::cout << idmap[labs[j]] << " ";
    }
    std::cout << "\n";
  }
	return 0;
}

