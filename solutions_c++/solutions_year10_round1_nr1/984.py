#pragma once
#include <iostream>

using namespace std;


class Case
{
public:
  int _boardSize;
  int _k;
  char** _board;
public:
  Case () {}
  Case (const Case& source)
  {
    _boardSize = source._boardSize;
    _k = source._k;
    _board = new char*[_boardSize];
    for (int i = 0; i < _boardSize; ++i)
    {
      _board[i] = new char[_boardSize];
      for (int j = 0; j < _boardSize; ++j)
      {
        _board[i][j] = source._board[i][j];
      }
    }
  }
  ~Case ()
  {
    for (int i = 0; i < _boardSize; ++i)
    {
      delete[] _board[i];
    }
    delete[] _board;
  }
  void read_stream (istream& input)
  {
    input >> _boardSize >> _k;
    _board = new char*[_boardSize];
    for (int i = 0; i < _boardSize; ++i)
    {
      _board[i] = new char[_boardSize];
      for (int j = 0; j < _boardSize; ++j)
      {
        input >> _board[i][j];
      }
    }
  }

};